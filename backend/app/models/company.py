"""
Company database model.
Demonstrates: SQLAlchemy ORM, relationships, data modeling
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.core.database import Base


class Company(Base):
    """Portfolio company model."""
    
    __tablename__ = "companies"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic information
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    website = Column(String(500), nullable=True)
    industry = Column(String(100), nullable=True)
    stage = Column(String(50), nullable=True)  # Seed, Series A, B, C, etc.
    
    # Investment details
    investment_date = Column(DateTime, nullable=True)
    investment_amount = Column(Float, nullable=True)
    ownership_percentage = Column(Float, nullable=True)
    valuation = Column(Float, nullable=True)
    
    # Contact information
    ceo_name = Column(String(255), nullable=True)
    ceo_email = Column(String(255), nullable=True)
    headquarters = Column(String(255), nullable=True)
    
    # Current metrics (updated regularly)
    current_arr = Column(Float, nullable=True)  # Annual Recurring Revenue
    monthly_burn_rate = Column(Float, nullable=True)
    runway_months = Column(Integer, nullable=True)
    employee_count = Column(Integer, nullable=True)
    
    # Risk & health scores (0-100)
    risk_score = Column(Integer, default=50)
    health_score = Column(Integer, default=50)
    
    # Status
    is_active = Column(Boolean, default=True)
    
    # Metadata
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Additional data as JSON
    extra_data = Column(JSON, nullable=True)
    
    # Relationships
    metrics = relationship("Metric", back_populates="company", cascade="all, delete-orphan")
    alerts = relationship("Alert", back_populates="company", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Company(id={self.id}, name='{self.name}', stage='{self.stage}')>"

