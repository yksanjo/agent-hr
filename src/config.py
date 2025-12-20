"""Configuration management for AgentHR."""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # API Keys
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    
    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://localhost/agenthr")
    
    # Redis
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Message Queue
    celery_broker_url: str = os.getenv("CELERY_BROKER_URL", "amqp://localhost:5672//")
    celery_result_backend: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    
    # API Settings
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    api_debug: bool = os.getenv("API_DEBUG", "false").lower() == "true"
    
    # Transaction Pricing
    pricing_hiring: float = float(os.getenv("PRICING_HIRING", "50.0"))
    pricing_payroll: float = float(os.getenv("PRICING_PAYROLL", "2.0"))
    pricing_benefits_enrollment: float = float(os.getenv("PRICING_BENEFITS_ENROLLMENT", "1.0"))
    pricing_performance_review: float = float(os.getenv("PRICING_PERFORMANCE_REVIEW", "10.0"))
    pricing_offboarding: float = float(os.getenv("PRICING_OFFBOARDING", "25.0"))
    
    # AI Model Settings
    default_llm_provider: str = os.getenv("DEFAULT_LLM_PROVIDER", "openai")
    default_model: str = os.getenv("DEFAULT_MODEL", "gpt-4-turbo-preview")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

