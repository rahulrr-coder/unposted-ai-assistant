"""
Voice API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from app.models.schemas import VoiceRequest, VoiceResponse, JournalInput, JournalOutput
from app.services.voice_service import voice_service
from app.services.ai_service import ai_service
from app.api.auth import get_current_user
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/voice", tags=["Voice"])


@router.post("/generate", response_model=VoiceResponse)
async def generate_voice(
    request: VoiceRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Generate speech from text.
    
    Args:
        request: VoiceRequest with text and voice settings
        current_user: Authenticated user
        
    Returns:
        VoiceResponse with audio URL
    """
    try:
        return await voice_service.generate_speech(request)
    except Exception as e:
        logger.error(f"Voice generation failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Voice generation failed"
        )


@router.get("/voices")
async def get_voices(current_user: dict = Depends(get_current_user)):
    """
    Get available voice options.
    
    Args:
        current_user: Authenticated user
        
    Returns:
        List of available voices
    """
    return {"voices": voice_service.get_available_voices()}


@router.post("/journal", response_model=JournalOutput)
async def process_journal(
    journal_input: JournalInput,
    current_user: dict = Depends(get_current_user)
):
    """
    Process a voice journal entry with AI analysis.
    
    Args:
        journal_input: Journal transcript with prosody and sentiment
        current_user: Authenticated user
        
    Returns:
        JournalOutput with bullets, emotion, and next prompt
    """
    try:
        result = ai_service.process_journal(journal_input)
        
        # TODO: Save journal entry to database
        logger.info(f"Processed journal for user {current_user['id']}")
        
        return result
    except Exception as e:
        logger.error(f"Journal processing failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Journal processing failed"
        )
