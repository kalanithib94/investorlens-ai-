"""
LLM-powered analysis service using OpenAI GPT-4 and Anthropic Claude.
Demonstrates: AI/LLM integration, prompt engineering, async processing
"""

from typing import Dict, List, Optional
import asyncio
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic

from app.core.config import settings


class LLMAnalyzer:
    """
    AI-powered analyzer using Large Language Models.
    Supports multiple LLM providers for different use cases.
    """
    
    def __init__(self):
        """Initialize LLM clients."""
        self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None
        self.anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY) if settings.ANTHROPIC_API_KEY else None
    
    async def generate_executive_summary(
        self, 
        company_data: Dict, 
        metrics: List[Dict], 
        news: List[Dict]
    ) -> Dict[str, str]:
        """
        Generate AI-powered executive summary for a company.
        
        Args:
            company_data: Company information
            metrics: Recent metrics data
            news: Recent news articles
            
        Returns:
            Dictionary with summary and key insights
        """
        if not self.openai_client:
            return self._generate_mock_summary(company_data)
        
        # Build context from data
        context = self._build_context(company_data, metrics, news)
        
        # Create prompt for GPT-4
        prompt = f"""You are an expert venture capital analyst. Analyze the following portfolio company data and provide a concise executive summary.

Company: {company_data.get('name')}
Industry: {company_data.get('industry')}
Stage: {company_data.get('stage')}

Recent Metrics:
{self._format_metrics(metrics)}

Recent News:
{self._format_news(news)}

Provide:
1. A 2-3 sentence executive summary
2. Key performance highlights (3-4 bullet points)
3. Areas of concern (if any)
4. Strategic recommendations (2-3 points)

Be specific, data-driven, and actionable."""

        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert venture capital analyst specializing in portfolio company analysis."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,  # Lower temperature for more consistent analysis
                max_tokens=800
            )
            
            summary_text = response.choices[0].message.content
            
            return {
                "summary": summary_text,
                "model_used": "gpt-4",
                "confidence": "high"
            }
            
        except Exception as e:
            print(f"Error generating summary: {e}")
            return self._generate_mock_summary(company_data)
    
    async def assess_risk_score(
        self, 
        company_data: Dict, 
        metrics: List[Dict], 
        alerts: List[Dict]
    ) -> Dict:
        """
        Calculate AI-powered risk score (0-100, where 100 is highest risk).
        
        Uses Claude for complex reasoning about risk factors.
        
        Args:
            company_data: Company information
            metrics: Recent metrics
            alerts: Existing alerts
            
        Returns:
            Dictionary with risk score, factors, and explanation
        """
        if not self.anthropic_client:
            return self._generate_mock_risk_score(company_data)
        
        prompt = f"""Analyze this portfolio company's risk profile and provide a risk score from 0-100 (100 = highest risk).

Company: {company_data.get('name')}
Industry: {company_data.get('industry')}
Current Runway: {company_data.get('runway_months', 'Unknown')} months
Burn Rate: ${company_data.get('monthly_burn_rate', 0):,.0f}/month
ARR: ${company_data.get('current_arr', 0):,.0f}

Recent Metrics Trends:
{self._format_metrics(metrics)}

Active Alerts: {len(alerts)}

Provide:
1. Overall Risk Score (0-100)
2. Key Risk Factors (3-5 items)
3. Risk Mitigation Recommendations
4. Confidence Level (high/medium/low)

Format your response as:
RISK_SCORE: [number]
FACTORS: [list of factors]
RECOMMENDATIONS: [recommendations]
CONFIDENCE: [level]"""

        try:
            response = await self.anthropic_client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            content = response.content[0].text
            risk_score = self._parse_risk_score(content)
            
            return {
                "risk_score": risk_score,
                "analysis": content,
                "model_used": "claude-3-sonnet",
                "timestamp": "2024-01-15T10:00:00Z"
            }
            
        except Exception as e:
            print(f"Error assessing risk: {e}")
            return self._generate_mock_risk_score(company_data)
    
    async def analyze_competitive_landscape(
        self, 
        company_data: Dict, 
        competitor_news: List[Dict]
    ) -> Dict:
        """
        Analyze competitive landscape and identify opportunities/threats.
        
        Args:
            company_data: Company information
            competitor_news: News about competitors
            
        Returns:
            Competitive analysis insights
        """
        if not self.openai_client:
            return {
                "opportunities": ["Market expansion potential", "Product differentiation"],
                "threats": ["Increased competition", "Market saturation"],
                "strategic_actions": ["Focus on customer retention", "Accelerate product development"]
            }
        
        prompt = f"""Analyze the competitive landscape for this portfolio company:

Company: {company_data.get('name')}
Industry: {company_data.get('industry')}

Competitor Activity:
{self._format_news(competitor_news)}

Identify:
1. Key Opportunities (3 items)
2. Potential Threats (3 items)
3. Strategic Actions to Consider (3-4 items)"""

        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a strategic business analyst specializing in competitive intelligence."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=600
            )
            
            return {
                "analysis": response.choices[0].message.content,
                "model_used": "gpt-4"
            }
            
        except Exception as e:
            print(f"Error in competitive analysis: {e}")
            return {"analysis": "Competitive analysis unavailable", "model_used": "fallback"}
    
    # Helper methods
    
    def _build_context(self, company_data: Dict, metrics: List[Dict], news: List[Dict]) -> str:
        """Build context string from data."""
        return f"Company: {company_data.get('name')}\nMetrics: {len(metrics)} data points\nNews: {len(news)} articles"
    
    def _format_metrics(self, metrics: List[Dict]) -> str:
        """Format metrics for LLM prompt."""
        if not metrics:
            return "No recent metrics available"
        
        formatted = []
        for metric in metrics[:5]:  # Last 5 metrics
            formatted.append(
                f"- {metric.get('metric_name')}: {metric.get('metric_value')} {metric.get('metric_unit', '')}"
            )
        return "\n".join(formatted)
    
    def _format_news(self, news: List[Dict]) -> str:
        """Format news for LLM prompt."""
        if not news:
            return "No recent news available"
        
        formatted = []
        for article in news[:3]:  # Last 3 articles
            formatted.append(f"- {article.get('title')} ({article.get('date', 'Recent')})")
        return "\n".join(formatted)
    
    def _parse_risk_score(self, content: str) -> int:
        """Parse risk score from LLM response."""
        # Simple parsing - look for RISK_SCORE: [number]
        import re
        match = re.search(r'RISK_SCORE:\s*(\d+)', content)
        if match:
            return int(match.group(1))
        return 50  # Default moderate risk
    
    def _generate_mock_summary(self, company_data: Dict) -> Dict:
        """Generate mock summary when API key is not available."""
        return {
            "summary": f"{company_data.get('name')} is performing within expected parameters. The company shows steady growth with manageable burn rate. Continue monitoring key metrics.",
            "model_used": "mock",
            "confidence": "medium"
        }
    
    def _generate_mock_risk_score(self, company_data: Dict) -> Dict:
        """Generate mock risk score when API key is not available."""
        runway = company_data.get('runway_months', 12)
        
        # Simple risk calculation based on runway
        if runway >= 18:
            risk_score = 20  # Low risk
        elif runway >= 12:
            risk_score = 40  # Medium-low risk
        elif runway >= 6:
            risk_score = 65  # Medium-high risk
        else:
            risk_score = 85  # High risk
        
        return {
            "risk_score": risk_score,
            "analysis": f"Risk assessment based on {runway} months runway. Company has {'adequate' if runway >= 12 else 'concerning'} cash position.",
            "model_used": "fallback",
            "timestamp": "2024-01-15T10:00:00Z"
        }


# Global instance
llm_analyzer = LLMAnalyzer()

