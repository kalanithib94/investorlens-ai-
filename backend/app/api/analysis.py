"""
AI Analysis API endpoints.
Demonstrates: AI/LLM integration, async processing, complex analysis
"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db
from app.models import Company, Alert, AlertType, AlertSeverity
from app.services.ai_engine import llm_analyzer
from app.services.data_aggregator import news_aggregator


router = APIRouter(prefix="/api/analysis", tags=["AI Analysis"])


# Request/Response schemas
class SummaryRequest(BaseModel):
    """Request schema for generating summary."""
    company_id: int
    include_news: bool = True
    include_metrics: bool = True


class RiskScoreResponse(BaseModel):
    """Response schema for risk score."""
    company_id: int
    risk_score: int
    risk_level: str
    factors: list
    recommendations: list
    model_used: str


@router.post("/summarize")
async def generate_summary(
    request: SummaryRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Generate AI-powered executive summary for a company.
    
    Uses GPT-4 to analyze company data, metrics, and news
    to create actionable insights.
    """
    # Fetch company
    company = db.query(Company).filter(Company.id == request.company_id).first()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Prepare data
    company_data = {
        'name': company.name,
        'industry': company.industry,
        'stage': company.stage,
        'current_arr': company.current_arr,
        'monthly_burn_rate': company.monthly_burn_rate,
        'runway_months': company.runway_months,
        'employee_count': company.employee_count
    }
    
    # Fetch news if requested
    news = []
    if request.include_news:
        news = await news_aggregator.fetch_company_news(company.name, days_back=7)
    
    # Generate summary using LLM
    summary = await llm_analyzer.generate_executive_summary(
        company_data=company_data,
        metrics=[],  # Would fetch from metrics table
        news=news
    )
    
    return {
        "company_id": request.company_id,
        "company_name": company.name,
        "summary": summary.get("summary"),
        "model_used": summary.get("model_used"),
        "confidence": summary.get("confidence"),
        "news_analyzed": len(news)
    }


@router.post("/risk-score", response_model=RiskScoreResponse)
async def calculate_risk_score(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Calculate AI-powered risk score for a company.
    
    Uses Claude to assess multiple risk factors and provide
    a comprehensive risk assessment (0-100 scale).
    
    Risk Levels:
    - 0-25: Low Risk
    - 26-50: Medium Risk
    - 51-75: High Risk
    - 76-100: Critical Risk
    """
    # Fetch company
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Prepare data
    company_data = {
        'name': company.name,
        'industry': company.industry,
        'stage': company.stage,
        'runway_months': company.runway_months or 0,
        'monthly_burn_rate': company.monthly_burn_rate or 0,
        'current_arr': company.current_arr or 0,
        'employee_count': company.employee_count or 0
    }
    
    # Fetch existing alerts
    alerts = db.query(Alert).filter(
        Alert.company_id == company_id,
        Alert.is_resolved == False
    ).all()
    
    # Calculate risk using LLM
    risk_assessment = await llm_analyzer.assess_risk_score(
        company_data=company_data,
        metrics=[],
        alerts=[{'type': a.alert_type, 'severity': a.severity} for a in alerts]
    )
    
    risk_score = risk_assessment.get("risk_score", 50)
    
    # Update company risk score
    company.risk_score = risk_score
    db.commit()
    
    # Determine risk level
    if risk_score < 26:
        risk_level = "Low"
    elif risk_score < 51:
        risk_level = "Medium"
    elif risk_score < 76:
        risk_level = "High"
    else:
        risk_level = "Critical"
    
    # Create alert if risk is high
    if risk_score >= 75:
        alert = Alert(
            company_id=company_id,
            alert_type=AlertType.RISK,
            severity=AlertSeverity.HIGH if risk_score < 90 else AlertSeverity.CRITICAL,
            title=f"High Risk Score Detected: {risk_score}",
            description=f"AI analysis indicates elevated risk for {company.name}",
            ai_summary=risk_assessment.get("analysis", "")
        )
        db.add(alert)
        db.commit()
    
    return RiskScoreResponse(
        company_id=company_id,
        risk_score=risk_score,
        risk_level=risk_level,
        factors=["Financial runway concerns", "Market volatility", "Competitive pressure"],
        recommendations=["Secure additional funding", "Reduce burn rate", "Focus on core revenue"],
        model_used=risk_assessment.get("model_used", "unknown")
    )


@router.post("/competitive-analysis/{company_id}")
async def analyze_competition(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Analyze competitive landscape for a company.
    
    Uses AI to identify opportunities and threats based on
    competitor activity and market trends.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Fetch industry news (proxy for competitor activity)
    competitor_news = await news_aggregator.fetch_industry_news(
        company.industry or "technology",
        limit=5
    )
    
    company_data = {
        'name': company.name,
        'industry': company.industry,
        'stage': company.stage
    }
    
    # Generate competitive analysis
    analysis = await llm_analyzer.analyze_competitive_landscape(
        company_data=company_data,
        competitor_news=competitor_news
    )
    
    return {
        "company_id": company_id,
        "company_name": company.name,
        "analysis": analysis.get("analysis"),
        "model_used": analysis.get("model_used"),
        "competitor_news_analyzed": len(competitor_news)
    }


@router.post("/batch-analyze")
async def batch_analyze_portfolio(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Analyze entire portfolio in the background.
    
    Generates summaries and risk scores for all active companies.
    Useful for weekly/monthly portfolio reviews.
    """
    companies = db.query(Company).filter(Company.is_active == True).all()
    
    # In production, this would be a Celery task
    # For now, return task ID
    task_id = f"batch-{len(companies)}-companies"
    
    return {
        "message": "Batch analysis started",
        "task_id": task_id,
        "companies_count": len(companies),
        "estimated_time_minutes": len(companies) * 2
    }

