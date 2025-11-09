"""Add fresh demo data with new company names"""

import requests

API_URL = "https://portfolio-intelligence-production-58fa.up.railway.app"

COMPANIES = [
    {
        "name": "NexusAI Corp",
        "industry": "Artificial Intelligence",
        "stage": "Series B",
        "current_arr": 5200000,
        "monthly_burn_rate": 280000,
        "runway_months": 18,
        "risk_score": 35,
        "is_active": True,
        "employee_count": 45
    },
    {
        "name": "DataStream Technologies",
        "industry": "Cloud Infrastructure", 
        "stage": "Series A",
        "current_arr": 2800000,
        "monthly_burn_rate": 180000,
        "runway_months": 14,
        "risk_score": 42,
        "is_active": True,
        "employee_count": 32
    },
    {
        "name": "PaySecure Labs",
        "industry": "FinTech",
        "stage": "Seed",
        "current_arr": 980000,
        "monthly_burn_rate": 95000,
        "runway_months": 10,
        "risk_score": 68,
        "is_active": True,
        "employee_count": 18
    },
    {
        "name": "MedVision Health",
        "industry": "Healthcare",
        "stage": "Series B",
        "current_arr": 6500000,
        "monthly_burn_rate": 320000,
        "runway_months": 24,
        "risk_score": 22,
        "is_active": True,
        "employee_count": 68
    },
    {
        "name": "ShopMetrics AI",
        "industry": "Retail Tech",
        "stage": "Seed",
        "current_arr": 650000,
        "monthly_burn_rate": 125000,
        "runway_months": 5,
        "risk_score": 85,
        "is_active": True,
        "employee_count": 12
    },
    {
        "name": "SolarGrid Innovations",
        "industry": "Clean Energy",
        "stage": "Series C",
        "current_arr": 14200000,
        "monthly_burn_rate": 450000,
        "runway_months": 32,
        "risk_score": 18,
        "is_active": True,
        "employee_count": 95
    },
    {
        "name": "SmartLearn Platform",
        "industry": "EdTech",
        "stage": "Series A",
        "current_arr": 3100000,
        "monthly_burn_rate": 215000,
        "runway_months": 15,
        "risk_score": 48,
        "is_active": True,
        "employee_count": 38
    },
    {
        "name": "DefenseNet Systems",
        "industry": "Cybersecurity",
        "stage": "Series B",
        "current_arr": 8900000,
        "monthly_burn_rate": 380000,
        "runway_months": 26,
        "risk_score": 25,
        "is_active": True,
        "employee_count": 72
    }
]

print("Adding companies...")
for company in COMPANIES:
    try:
        response = requests.post(f"{API_URL}/api/companies", json=company, timeout=10)
        if response.status_code in [200, 201]:
            risk = "LOW" if company['risk_score'] < 35 else "MED" if company['risk_score'] < 60 else "HIGH"
            print(f"[OK] {company['name']} - Risk: {company['risk_score']}/100 ({risk})")
        else:
            print(f"[ERROR] {company['name']}: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] {company['name']}: {e}")

print("\nDone! Refresh your dashboard.")

