"""API routers."""

from fastapi import APIRouter
from app.api import companies, analysis, alerts

# Create main API router
api_router = APIRouter()

# Include all sub-routers
api_router.include_router(companies.router)
api_router.include_router(analysis.router)
api_router.include_router(alerts.router)

__all__ = ["api_router"]

