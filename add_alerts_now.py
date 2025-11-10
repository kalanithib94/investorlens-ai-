"""Add realistic alerts to demonstrate the AI monitoring system"""
import requests

API_URL = "https://investorlens-ai-production.up.railway.app"

# Get companies first
companies_response = requests.get(f"{API_URL}/api/companies")
companies = companies_response.json()

# Create a map of company names to IDs
company_map = {c['name']: c['id'] for c in companies}

# Realistic alerts based on actual company data
alerts = [
    {
        "company_id": company_map.get("RetailVision360"),
        "alert_type": "risk",
        "severity": "critical",
        "title": "Critical: Runway Below 6 Months",
        "description": "AI detected only 5 months runway. Immediate action: explore bridge funding or reduce burn 30%. Competitive analysis shows similar companies securing emergency rounds.",
        "source": "ai_risk_analyzer"
    },
    {
        "company_id": company_map.get("PayFlow Secure"),
        "alert_type": "financial",
        "severity": "high",
        "title": "High Burn Rate Alert",
        "description": "Burn multiple analysis: $95K monthly with $980K ARR = 11.6x burn rate. Industry benchmark: 6-8x. AI recommends immediate cost optimization.",
        "source": "ai_financial_monitor"
    },
    {
        "company_id": company_map.get("RetailVision360"),
        "alert_type": "anomaly",
        "severity": "high",
        "title": "Customer Churn Spike Detected",
        "description": "AI sentiment analysis of customer feedback shows 22% increase in negative sentiment. 2 major clients at risk based on usage patterns.",
        "source": "ai_market_analyzer"
    },
    {
        "company_id": company_map.get("Velocity Cloud Inc"),
        "alert_type": "risk",
        "severity": "medium",
        "title": "Runway Approaching Threshold",
        "description": "14-month runway detected. AI suggests fundraising timeline: start process in 6 months for 12-month Series B round.",
        "source": "ai_risk_analyzer"
    },
    {
        "company_id": company_map.get("LearnHub Platform"),
        "alert_type": "news",
        "severity": "medium",
        "title": "Competitor Raised $50M Series B",
        "description": "AI news scraping detected major competitor funding. Market consolidation likely. Recommend accelerating product roadmap.",
        "source": "ai_news_monitor"
    },
    {
        "company_id": company_map.get("HealthBridge Pro"),
        "alert_type": "opportunity",
        "severity": "low",
        "title": "Expansion Opportunity Identified",
        "description": "AI market analysis: Strong metrics ($6.5M ARR, 24mo runway) + 3 strategic partnership opportunities in EU market detected.",
        "source": "ai_growth_analyzer"
    }
]

print("Adding alerts...")
added = 0
for alert in alerts:
    if alert['company_id']:
        try:
            response = requests.post(f"{API_URL}/api/alerts", json=alert)
            if response.status_code in [200, 201]:
                print(f"[OK] {alert['severity'].upper()}: {alert['title'][:50]}...")
                added += 1
            else:
                print(f"[ERROR] {response.status_code}: {response.text[:100]}")
        except Exception as e:
            print(f"[ERROR] {e}")

print(f"\nAdded {added} alerts!")
print("Refresh dashboard to see them.")
