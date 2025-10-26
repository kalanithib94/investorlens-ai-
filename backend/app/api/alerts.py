"""
Alert management API endpoints.
Demonstrates: Notification system, filtering, status management
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from pydantic import BaseModel
from datetime import datetime

from app.core.database import get_db
from app.models import Alert, AlertType, AlertSeverity, Company


router = APIRouter(prefix="/api/alerts", tags=["Alerts"])


# Response schemas
class AlertResponse(BaseModel):
    """Alert response schema."""
    id: int
    company_id: int
    company_name: Optional[str]
    alert_type: AlertType
    severity: AlertSeverity
    title: str
    description: str
    ai_summary: Optional[str]
    is_read: bool
    is_resolved: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


@router.get("", response_model=List[AlertResponse])
async def get_alerts(
    severity: Optional[AlertSeverity] = None,
    alert_type: Optional[AlertType] = None,
    company_id: Optional[int] = None,
    unread_only: bool = False,
    unresolved_only: bool = True,
    limit: int = Query(50, le=200),
    db: Session = Depends(get_db)
):
    """
    Retrieve alerts with advanced filtering.
    
    Query Parameters:
    - severity: Filter by severity (low, medium, high, critical)
    - alert_type: Filter by type (risk, opportunity, anomaly, news, financial)
    - company_id: Filter by specific company
    - unread_only: Show only unread alerts
    - unresolved_only: Show only unresolved alerts (default: true)
    - limit: Maximum number of alerts to return
    """
    query = db.query(Alert).join(Company)
    
    # Apply filters
    if severity:
        query = query.filter(Alert.severity == severity)
    if alert_type:
        query = query.filter(Alert.alert_type == alert_type)
    if company_id:
        query = query.filter(Alert.company_id == company_id)
    if unread_only:
        query = query.filter(Alert.is_read == False)
    if unresolved_only:
        query = query.filter(Alert.is_resolved == False)
    
    # Order by created date (newest first)
    query = query.order_by(desc(Alert.created_at))
    
    # Limit results
    alerts = query.limit(limit).all()
    
    # Add company name to response
    result = []
    for alert in alerts:
        alert_dict = {
            "id": alert.id,
            "company_id": alert.company_id,
            "company_name": alert.company.name,
            "alert_type": alert.alert_type,
            "severity": alert.severity,
            "title": alert.title,
            "description": alert.description,
            "ai_summary": alert.ai_summary,
            "is_read": alert.is_read,
            "is_resolved": alert.is_resolved,
            "created_at": alert.created_at
        }
        result.append(AlertResponse(**alert_dict))
    
    return result


@router.get("/{alert_id}", response_model=AlertResponse)
async def get_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific alert."""
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    alert_dict = {
        "id": alert.id,
        "company_id": alert.company_id,
        "company_name": alert.company.name,
        "alert_type": alert.alert_type,
        "severity": alert.severity,
        "title": alert.title,
        "description": alert.description,
        "ai_summary": alert.ai_summary,
        "is_read": alert.is_read,
        "is_resolved": alert.is_resolved,
        "created_at": alert.created_at
    }
    
    return AlertResponse(**alert_dict)


@router.patch("/{alert_id}/read")
async def mark_alert_read(
    alert_id: int,
    db: Session = Depends(get_db)
):
    """Mark an alert as read."""
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    alert.is_read = True
    db.commit()
    
    return {"message": "Alert marked as read", "alert_id": alert_id}


@router.patch("/{alert_id}/resolve")
async def resolve_alert(
    alert_id: int,
    resolved_by: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Resolve an alert."""
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    alert.is_resolved = True
    alert.resolved_at = datetime.utcnow()
    alert.resolved_by = resolved_by
    db.commit()
    
    return {"message": "Alert resolved", "alert_id": alert_id}


@router.get("/stats/summary")
async def get_alert_stats(
    db: Session = Depends(get_db)
):
    """
    Get summary statistics about alerts.
    
    Returns counts by severity and type.
    """
    total_alerts = db.query(Alert).filter(Alert.is_resolved == False).count()
    
    critical = db.query(Alert).filter(
        Alert.severity == AlertSeverity.CRITICAL,
        Alert.is_resolved == False
    ).count()
    
    high = db.query(Alert).filter(
        Alert.severity == AlertSeverity.HIGH,
        Alert.is_resolved == False
    ).count()
    
    unread = db.query(Alert).filter(Alert.is_read == False).count()
    
    return {
        "total_unresolved": total_alerts,
        "critical": critical,
        "high": high,
        "unread": unread,
        "by_severity": {
            "critical": critical,
            "high": high,
            "medium": db.query(Alert).filter(
                Alert.severity == AlertSeverity.MEDIUM,
                Alert.is_resolved == False
            ).count(),
            "low": db.query(Alert).filter(
                Alert.severity == AlertSeverity.LOW,
                Alert.is_resolved == False
            ).count()
        }
    }

