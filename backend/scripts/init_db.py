"""
Database initialization script.
Creates tables and optionally adds sample data.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import init_db, SessionLocal
from app.models import Company, Metric, Alert, AlertType, AlertSeverity
from datetime import datetime, timedelta
import random


def create_sample_data():
    """Create sample portfolio companies for demo purposes."""
    db = SessionLocal()
    
    try:
        # Sample companies
        companies_data = [
            {
                "name": "TechFlow AI",
                "description": "AI-powered workflow automation platform",
                "industry": "Enterprise Software",
                "stage": "Series B",
                "website": "https://techflow.ai",
                "investment_amount": 5000000,
                "ownership_percentage": 15.0,
                "current_arr": 3500000,
                "monthly_burn_rate": 250000,
                "runway_months": 18,
                "employee_count": 45,
                "risk_score": 35,
                "health_score": 75
            },
            {
                "name": "HealthHub",
                "description": "Telemedicine and health records platform",
                "industry": "Healthcare",
                "stage": "Series A",
                "website": "https://healthhub.com",
                "investment_amount": 3000000,
                "ownership_percentage": 20.0,
                "current_arr": 1200000,
                "monthly_burn_rate": 180000,
                "runway_months": 14,
                "employee_count": 28,
                "risk_score": 45,
                "health_score": 65
            },
            {
                "name": "EcoTrack",
                "description": "Sustainability tracking for enterprises",
                "industry": "Climate Tech",
                "stage": "Seed",
                "website": "https://ecotrack.io",
                "investment_amount": 1500000,
                "ownership_percentage": 25.0,
                "current_arr": 400000,
                "monthly_burn_rate": 120000,
                "runway_months": 10,
                "employee_count": 12,
                "risk_score": 65,
                "health_score": 55
            },
            {
                "name": "FinanceOS",
                "description": "Modern financial operations platform",
                "industry": "FinTech",
                "stage": "Series A",
                "website": "https://financeos.com",
                "investment_amount": 4000000,
                "ownership_percentage": 18.0,
                "current_arr": 2800000,
                "monthly_burn_rate": 200000,
                "runway_months": 20,
                "employee_count": 35,
                "risk_score": 30,
                "health_score": 80
            }
        ]
        
        print("Creating sample companies...")
        for company_data in companies_data:
            company = Company(**company_data)
            db.add(company)
            print(f"  ✓ Created: {company_data['name']}")
        
        db.commit()
        
        # Create sample alerts
        companies = db.query(Company).all()
        
        print("\nCreating sample alerts...")
        alerts_data = [
            {
                "company_id": companies[2].id,  # EcoTrack (high risk)
                "alert_type": AlertType.RISK,
                "severity": AlertSeverity.HIGH,
                "title": "Low Runway Warning",
                "description": "Company has only 10 months of runway remaining at current burn rate.",
                "ai_summary": "Analysis suggests securing additional funding within the next quarter."
            },
            {
                "company_id": companies[1].id,  # HealthHub
                "alert_type": AlertType.OPPORTUNITY,
                "severity": AlertSeverity.MEDIUM,
                "title": "Market Expansion Opportunity",
                "description": "Recent competitor acquisition suggests strong market consolidation.",
                "ai_summary": "Consider strategic partnerships or acquisition discussions."
            },
            {
                "company_id": companies[0].id,  # TechFlow AI
                "alert_type": AlertType.NEWS,
                "severity": AlertSeverity.LOW,
                "title": "Positive Press Coverage",
                "description": "Featured in TechCrunch as 'Top 10 AI Startups to Watch'.",
                "ai_summary": "Positive brand recognition could accelerate customer acquisition."
            }
        ]
        
        for alert_data in alerts_data:
            alert = Alert(**alert_data)
            db.add(alert)
            print(f"  ✓ Created alert for: {companies[alert_data['company_id']-1].name}")
        
        db.commit()
        
        print("\n✅ Sample data created successfully!")
        print(f"\nCreated:")
        print(f"  - {len(companies_data)} companies")
        print(f"  - {len(alerts_data)} alerts")
        
    except Exception as e:
        print(f"\n❌ Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()


def main():
    """Initialize database and optionally create sample data."""
    print("Initializing InvestorLens AI database...")
    print("=" * 50)
    
    try:
        # Create all tables
        print("\n1. Creating database tables...")
        init_db()
        print("   ✓ Tables created successfully!")
        
        # Ask if user wants sample data
        print("\n2. Would you like to create sample data? (y/n): ", end="")
        choice = input().lower().strip()
        
        if choice == 'y':
            create_sample_data()
        else:
            print("   Skipping sample data creation.")
        
        print("\n" + "=" * 50)
        print("✅ Database initialization complete!")
        print("\nYou can now start the server with:")
        print("   uvicorn app.main:app --reload")
        
    except Exception as e:
        print(f"\n❌ Error initializing database: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

