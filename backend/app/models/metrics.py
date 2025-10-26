"""
Metrics database model for tracking company performance over time.
Demonstrates: Time-series data modeling, foreign keys
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Metric(Base):
    """Time-series metrics for portfolio companies."""
    
    __tablename__ = "metrics"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to company
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    
    # Metric details
    metric_type = Column(String(100), nullable=False, index=True)
    # Types: revenue, burn_rate, runway, employee_count, web_traffic, 
    #        social_mentions, news_sentiment, etc.
    
    metric_name = Column(String(255), nullable=False)
    metric_value = Column(Float, nullable=False)
    metric_unit = Column(String(50), nullable=True)  # USD, months, count, percentage, etc.
    
    # Time period
    period_start = Column(DateTime, nullable=True)
    period_end = Column(DateTime, nullable=True)
    recorded_at = Column(DateTime, server_default=func.now(), index=True)
    
    # Source information
    source = Column(String(100), nullable=True)  # manual, api, scraper, etc.
    source_url = Column(Text, nullable=True)
    
    # Additional context
    notes = Column(Text, nullable=True)
    
    # Relationships
    company = relationship("Company", back_populates="metrics")
    
    def __repr__(self):
        return f"<Metric(company_id={self.company_id}, type='{self.metric_type}', value={self.metric_value})>"

