"""Add companies with completely new names"""
import requests

API_URL = "https://investorlens-ai-production.up.railway.app"

companies = [
    {"name": "Quantum Dynamics Ltd", "industry": "AI", "stage": "Series B", "current_arr": 5200000, "monthly_burn_rate": 280000, "runway_months": 18, "risk_score": 35, "is_active": True, "employee_count": 45},
    {"name": "Velocity Cloud Inc", "industry": "SaaS", "stage": "Series A", "current_arr": 2800000, "monthly_burn_rate": 180000, "runway_months": 14, "risk_score": 42, "is_active": True, "employee_count": 32},
    {"name": "PayFlow Secure", "industry": "FinTech", "stage": "Seed", "current_arr": 980000, "monthly_burn_rate": 95000, "runway_months": 10, "risk_score": 68, "is_active": True, "employee_count": 18},
    {"name": "HealthBridge Pro", "industry": "Healthcare", "stage": "Series B", "current_arr": 6500000, "monthly_burn_rate": 320000, "runway_months": 24, "risk_score": 22, "is_active": True, "employee_count": 68},
    {"name": "RetailVision360", "industry": "Retail", "stage": "Seed", "current_arr": 650000, "monthly_burn_rate": 125000, "runway_months": 5, "risk_score": 85, "is_active": True, "employee_count": 12},
    {"name": "EcoSmart Energy", "industry": "CleanTech", "stage": "Series C", "current_arr": 14200000, "monthly_burn_rate": 450000, "runway_months": 32, "risk_score": 18, "is_active": True, "employee_count": 95},
    {"name": "LearnHub Platform", "industry": "EdTech", "stage": "Series A", "current_arr": 3100000, "monthly_burn_rate": 215000, "runway_months": 15, "risk_score": 48, "is_active": True, "employee_count": 38},
    {"name": "CyberGuard Elite", "industry": "Security", "stage": "Series B", "current_arr": 8900000, "monthly_burn_rate": 380000, "runway_months": 26, "risk_score": 25, "is_active": True, "employee_count": 72}
]

for c in companies:
    r = requests.post(f"{API_URL}/api/companies", json=c)
    print(f"[{r.status_code}] {c['name']} - Risk: {c['risk_score']}")
    
print("\nDone!")

