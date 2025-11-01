"""
Configuration management using Pydantic settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # App
    APP_NAME: str = "Unposted AI Assistant"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Supabase
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_SERVICE_KEY: Optional[str] = None
    
    # News API
    NEWS_API_KEY: str
    NEWS_API_BASE_URL: str = "https://newsapi.org/v2"
    
    # Claude/Anthropic
    ANTHROPIC_API_KEY: str
    CLAUDE_MODEL: str = "claude-3-5-sonnet-20241022"
    CLAUDE_MAX_TOKENS: int = 1024
    
    # OpenAI (for voice)
    OPENAI_API_KEY: str
    OPENAI_TTS_MODEL: str = "tts-1"
    OPENAI_VOICE_DEFAULT: str = "alloy"
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8501"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
