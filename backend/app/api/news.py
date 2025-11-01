"""
News API endpoints
"""
from fastapi import APIRouter, Depends, Query
from typing import Optional
from app.models.schemas import NewsResponse, NewsPreferences
from app.services.news_service import news_service
from app.services.personalization import personalization_service
from app.api.auth import get_current_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/news", tags=["News"])


@router.get("/", response_model=NewsResponse)
async def get_news(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    """
    Get personalized news feed based on user preferences.
    
    Args:
        page: Page number
        page_size: Articles per page
        category: Optional category filter
        current_user: Authenticated user
        
    Returns:
        NewsResponse with articles
    """
    # Get user preferences
    user_prefs = personalization_service.get_user_preferences(current_user["id"])
    
    # Build news preferences
    news_prefs = NewsPreferences(
        categories=[category] if category else user_prefs.news_categories,
        sources=user_prefs.news_sources,
        languages=[user_prefs.language]
    )
    
    # Fetch news
    return await news_service.get_top_headlines(
        preferences=news_prefs,
        page=page,
        page_size=page_size
    )


@router.get("/search", response_model=NewsResponse)
async def search_news(
    q: str = Query(..., min_length=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    current_user: dict = Depends(get_current_user)
):
    """
    Search for news articles.
    
    Args:
        q: Search query
        page: Page number
        page_size: Articles per page
        current_user: Authenticated user
        
    Returns:
        NewsResponse with matching articles
    """
    user_prefs = personalization_service.get_user_preferences(current_user["id"])
    
    news_prefs = NewsPreferences(
        languages=[user_prefs.language]
    )
    
    return await news_service.search_news(
        query=q,
        preferences=news_prefs,
        page=page,
        page_size=page_size
    )


@router.get("/recommendations", response_model=NewsResponse)
async def get_recommendations(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    current_user: dict = Depends(get_current_user)
):
    """
    Get AI-recommended news based on user history.
    
    Args:
        page: Page number
        page_size: Articles per page
        current_user: Authenticated user
        
    Returns:
        NewsResponse with recommended articles
    """
    # Get personalized recommendations
    recommendations = personalization_service.get_news_recommendations(
        user_id=current_user["id"]
    )
    
    return await news_service.get_top_headlines(
        preferences=recommendations,
        page=page,
        page_size=page_size
    )
