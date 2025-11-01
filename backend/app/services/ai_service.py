"""
AI Service - Claude integration for journaling assistance
"""
import re
from typing import List, Dict, Any
from app.models.schemas import JournalInput, JournalOutput, Emotion, Prosody, Sentiment
import logging

logger = logging.getLogger(__name__)


class AIService:
    """
    AI service for processing journal entries using Claude.
    Provides emotional analysis and personalized reflections.
    """

    EMOTION_LABELS = {
        "calm_content": "calm content",
        "calm_sad": "calm sad",
        "tense_worried": "tense worried",
        "tense_angry": "tense angry",
        "energized_hopeful": "energized hopeful",
        "energized_anxious": "energized anxious",
        "neutral": "neutral"
    }

    PII_PATTERNS = [
        (r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '[PHONE]'),
        (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]'),
        (r'\b\d{1,5}\s+\w+\s+(street|st|avenue|ave|road|rd|lane|ln|drive|dr|court|ct|boulevard|blvd)\b', '[ADDRESS]', re.IGNORECASE)
    ]

    def process_journal(self, input_data: JournalInput) -> JournalOutput:
        """
        Process journal input and return structured output.
        
        Args:
            input_data: JournalInput schema with transcript and metadata
            
        Returns:
            JournalOutput with bullets, emotion, and next_prompt
        """
        # Redact PII if enabled
        transcript = self._redact_pii(
            input_data.transcript,
            input_data.privacy.pii_redaction_enabled
        )
        
        # Calculate emotion
        emotion = self._calculate_emotion(
            input_data.sentiment,
            input_data.prosody,
            transcript
        )
        
        # Generate reflection bullets
        bullets = self._generate_bullets(transcript, input_data.entities)
        
        # Generate follow-up prompt
        next_prompt = self._generate_prompt(transcript, emotion)
        
        return JournalOutput(
            bullets=bullets,
            emotion=emotion,
            next_prompt=next_prompt
        )

    def _redact_pii(self, text: str, enabled: bool) -> str:
        """Redact personally identifiable information if enabled."""
        if not enabled:
            return text
        
        result = text
        for pattern, replacement, *flags in self.PII_PATTERNS:
            flag = flags[0] if flags else 0
            result = re.sub(pattern, replacement, result, flags=flag)
        return result

    def _calculate_emotion(self, sentiment: Sentiment, prosody: Prosody, transcript: str) -> Emotion:
        """Calculate 2-D emotion from sentiment and prosody."""
        token_count = len(transcript.split())
        
        # Low confidence or short transcript → neutral
        if sentiment.confidence < 0.5 or token_count < 20:
            return Emotion(valence=0.0, arousal=0.0, label=self.EMOTION_LABELS["neutral"])
        
        # Valence from sentiment
        valence = sentiment.valence
        
        # Arousal from prosody
        arousal_energy = min(prosody.rms_energy / 0.1, 1.0)
        arousal_pitch = min(prosody.pitch_var / 1000, 1.0)
        arousal_rate = min(prosody.speech_rate_wps / 3.0, 1.0)
        
        arousal = (arousal_energy + arousal_pitch + arousal_rate) / 3.0
        arousal = (arousal * 2) - 1  # Scale to [-1, 1]
        
        label = self._get_emotion_label(valence, arousal)
        
        return Emotion(valence=round(valence, 2), arousal=round(arousal, 2), label=label)

    def _get_emotion_label(self, valence: float, arousal: float) -> str:
        """Map valence and arousal to emotion label."""
        if abs(valence) < 0.2 and abs(arousal) < 0.2:
            return self.EMOTION_LABELS["neutral"]
        
        if arousal > 0.3:
            if valence > 0.3:
                return self.EMOTION_LABELS["energized_hopeful"]
            elif valence < -0.3:
                return self.EMOTION_LABELS["tense_angry"]
            else:
                return self.EMOTION_LABELS["energized_anxious"]
        else:
            if valence > 0.3:
                return self.EMOTION_LABELS["calm_content"]
            elif valence < -0.3:
                return self.EMOTION_LABELS["calm_sad"]
            else:
                return self.EMOTION_LABELS["neutral"]

    def _generate_bullets(self, transcript: str, entities: List[str]) -> List[str]:
        """Generate three concise reflection bullets."""
        sentences = [s.strip() for s in re.split(r'[.!?]+', transcript) if s.strip()]
        bullets = []
        
        if len(sentences) >= 3:
            bullets.append(self._make_bullet(sentences[0], entities))
            bullets.append(self._make_bullet(sentences[len(sentences)//2], entities))
            bullets.append(self._make_bullet(sentences[-1], entities))
        elif len(sentences) == 2:
            bullets.append(self._make_bullet(sentences[0], entities))
            bullets.append(self._make_bullet(sentences[1], entities))
            bullets.append(self._extract_theme(transcript))
        elif len(sentences) == 1:
            bullets.append(self._make_bullet(sentences[0], entities))
            bullets.append(self._extract_theme(transcript))
            bullets.append("I'm noticing how I feel about this.")
        else:
            bullets = [
                "I shared something today.",
                "I'm reflecting on my thoughts.",
                "I'm being present with my feelings."
            ]
        
        return [self._truncate(b, 110) for b in bullets]

    def _make_bullet(self, sentence: str, entities: List[str]) -> str:
        """Convert a sentence into a first-person reflection."""
        sentence = sentence.strip()
        if sentence.lower().startswith("i "):
            return sentence
        return f"I noticed that {sentence.lower()}"

    def _extract_theme(self, text: str) -> str:
        """Extract a thematic reflection from text."""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["work", "job", "meeting", "boss"]):
            return "I'm thinking about my work situation."
        elif any(word in text_lower for word in ["friend", "family", "relationship", "partner"]):
            return "I'm reflecting on my relationships."
        elif any(word in text_lower for word in ["feel", "feeling", "emotion", "happy", "sad", "angry", "worried"]):
            return "I'm processing how I feel right now."
        return "I'm exploring what's on my mind."

    def _generate_prompt(self, transcript: str, emotion: Emotion) -> str:
        """Generate a personalized follow-up prompt."""
        prompts = {
            "calm_content": "What small joy might you notice tomorrow?",
            "calm_sad": "What would feel gentle or supportive tomorrow?",
            "tense_worried": "What's one thing you can control tomorrow?",
            "tense_angry": "What boundary might you want to set tomorrow?",
            "energized_hopeful": "What momentum can you carry into tomorrow?",
            "energized_anxious": "What would help you feel grounded tomorrow?",
            "neutral": "What would you like to pay attention to tomorrow?"
        }
        
        prompt = prompts.get(emotion.label, prompts["neutral"])
        return self._truncate(prompt, 120)

    def _truncate(self, text: str, max_len: int) -> str:
        """Truncate text to max length."""
        if len(text) <= max_len:
            return text
        return text[:max_len-3] + "..."


# Global service instance
ai_service = AIService()
