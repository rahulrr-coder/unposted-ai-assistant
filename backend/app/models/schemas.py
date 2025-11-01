"""
Pydantic schemas for API requests and responses
"""
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime


# ===== TODO MODELS =====

class TodoBase(BaseModel):
    """Base Todo model with common fields."""
    title: str = Field(min_length=1, max_length=500)
    description: Optional[str] = None
    status: str = Field(default="pending")
    priority: str = Field(default="medium")
    
    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        allowed = ["pending", "in_progress", "completed", "archived"]
        if v not in allowed:
            raise ValueError(f"Status must be one of: {allowed}")
        return v
    
    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: str) -> str:
        allowed = ["low", "medium", "high", "urgent"]
        if v not in allowed:
            raise ValueError(f"Priority must be one of: {allowed}")
        return v


class TodoCreate(TodoBase):
    """Schema for creating a new todo."""
    pass


class TodoUpdate(BaseModel):
    """Schema for updating a todo (all fields optional)."""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    
    @field_validator("status")
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        allowed = ["pending", "in_progress", "completed", "archived"]
        if v not in allowed:
            raise ValueError(f"Status must be one of: {allowed}")
        return v
    
    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        allowed = ["low", "medium", "high", "urgent"]
        if v not in allowed:
            raise ValueError(f"Priority must be one of: {allowed}")
        return v


class TodoResponse(TodoBase):
    """Schema for todo response."""
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# ===== JOURNAL MODELS =====

class Prosody(BaseModel):
    """Acoustic features from speech."""
    mean_pitch_hz: float = Field(ge=0)
    pitch_var: float = Field(ge=0)
    rms_energy: float = Field(ge=0)
    speech_rate_wps: float = Field(ge=0)


class Sentiment(BaseModel):
    """Text sentiment analysis result."""
    valence: float = Field(ge=-1, le=1)
    confidence: float = Field(ge=0, le=1)


class Privacy(BaseModel):
    """Privacy settings."""
    pii_redaction_enabled: bool = False


class JournalInput(BaseModel):
    """Input data for journal processing."""
    transcript: str
    entities: List[str] = Field(default_factory=list)
    prosody: Prosody
    sentiment: Sentiment
    language: str = "en"
    privacy: Privacy = Field(default_factory=Privacy)


class Emotion(BaseModel):
    """2-D emotion estimate."""
    valence: float = Field(ge=-1, le=1)
    arousal: float = Field(ge=-1, le=1)
    label: str


class JournalOutput(BaseModel):
    """Output format for journal reflection."""
    bullets: List[str] = Field(min_length=3, max_length=3)
    emotion: Emotion
    next_prompt: str

    @field_validator("bullets")
    @classmethod
    def validate_bullets(cls, v: List[str]) -> List[str]:
        for bullet in v:
            if len(bullet) > 110:
                raise ValueError(f"Bullet too long: {len(bullet)} chars")
        return v

    @field_validator("next_prompt")
    @classmethod
    def validate_prompt(cls, v: str) -> str:
        if len(v) > 120:
            raise ValueError(f"Prompt too long: {len(v)} chars")
        return v


# ===== USER & AUTH MODELS =====

class UserCreate(BaseModel):
    """User registration schema."""
    email: str
    password: str
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    """User login schema."""
    email: str
    password: str


class UserResponse(BaseModel):
    """User response schema."""
    id: str
    email: str
    full_name: Optional[str] = None
    created_at: datetime


class Token(BaseModel):
    """JWT token response."""
    access_token: str
    token_type: str = "bearer"


# ===== NEWS MODELS =====

class NewsPreferences(BaseModel):
    """User news preferences."""
    categories: List[str] = Field(default_factory=list)
    sources: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default=["en"])
    keywords: List[str] = Field(default_factory=list)


class NewsArticle(BaseModel):
    """News article schema."""
    title: str
    description: Optional[str] = None
    url: str
    source: str
    published_at: datetime
    category: Optional[str] = None
    image_url: Optional[str] = None


class NewsResponse(BaseModel):
    """News feed response."""
    articles: List[NewsArticle]
    total: int
    page: int = 1
    page_size: int = 10


# ===== VOICE MODELS =====

class VoiceRequest(BaseModel):
    """Voice generation request."""
    text: str
    voice: str = "alloy"  # OpenAI voice options: alloy, echo, fable, onyx, nova, shimmer
    speed: float = Field(default=1.0, ge=0.25, le=4.0)


class VoiceResponse(BaseModel):
    """Voice generation response."""
    audio_url: str
    duration: Optional[float] = None


# ===== PREFERENCE MODELS =====

class UserPreferences(BaseModel):
    """Complete user preferences."""
    news_categories: List[str] = Field(default_factory=list)
    news_sources: List[str] = Field(default_factory=list)
    voice_preference: str = "alloy"
    notification_enabled: bool = True
    theme: str = "light"
    language: str = "en"


class PreferenceUpdate(BaseModel):
    """Partial preference update."""
    news_categories: Optional[List[str]] = None
    news_sources: Optional[List[str]] = None
    voice_preference: Optional[str] = None
    notification_enabled: Optional[bool] = None
    theme: Optional[str] = None
    language: Optional[str] = None


# ===== GENERIC RESPONSES =====

class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    timestamp: datetime


class ErrorResponse(BaseModel):
    """Error response schema."""
    error: str
    detail: Optional[str] = None
    timestamp: datetime
