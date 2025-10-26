"""
Alert database model for notifications and warnings.
Demonstrates: Enum types, status tracking
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base


class AlertSeverity(str, enum.Enum):
    """Alert severity levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AlertType(str, enum.Enum):
    """Types of alerts."""
    RISK = "risk"
    OPPORTUNITY = "opportunity"
    ANOMALY = "anomaly"
    NEWS = "news"
    FINANCIAL = "financial"
    COMPLIANCE = "compliance"


class Alert(Base):
    """Alert/notification model."""
    
    __tablename__ = "alerts"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key to company
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    
    # Alert details
    alert_type = Column(Enum(AlertType), nullable=False, index=True)
    severity = Column(Enum(AlertSeverity), nullable=False, index=True)
    
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    
    # AI-generated insights
    ai_summary = Column(Text, nullable=True)
    recommended_actions = Column(Text, nullable=True)
    
    # Status
    is_read = Column(Boolean, default=False)
    is_resolved = Column(Boolean, default=False)
    resolved_at = Column(DateTime, nullable=True)
    resolved_by = Column(String(255), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    company = relationship("Company", back_populates="alerts")
    
    def __repr__(self):
        return f"<Alert(id={self.id}, type='{self.alert_type}', severity='{self.severity}')>"

