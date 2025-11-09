"""
Company management API endpoints.
Demonstrates: RESTful API design, CRUD operations, data validation
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from datetime import datetime

from app.core.database import get_db
from app.models import Company
from app.services.ai_engine import llm_analyzer
from app.services.data_aggregator import news_aggregator


router = APIRouter(prefix="/api/companies", tags=["Companies"])


# Pydantic schemas for request/response validation
class CompanyBase(BaseModel):
    """Base company schema."""
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    stage: Optional[str] = None
    investment_amount: Optional[float] = None
    ownership_percentage: Optional[float] = Field(None, ge=0, le=100)
    ceo_name: Optional[str] = None
    headquarters: Optional[str] = None


class CompanyCreate(CompanyBase):
    """Schema for creating a company."""
    current_arr: Optional[float] = None
    monthly_burn_rate: Optional[float] = None
    runway_months: Optional[int] = None
    employee_count: Optional[int] = None
    risk_score: Optional[int] = Field(None, ge=0, le=100)


class CompanyUpdate(BaseModel):
    """Schema for updating a company."""
    name: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    current_arr: Optional[float] = None
    monthly_burn_rate: Optional[float] = None
    runway_months: Optional[int] = None
    employee_count: Optional[int] = None


class CompanyResponse(CompanyBase):
    """Schema for company response."""
    id: int
    risk_score: int
    health_score: int
    current_arr: Optional[float]
    monthly_burn_rate: Optional[float]
    runway_months: Optional[int]
    employee_count: Optional[int]
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# API Endpoints

@router.get("", response_model=List[CompanyResponse])
async def list_companies(
    skip: int = 0,
    limit: int = 100,
    industry: Optional[str] = None,
    stage: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    List all portfolio companies with optional filtering.
    
    Query Parameters:
    - skip: Number of records to skip (pagination)
    - limit: Maximum number of records to return
    - industry: Filter by industry
    - stage: Filter by funding stage
    """
    query = db.query(Company).filter(Company.is_active == True)
    
    if industry:
        query = query.filter(Company.industry == industry)
    if stage:
        query = query.filter(Company.stage == stage)
    
    companies = query.offset(skip).limit(limit).all()
    return companies


@router.post("", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
async def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    """
    Add a new portfolio company.
    
    Validates input and creates company record in database.
    """
    # Check if company with same name already exists
    existing = db.query(Company).filter(Company.name == company.name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Company with name '{company.name}' already exists"
        )
    
    # Create new company
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    
    return db_company


@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Get detailed information about a specific company.
    
    Path Parameters:
    - company_id: Unique identifier of the company
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found"
        )
    
    return company


@router.put("/{company_id}", response_model=CompanyResponse)
async def update_company(
    company_id: int,
    company_update: CompanyUpdate,
    db: Session = Depends(get_db)
):
    """
    Update company information.
    
    Only provided fields will be updated.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found"
        )
    
    # Update only provided fields
    update_data = company_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(company, field, value)
    
    db.commit()
    db.refresh(company)
    
    return company


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Soft delete a company (marks as inactive).
    
    Path Parameters:
    - company_id: Unique identifier of the company
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found"
        )
    
    company.is_active = False
    db.commit()
    
    return None


@router.get("/{company_id}/news")
async def get_company_news(
    company_id: int,
    days_back: int = 7,
    db: Session = Depends(get_db)
):
    """
    Fetch recent news articles about a company.
    
    Integrates with external news APIs.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found"
        )
    
    # Fetch news from external API
    news = await news_aggregator.fetch_company_news(company.name, days_back)
    
    return {
        "company_id": company_id,
        "company_name": company.name,
        "news_count": len(news),
        "articles": news
    }


@router.get("/{company_id}/insights")
async def get_company_insights(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Get AI-generated insights for a company.
    
    Combines metrics, news, and AI analysis.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id {company_id} not found"
        )
    
    # Fetch related data
    metrics = db.query(Company).filter(Company.id == company_id).first()  # Simplified
    news = await news_aggregator.fetch_company_news(company.name, days_back=7)
    
    # Generate AI insights
    company_data = {
        'name': company.name,
        'industry': company.industry,
        'stage': company.stage,
        'runway_months': company.runway_months,
        'monthly_burn_rate': company.monthly_burn_rate,
        'current_arr': company.current_arr
    }
    
    summary = await llm_analyzer.generate_executive_summary(
        company_data=company_data,
        metrics=[],
        news=news
    )
    
    return {
        "company_id": company_id,
        "company_name": company.name,
        "executive_summary": summary,
        "recent_news_count": len(news)
    }

