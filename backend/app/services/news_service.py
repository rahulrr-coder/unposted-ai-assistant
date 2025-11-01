"""
News Service - NewsAPI integration
"""
import httpx
from typing import List, Optional
from datetime import datetime
from app.config import settings
from app.models.schemas import NewsArticle, NewsResponse, NewsPreferences
import logging

logger = logging.getLogger(__name__)


class NewsService:
    """Service for fetching and filtering news articles."""
    
    def __init__(self):
        self.api_key = settings.NEWS_API_KEY
        self.base_url = settings.NEWS_API_BASE_URL
        
    async def get_top_headlines(
        self,
        preferences: Optional[NewsPreferences] = None,
        page: int = 1,
        page_size: int = 10
    ) -> NewsResponse:
        """
        Fetch top headlines based on user preferences.
        
        Args:
            preferences: User news preferences (categories, sources, etc.)
            page: Page number for pagination
            page_size: Number of articles per page
            
        Returns:
            NewsResponse with articles
        """
        params = {
            "apiKey": self.api_key,
            "page": page,
            "pageSize": page_size,
            "language": "en"
        }
        
        if preferences:
            if preferences.categories:
                params["category"] = preferences.categories[0]  # NewsAPI supports one category
            if preferences.sources:
                params["sources"] = ",".join(preferences.sources[:20])  # Max 20 sources
            if preferences.languages:
                params["language"] = preferences.languages[0]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/top-headlines",
                    params=params,
                    timeout=10.0
                )
                response.raise_for_status()
                data = response.json()
                
                articles = [
                    NewsArticle(
                        title=article["title"],
                        description=article.get("description"),
                        url=article["url"],
                        source=article["source"]["name"],
                        published_at=datetime.fromisoformat(
                            article["publishedAt"].replace("Z", "+00:00")
                        ),
                        image_url=article.get("urlToImage")
                    )
                    for article in data.get("articles", [])
                ]
                
                return NewsResponse(
                    articles=articles,
                    total=data.get("totalResults", len(articles)),
                    page=page,
                    page_size=page_size
                )
                
        except httpx.HTTPError as e:
            logger.error(f"News API error: {e}")
            return NewsResponse(articles=[], total=0, page=page, page_size=page_size)
    
    async def search_news(
        self,
        query: str,
        preferences: Optional[NewsPreferences] = None,
        page: int = 1,
        page_size: int = 10
    ) -> NewsResponse:
        """
        Search for news articles by query.
        
        Args:
            query: Search query
            preferences: User preferences for filtering
            page: Page number
            page_size: Results per page
            
        Returns:
            NewsResponse with matching articles
        """
        params = {
            "apiKey": self.api_key,
            "q": query,
            "page": page,
            "pageSize": page_size,
            "language": "en",
            "sortBy": "relevancy"
        }
        
        if preferences and preferences.languages:
            params["language"] = preferences.languages[0]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/everything",
                    params=params,
                    timeout=10.0
                )
                response.raise_for_status()
                data = response.json()
                
                articles = [
                    NewsArticle(
                        title=article["title"],
                        description=article.get("description"),
                        url=article["url"],
                        source=article["source"]["name"],
                        published_at=datetime.fromisoformat(
                            article["publishedAt"].replace("Z", "+00:00")
                        ),
                        image_url=article.get("urlToImage")
                    )
                    for article in data.get("articles", [])
                ]
                
                return NewsResponse(
                    articles=articles,
                    total=data.get("totalResults", len(articles)),
                    page=page,
                    page_size=page_size
                )
                
        except httpx.HTTPError as e:
            logger.error(f"News search error: {e}")
            return NewsResponse(articles=[], total=0, page=page, page_size=page_size)


# Global service instance
news_service = NewsService()
