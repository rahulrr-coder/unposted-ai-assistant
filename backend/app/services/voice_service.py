"""
Voice Service - OpenAI TTS integration
"""
from typing import List
from openai import OpenAI
from app.config import settings
from app.models.schemas import VoiceRequest, VoiceResponse
import logging
import base64
from pathlib import Path
import tempfile

logger = logging.getLogger(__name__)


class VoiceService:
    """Service for text-to-speech using OpenAI."""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_TTS_MODEL
    
    async def generate_speech(self, request: VoiceRequest) -> VoiceResponse:
        """
        Generate speech audio from text.
        
        Args:
            request: VoiceRequest with text and voice settings
            
        Returns:
            VoiceResponse with audio URL or base64 data
        """
        try:
            response = self.client.audio.speech.create(
                model=self.model,
                voice=request.voice,
                input=request.text,
                speed=request.speed
            )
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                response.stream_to_file(temp_file.name)
                audio_path = temp_file.name
            
            # Read and encode as base64 for now (in production, upload to storage)
            with open(audio_path, "rb") as audio_file:
                audio_data = audio_file.read()
                audio_base64 = base64.b64encode(audio_data).decode()
            
            # Clean up temp file
            Path(audio_path).unlink()
            
            return VoiceResponse(
                audio_url=f"data:audio/mpeg;base64,{audio_base64}",
                duration=None  # Could calculate if needed
            )
            
        except Exception as e:
            logger.error(f"Voice generation error: {e}")
            raise
    
    def get_available_voices(self) -> List[str]:
        """Get list of available voice options."""
        return ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]


# Global service instance
voice_service = VoiceService()
