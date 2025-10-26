"""
News scraping and aggregation service.
Demonstrates: External API integration, data aggregation, async processing
"""

from typing import List, Dict, Optional
import asyncio
from datetime import datetime, timedelta
import httpx

from app.core.config import settings


class NewsAggregator:
    """
    Aggregate news from multiple sources.
    Integrates with Google News API, NewsAPI, etc.
    """
    
    def __init__(self):
        """Initialize news aggregator."""
        self.news_api_key = settings.NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2"
    
    async def fetch_company_news(
        self, 
        company_name: str, 
        days_back: int = 7
    ) -> List[Dict]:
        """
        Fetch recent news about a company.
        
        Args:
            company_name: Name of the company to search for
            days_back: Number of days to look back
            
        Returns:
            List of news articles
        """
        if not self.news_api_key:
            return self._generate_mock_news(company_name)
        
        from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        
        params = {
            'q': company_name,
            'from': from_date,
            'sortBy': 'relevancy',
            'apiKey': self.news_api_key,
            'language': 'en'
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/everything",
                    params=params,
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    articles = data.get('articles', [])
                    
                    return [
                        {
                            'title': article.get('title'),
                            'description': article.get('description'),
                            'url': article.get('url'),
                            'source': article.get('source', {}).get('name'),
                            'published_at': article.get('publishedAt'),
                            'sentiment': self._analyze_sentiment(article.get('title', '') + ' ' + article.get('description', ''))
                        }
                        for article in articles[:10]  # Limit to 10 articles
                    ]
                else:
                    print(f"News API error: {response.status_code}")
                    return self._generate_mock_news(company_name)
                    
        except Exception as e:
            print(f"Error fetching news: {e}")
            return self._generate_mock_news(company_name)
    
    async def fetch_industry_news(self, industry: str, limit: int = 5) -> List[Dict]:
        """
        Fetch news about an industry.
        
        Args:
            industry: Industry name/keyword
            limit: Number of articles to return
            
        Returns:
            List of news articles
        """
        if not self.news_api_key:
            return self._generate_mock_news(industry)
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/everything",
                    params={
                        'q': industry,
                        'sortBy': 'publishedAt',
                        'apiKey': self.news_api_key,
                        'pageSize': limit
                    },
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    articles = data.get('articles', [])
                    
                    return [
                        {
                            'title': article.get('title'),
                            'url': article.get('url'),
                            'published_at': article.get('publishedAt')
                        }
                        for article in articles
                    ]
                    
        except Exception as e:
            print(f"Error fetching industry news: {e}")
            
        return []
    
    def _analyze_sentiment(self, text: str) -> str:
        """
        Basic sentiment analysis.
        In production, would use NLP library or API.
        """
        positive_words = ['growth', 'success', 'profit', 'innovation', 'award', 'funding', 'expansion']
        negative_words = ['loss', 'decline', 'lawsuit', 'scandal', 'layoff', 'bankruptcy', 'failure']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def _generate_mock_news(self, query: str) -> List[Dict]:
        """Generate mock news data for demo purposes."""
        return [
            {
                'title': f'{query} announces new product launch',
                'description': 'Company reveals innovative solution to market challenges.',
                'url': f'https://example.com/news/{query.lower().replace(" ", "-")}-1',
                'source': 'TechCrunch',
                'published_at': datetime.now().isoformat(),
                'sentiment': 'positive'
            },
            {
                'title': f'{query} raises Series B funding',
                'description': 'Investment round values company at $100M+.',
                'url': f'https://example.com/news/{query.lower().replace(" ", "-")}-2',
                'source': 'Business Insider',
                'published_at': (datetime.now() - timedelta(days=2)).isoformat(),
                'sentiment': 'positive'
            },
            {
                'title': f'Industry analysis: {query} competitive position',
                'description': 'Analysts weigh in on market positioning.',
                'url': f'https://example.com/news/{query.lower().replace(" ", "-")}-3',
                'source': 'Forbes',
                'published_at': (datetime.now() - timedelta(days=5)).isoformat(),
                'sentiment': 'neutral'
            }
        ]


# Global instance
news_aggregator = NewsAggregator()

