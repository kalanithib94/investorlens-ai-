"""Add realistic alerts for portfolio companies"""
import requests

API_URL = "https://portfolio-intelligence-production-58fa.up.railway.app"

# Get companies first to get their IDs
companies_response = requests.get(f"{API_URL}/api/companies")
companies = companies_response.json()

# Create a map of company names to IDs
company_map = {}
for c in companies:
    company_map[c['name']] = c['id']
    print(f"Found: {c['name']} (ID: {c['id']}, Risk: {c['risk_score']})")

print("\nAdding alerts...")

# Add alerts based on actual risks
alerts = [
    {
        "company_id": company_map.get("RetailVision360"),  # Risk: 85, Runway: 5 months
        "severity": "critical",
        "title": "Critical: Runway Below 6 Months",
        "description": "RetailVision360 has only 5 months of runway remaining at current burn rate. Immediate fundraising or cost reduction required.",
        "source": "automated_risk_analysis"
    },
    {
        "company_id": company_map.get("PayFlow Secure"),  # Risk: 68, Runway: 10 months
        "severity": "high",
        "title": "High Burn Rate Detected",
        "description": "Burn rate of $95K/month is high relative to $980K ARR. Revenue growth not keeping pace with expenses.",
        "source": "financial_metrics"
    },
    {
        "company_id": company_map.get("RetailVision360"),
        "severity": "critical",
        "title": "Negative Unit Economics Alert",
        "description": "Customer acquisition cost exceeding lifetime value. Business model sustainability at risk.",
        "source": "ai_analysis"
    },
    {
        "company_id": company_map.get("PayFlow Secure"),
        "severity": "high", 
        "title": "Market Competition Intensifying",
        "description": "3 new competitors raised funding in FinTech space. Market share protection strategy needed.",
        "source": "competitive_intelligence"
    },
    {
        "company_id": company_map.get("LearnHub Platform"),  # Risk: 48
        "severity": "medium",
        "title": "Churn Rate Increasing",
        "description": "Customer churn up 12% QoQ. Product engagement metrics declining.",
        "source": "analytics_engine"
    },
    {
        "company_id": company_map.get("EcoSmart Energy"),  # Risk: 18 - Low risk
        "severity": "low",
        "title": "Strong Performance - Expansion Opportunity",
        "description": "ARR growing 40% YoY with healthy margins. Consider Series D fundraising for expansion.",
        "source": "growth_analysis"
    },
    {
        "company_id": company_map.get("HealthBridge Pro"),  # Risk: 22 - Low risk
        "severity": "low",
        "title": "Positive Market Sentiment",
        "description": "Recent news coverage highly positive. Brand awareness increasing in target market.",
        "source": "news_sentiment"
    }
]

added = 0
for alert in alerts:
    if alert['company_id']:
        try:
            response = requests.post(f"{API_URL}/api/alerts", json=alert)
            if response.status_code in [200, 201]:
                print(f"[OK] {alert['severity'].upper()}: {alert['title'][:50]}...")
                added += 1
            else:
                print(f"[ERROR] Failed: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] {e}")
    else:
        print(f"[SKIP] Company not found for alert")

print(f"\n{added} alerts added successfully!")
print("\nRefresh your dashboard to see alerts!")

