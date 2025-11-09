"""Check what's actually in the database"""

import requests
import json

API_URL = "https://portfolio-intelligence-production-58fa.up.railway.app"

print("Checking database contents...")
print("=" * 60)

# Get all companies
response = requests.get(f"{API_URL}/api/companies")
companies = response.json()

print(f"\nTotal Companies: {len(companies)}")
print("=" * 60)

for company in companies:
    print(f"\nCompany: {company.get('name')}")
    print(f"  ID: {company.get('id')}")
    print(f"  Industry: {company.get('industry')}")
    print(f"  Stage: {company.get('stage')}")
    print(f"  Risk Score: {company.get('risk_score')}")
    print(f"  ARR: ${company.get('current_arr'):,.0f}" if company.get('current_arr') else "  ARR: None")
    print(f"  Burn Rate: ${company.get('monthly_burn_rate'):,.0f}/mo" if company.get('monthly_burn_rate') else "  Burn Rate: None")
    print(f"  Runway: {company.get('runway_months')} months" if company.get('runway_months') else "  Runway: None")
    print(f"  Employees: {company.get('employee_count')}" if company.get('employee_count') else "  Employees: None")

print("\n" + "=" * 60)
print("Full JSON of first company:")
print(json.dumps(companies[0] if companies else {}, indent=2))

