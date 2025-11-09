"""
Add realistic demo data to InvestorLens AI platform
Run this to populate your dashboard with sample companies and alerts
"""

import requests
import random
from datetime import datetime, timedelta

# Your Railway backend URL
API_URL = "https://portfolio-intelligence-production-58fa.up.railway.app"

# Demo companies with realistic data
DEMO_COMPANIES = [
    {
        "name": "TechVision AI",
        "industry": "Artificial Intelligence",
        "stage": "Series B",
        "current_arr": 5200000,
        "monthly_burn_rate": 280000,
        "runway_months": 18,
        "risk_score": 35,
        "is_active": True,
        "website": "https://techvision.ai",
        "description": "AI-powered analytics platform for enterprise data"
    },
    {
        "name": "CloudFlow Systems",
        "industry": "Cloud Infrastructure",
        "stage": "Series A",
        "current_arr": 2800000,
        "monthly_burn_rate": 180000,
        "runway_months": 14,
        "risk_score": 42,
        "is_active": True,
        "website": "https://cloudflow.io",
        "description": "Modern cloud orchestration and deployment platform"
    },
    {
        "name": "FinSecure Pro",
        "industry": "FinTech",
        "stage": "Seed",
        "current_arr": 980000,
        "monthly_burn_rate": 95000,
        "runway_months": 10,
        "risk_score": 58,
        "is_active": True,
        "website": "https://finsecure.co",
        "description": "Next-gen fraud detection and prevention platform"
    },
    {
        "name": "HealthTech Plus",
        "industry": "Healthcare Technology",
        "stage": "Series B",
        "current_arr": 6500000,
        "monthly_burn_rate": 320000,
        "runway_months": 22,
        "risk_score": 28,
        "is_active": True,
        "website": "https://healthtechplus.com",
        "description": "Patient data management and telehealth solutions"
    },
    {
        "name": "EduLearn Global",
        "industry": "EdTech",
        "stage": "Series A",
        "current_arr": 3200000,
        "monthly_burn_rate": 210000,
        "runway_months": 16,
        "risk_score": 45,
        "is_active": True,
        "website": "https://edulearn.io",
        "description": "AI-powered personalized learning platform"
    },
    {
        "name": "GreenEnergy Solutions",
        "industry": "Clean Energy",
        "stage": "Series C",
        "current_arr": 12500000,
        "monthly_burn_rate": 450000,
        "runway_months": 28,
        "risk_score": 22,
        "is_active": True,
        "website": "https://greenenergy.tech",
        "description": "Smart grid optimization and renewable energy management"
    },
    {
        "name": "RetailX Analytics",
        "industry": "Retail Tech",
        "stage": "Seed",
        "current_arr": 750000,
        "monthly_burn_rate": 125000,
        "runway_months": 6,
        "risk_score": 72,
        "is_active": True,
        "website": "https://retailx.ai",
        "description": "Customer behavior analytics and inventory optimization"
    },
    {
        "name": "SecureAuth Systems",
        "industry": "Cybersecurity",
        "stage": "Series A",
        "current_arr": 4100000,
        "monthly_burn_rate": 250000,
        "runway_months": 20,
        "risk_score": 31,
        "is_active": True,
        "website": "https://secureauth.io",
        "description": "Zero-trust authentication and identity management"
    }
]

# Demo alerts
DEMO_ALERTS = [
    {
        "severity": "high",
        "title": "Burn Rate Exceeding Projections",
        "description": "Monthly burn increased by 15% compared to last quarter. Immediate review recommended.",
        "company_name": "RetailX Analytics"
    },
    {
        "severity": "medium",
        "title": "Runway Below 12 Months",
        "description": "Current cash runway has dropped below the 12-month threshold. Consider follow-on funding.",
        "company_name": "RetailX Analytics"
    },
    {
        "severity": "critical",
        "title": "Significant Market Downturn Detected",
        "description": "Competitor analysis shows 3 similar companies experienced 20%+ revenue decline this quarter.",
        "company_name": "FinSecure Pro"
    },
    {
        "severity": "low",
        "title": "Strong Performance Metrics",
        "description": "ARR growth exceeding targets by 25%. Team expansion recommended.",
        "company_name": "HealthTech Plus"
    },
    {
        "severity": "high",
        "title": "Key Customer Churn Alert",
        "description": "2 enterprise customers (representing 18% of ARR) at risk based on usage metrics.",
        "company_name": "EduLearn Global"
    }
]

