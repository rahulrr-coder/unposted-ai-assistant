#!/usr/bin/env python3
"""
Example usage of the AI Journaling Service.
Run this from the backend directory: python examples/example_usage.py
"""
from app.services.ai_service import ai_service
from app.models.schemas import JournalInput, Prosody, Sentiment, Privacy


def example_basic():
    """Basic example with a simple journal entry."""
    print("=" * 60)
    print("EXAMPLE 1: Basic Journal Entry")
    print("=" * 60)
    
    input_data = JournalInput(
        transcript="I had a really good day at work today. My presentation went well and my boss seemed impressed. I'm feeling pretty confident about the project now.",
        entities=["boss", "work", "project"],
        prosody=Prosody(
            mean_pitch_hz=180.0,
            pitch_var=400.0,
            rms_energy=0.05,
            speech_rate_wps=2.5
        ),
        sentiment=Sentiment(valence=0.7, confidence=0.85)
    )
    
    result = ai_service.process_journal(input_data)
    print(f"\nInput: {input_data.transcript[:80]}...")
    print(f"\nOutput:")
    print(result.model_dump_json(indent=2))
    print()


def example_with_pii():
    """Example with PII redaction enabled."""
    print("=" * 60)
    print("EXAMPLE 2: PII Redaction")
    print("=" * 60)
    
    input_data = JournalInput(
        transcript="Call me at 555-123-4567 or email john@example.com about the appointment.",
        entities=[],
        prosody=Prosody(
            mean_pitch_hz=190.0,
            pitch_var=600.0,
            rms_energy=0.07,
            speech_rate_wps=2.8
        ),
        sentiment=Sentiment(valence=-0.3, confidence=0.75),
        privacy=Privacy(pii_redaction_enabled=True)
    )
    
    result = ai_service.process_journal(input_data)
    print(f"\nInput: {input_data.transcript}")
    print(f"PII Redaction: Enabled")
    print(f"\nOutput:")
    print(result.model_dump_json(indent=2))
    print()


def example_emotions():
    """Example showing different emotional states."""
    print("=" * 60)
    print("EXAMPLE 3: Different Emotions")
    print("=" * 60)
    
    # Anxious
    anxious = JournalInput(
        transcript="I'm really worried about tomorrow's interview. What if everything goes wrong?",
        entities=["interview"],
        prosody=Prosody(mean_pitch_hz=220.0, pitch_var=800.0, rms_energy=0.08, speech_rate_wps=3.2),
        sentiment=Sentiment(valence=-0.5, confidence=0.9)
    )
    
    # Calm & Happy
    calm = JournalInput(
        transcript="I spent a peaceful afternoon reading by the window. The weather was perfect.",
        entities=[],
        prosody=Prosody(mean_pitch_hz=140.0, pitch_var=250.0, rms_energy=0.04, speech_rate_wps=1.8),
        sentiment=Sentiment(valence=0.6, confidence=0.85)
    )
    
    for name, data in [("Anxious", anxious), ("Calm & Happy", calm)]:
        result = ai_service.process_journal(data)
        print(f"\n{name}: {result.emotion.label}")
        print(f"  Valence: {result.emotion.valence}, Arousal: {result.emotion.arousal}")


if __name__ == "__main__":
    example_basic()
    example_with_pii()
    example_emotions()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)
