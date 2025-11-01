"""
Tests for AI Service
Run from backend directory: python -m pytest tests/
"""
from app.services.ai_service import ai_service
from app.models.schemas import JournalInput, Prosody, Sentiment, Privacy


def test_basic_processing():
    """Test basic journal processing."""
    input_data = JournalInput(
        transcript="I had a great day today. Everything went well.",
        entities=[],
        prosody=Prosody(
            mean_pitch_hz=180.0,
            pitch_var=400.0,
            rms_energy=0.05,
            speech_rate_wps=2.5
        ),
        sentiment=Sentiment(valence=0.7, confidence=0.8)
    )
    
    result = ai_service.process_journal(input_data)
    
    assert len(result.bullets) == 3
    assert all(len(b) <= 110 for b in result.bullets)
    assert len(result.next_prompt) <= 120
    assert -1 <= result.emotion.valence <= 1
    assert -1 <= result.emotion.arousal <= 1


def test_pii_redaction():
    """Test PII redaction."""
    input_data = JournalInput(
        transcript="Call me at 555-123-4567 or email test@example.com",
        entities=[],
        prosody=Prosody(
            mean_pitch_hz=180.0,
            pitch_var=400.0,
            rms_energy=0.05,
            speech_rate_wps=2.5
        ),
        sentiment=Sentiment(valence=0.0, confidence=0.8),
        privacy=Privacy(pii_redaction_enabled=True)
    )
    
    result = ai_service.process_journal(input_data)
    
    bullets_text = " ".join(result.bullets).lower()
    assert "555-123-4567" not in bullets_text
    assert "test@example.com" not in bullets_text
    assert "[phone]" in bullets_text or "[email]" in bullets_text


def test_low_confidence_neutral():
    """Test that low confidence results in neutral emotion."""
    input_data = JournalInput(
        transcript="Um, yeah, today was a day.",
        entities=[],
        prosody=Prosody(
            mean_pitch_hz=150.0,
            pitch_var=200.0,
            rms_energy=0.03,
            speech_rate_wps=1.5
        ),
        sentiment=Sentiment(valence=0.5, confidence=0.3)
    )
    
    result = ai_service.process_journal(input_data)
    
    assert result.emotion.label == "neutral"
    assert result.emotion.valence == 0.0
    assert result.emotion.arousal == 0.0


def test_emotion_labels():
    """Test different emotion labels."""
    # Test calm content
    calm_happy = JournalInput(
        transcript="I had a peaceful and happy day today. Everything feels right.",
        entities=[],
        prosody=Prosody(mean_pitch_hz=140.0, pitch_var=250.0, rms_energy=0.04, speech_rate_wps=1.8),
        sentiment=Sentiment(valence=0.6, confidence=0.85)
    )
    result = ai_service.process_journal(calm_happy)
    assert result.emotion.label == "calm content"
    
    # Test tense angry
    angry = JournalInput(
        transcript="I'm so frustrated and angry about what happened today! This is unacceptable!",
        entities=[],
        prosody=Prosody(mean_pitch_hz=220.0, pitch_var=900.0, rms_energy=0.09, speech_rate_wps=3.5),
        sentiment=Sentiment(valence=-0.7, confidence=0.9)
    )
    result = ai_service.process_journal(angry)
    assert result.emotion.label == "tense angry"


if __name__ == "__main__":
    import sys
    
    print("Running tests...")
    tests = [
        test_basic_processing,
        test_pii_redaction,
        test_low_confidence_neutral,
        test_emotion_labels
    ]
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            sys.exit(1)
    
    print("\n✓ All tests passed!")
