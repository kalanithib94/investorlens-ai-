"""
Reset database and add realistic, varied demo data
This will showcase the platform's value with diverse risk profiles
"""

import requests

API_URL = "https://portfolio-intelligence-production-58fa.up.railway.app"

# More realistic and varied companies
COMPANIES = [
    {
        "name": "TechVision AI",
        "industry": "Artificial Intelligence",
        "stage": "Series B",
        "current_arr": 5200000,
        "monthly_burn_rate": 280000,
        "runway_months": 18,
        "risk_score": 35,
        "is_active": True,
        "employee_count": 45,
        "description": "AI-powered analytics platform"
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
        "employee_count": 32,
        "description": "Cloud orchestration platform"
    },
    {
        "name": "FinSecure Pro",
        "industry": "FinTech",
        "stage": "Seed",
        "current_arr": 980000,
        "monthly_burn_rate": 95000,
        "runway_months": 10,
        "risk_score": 68,  # High risk - low runway
        "is_active": True,
        "employee_count": 18,
        "description": "Fraud detection platform"
    },
    {
        "name": "HealthTech Plus",
        "industry": "Healthcare",
        "stage": "Series B",
        "current_arr": 6500000,
        "monthly_burn_rate": 320000,
        "runway_months": 24,
        "risk_score": 22,  # Low risk - strong metrics
        "is_active": True,
        "employee_count": 68,
        "description": "Telehealth solutions"
    },
    {
        "name": "RetailX Analytics",
        "industry": "Retail Tech",
        "stage": "Seed",
        "current_arr": 650000,
        "monthly_burn_rate": 125000,
        "runway_months": 5,
        "risk_score": 85,  # Critical - very low runway
        "is_active": True,
        "employee_count": 12,
        "description": "Retail analytics platform"
    },
    {
        "name": "GreenEnergy Solutions",
        "industry": "Clean Energy",
        "stage": "Series C",
        "current_arr": 14200000,
        "monthly_burn_rate": 450000,
        "runway_months": 32,
        "risk_score": 18,  # Very low risk
        "is_active": True,
        "employee_count": 95,
        "description": "Smart grid optimization"
    },
    {
        "name": "EduLearn Global",
        "industry": "EdTech",
        "stage": "Series A",
        "current_arr": 3100000,
        "monthly_burn_rate": 215000,
        "runway_months": 15,
        "risk_score": 48,  # Medium risk
        "is_active": True,
        "employee_count": 38,
        "description": "AI-powered learning platform"
    },
    {
        "name": "CyberShield Pro",
        "industry": "Cybersecurity",
        "stage": "Series B",
        "current_arr": 8900000,
        "monthly_burn_rate": 380000,
        "runway_months": 26,
        "risk_score": 25,  # Low risk
        "is_active": True,
        "employee_count": 72,
        "description": "Enterprise security platform"
    }
]

def delete_all_companies():
    """Delete existing companies."""
    print("Clearing existing data...")
    try:
        response = requests.get(f"{API_URL}/api/companies")
        companies = response.json()
        
        for company in companies:
            delete_response = requests.delete(f"{API_URL}/api/companies/{company['id']}")
            if delete_response.status_code in [200, 204]:
                print(f"  [OK] Deleted: {company['name']}")
        print()
    except Exception as e:
        print(f"  [WARN] Could not clear data: {e}")
        print()

def add_companies():
    """Add companies with varied data."""
    print("Adding portfolio companies...")
    added = []
    
    for company in COMPANIES:
        try:
            response = requests.post(
                f"{API_URL}/api/companies",
                json=company,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                data = response.json()
                added.append(data)
                risk_level = "LOW" if company['risk_score'] < 35 else "MED" if company['risk_score'] < 60 else "HIGH"
                print(f"  [OK] {company['name']} - Risk: {company['risk_score']}/100 ({risk_level})")
            else:
                print(f"  [ERROR] Failed: {company['name']} - Status: {response.status_code}")
                print(f"         Response: {response.text[:100]}")
                
        except Exception as e:
            print(f"  [ERROR] {company['name']}: {e}")
    
    print()
    return added

def show_summary():
    """Show summary of data."""
    try:
        response = requests.get(f"{API_URL}/api/companies")
        companies = response.json()
        
        print("=" * 60)
        print("PORTFOLIO SUMMARY")
        print("=" * 60)
        print(f"Total Companies: {len(companies)}")
        
        if companies:
            avg_risk = sum(c.get('risk_score', 0) for c in companies) / len(companies)
            print(f"Average Risk Score: {avg_risk:.1f}/100")
            
            low_risk = len([c for c in companies if c.get('risk_score', 0) < 35])
            medium_risk = len([c for c in companies if 35 <= c.get('risk_score', 0) < 60])
            high_risk = len([c for c in companies if c.get('risk_score', 0) >= 60])
            
            print(f"Low Risk: {low_risk} companies")
            print(f"Medium Risk: {medium_risk} companies")
            print(f"High Risk: {high_risk} companies")
        
        print("=" * 60)
        print()
        print("Visit your dashboard:")
        print("https://frontend-mwzubpsvx-kalanithib94s-projects.vercel.app")
        print()
        
    except Exception as e:
        print(f"[ERROR] {e}")

def main():
    print("InvestorLens AI - Demo Data Setup")
    print("=" * 60)
    
    # Test connection
    try:
        health = requests.get(f"{API_URL}/health", timeout=5)
        if health.status_code == 200:
            print("[OK] Backend connected")
            print()
        else:
            print("[ERROR] Backend not healthy")
            return
    except Exception as e:
        print(f"[ERROR] Cannot connect: {e}")
        return
    
    # Reset and add data
    delete_all_companies()
    companies = add_companies()
    show_summary()

if __name__ == "__main__":
    main()