def add_companies():
    """Add demo companies to the platform."""
    print("Adding demo companies...")
    added_companies = []
    
    for company in DEMO_COMPANIES:
        try:
            response = requests.post(
                f"{API_URL}/api/companies",
                json=company,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                company_data = response.json()
                added_companies.append(company_data)
                print(f"  [OK] Added: {company['name']}")
            else:
                print(f"  [ERROR] Failed to add {company['name']}: {response.status_code}")
                
        except Exception as e:
            print(f"  [ERROR] Error adding {company['name']}: {e}")
    
    return added_companies

def add_alerts(companies):
    """Add demo alerts for companies."""
    print("\nAdding demo alerts...")
    
    # Map company names to IDs
    company_map = {c.get('name'): c.get('id') for c in companies if c.get('id')}
    
    for alert in DEMO_ALERTS:
        company_id = company_map.get(alert['company_name'])
        if not company_id:
            print(f"  [WARN] Skipping alert for {alert['company_name']} (company not found)")
            continue
            
        try:
            alert_data = {
                "company_id": company_id,
                "severity": alert['severity'],
                "title": alert['title'],
                "description": alert['description'],
                "source": "demo_data_script"
            }
            
            response = requests.post(
                f"{API_URL}/api/alerts",
                json=alert_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"  [OK] Added: {alert['title'][:50]}...")
            else:
                print(f"  [ERROR] Failed to add alert: {response.status_code}")
                
        except Exception as e:
            print(f"  [ERROR] Error adding alert: {e}")

def verify_data():
    """Verify data was added successfully."""
    print("\nVerifying data...")
    
    try:
        # Check companies
        companies_response = requests.get(f"{API_URL}/api/companies")
        companies = companies_response.json()
        print(f"  [OK] Companies in database: {len(companies)}")
        
        # Check alerts
        alerts_response = requests.get(f"{API_URL}/api/alerts")
        alerts = alerts_response.json()
        print(f"  [OK] Alerts in database: {len(alerts)}")
        
        # Get alert stats
        stats_response = requests.get(f"{API_URL}/api/alerts/stats/summary")
        stats = stats_response.json()
        print(f"  [OK] Alert stats: {stats}")
        
    except Exception as e:
        print(f"  [ERROR] Error verifying data: {e}")

def main():
    """Main function to add all demo data."""
    print("InvestorLens AI - Demo Data Setup")
    print("=" * 50)
    print(f"API URL: {API_URL}")
    print("=" * 50)
    print()
    
    # Test API connectivity
    try:
        health_response = requests.get(f"{API_URL}/health", timeout=5)
        if health_response.status_code == 200:
            print("[OK] Backend is healthy and accessible")
            print()
        else:
            print("[ERROR] Backend health check failed")
            return
    except Exception as e:
        print(f"[ERROR] Cannot connect to backend: {e}")
        print("Please verify the backend URL is correct and accessible.")
        return
    
    # Add data
    companies = add_companies()
    
    if companies:
        add_alerts(companies)
    
    verify_data()
    
    print()
    print("=" * 50)
    print("Demo data setup complete!")
    print("=" * 50)
    print()
    print("Visit your dashboard to see the data:")
    print("https://frontend-mwzubpsvx-kalanithib94s-projects.vercel.app")
    print()

if __name__ == "__main__":
    main()

