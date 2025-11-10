"""
Configuration management for InvestorLens AI platform.
Demonstrates: DevOps best practices, environment management
"""

from functools import lru_cache
from typing import List, Union
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, field_validator
import json
import os


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application
    APP_NAME: str = "InvestorLens AI"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/investorlens"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Security
    SECRET_KEY: str = "default-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    @field_validator('CORS_ORIGINS', mode='before')
    @classmethod
    def parse_cors_origins(cls, v) -> List[str]:
        """Parse CORS_ORIGINS from JSON string or return list."""
        print(f"🔍 RAW CORS_ORIGINS from env: {v}")
        print(f"🔍 Type: {type(v)}")
        
        # If already a list, return it
        if isinstance(v, list):
            print(f"✅ Already a list with {len(v)} origins")
            return v
        
        # If string, try to parse as JSON
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
                print(f"✅ Parsed JSON successfully: {parsed}")
                return parsed
            except json.JSONDecodeError as e:
                print(f"❌ JSON parse failed: {e}")
                # Fallback: split by comma
                result = [origin.strip() for origin in v.split(',')]
                print(f"⚠️ Using comma-split fallback: {result}")
                return result
        
        print(f"⚠️ Unexpected type, returning as-is")
        return v
    
    # AI/LLM Keys
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    
    # External APIs
    NEWS_API_KEY: str = ""
    LINKEDIN_API_KEY: str = ""
    SIMILARWEB_API_KEY: str = ""
    
    # AWS
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    S3_BUCKET_NAME: str = "investorlens-reports"
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Global settings instance
settings = get_settings()

