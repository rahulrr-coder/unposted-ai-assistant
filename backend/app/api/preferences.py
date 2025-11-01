"""
User Preferences API endpoints
"""
from fastapi import APIRouter, Depends, status
from app.models.schemas import UserPreferences, PreferenceUpdate
from app.services.personalization import personalization_service
from app.api.auth import get_current_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/preferences", tags=["Preferences"])


@router.get("/", response_model=UserPreferences)
async def get_preferences(current_user: dict = Depends(get_current_user)):
    """
    Get user preferences.
    
    Args:
        current_user: Authenticated user
        
    Returns:
        UserPreferences
    """
    return personalization_service.get_user_preferences(current_user["id"])


@router.put("/", response_model=UserPreferences)
async def update_preferences(
    preferences: PreferenceUpdate,
    current_user: dict = Depends(get_current_user)
):
    """
    Update user preferences.
    
    Args:
        preferences: Preference updates
        current_user: Authenticated user
        
    Returns:
        Updated UserPreferences
    """
    # Get current preferences
    current_prefs = personalization_service.get_user_preferences(current_user["id"])
    
    # Update only provided fields
    update_data = preferences.model_dump(exclude_unset=True)
    updated_prefs = current_prefs.model_copy(update=update_data)
    
    # Save updated preferences
    return personalization_service.update_user_preferences(
        user_id=current_user["id"],
        preferences=updated_prefs
    )


@router.post("/track-interaction", status_code=status.HTTP_204_NO_CONTENT)
async def track_interaction(
    article_id: str,
    interaction_type: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Track user interaction with an article for personalization.
    
    Args:
        article_id: Article identifier
        interaction_type: Type of interaction (view, like, share)
        current_user: Authenticated user
    """
    personalization_service.track_interaction(
        user_id=current_user["id"],
        article_id=article_id,
        interaction_type=interaction_type
    )
