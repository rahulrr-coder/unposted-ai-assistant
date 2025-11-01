# Unposted AI Journaling Assistant

A private, non-judgmental journaling assistant that processes spoken journal transcripts and provides emotional analysis with personalized reflections.

## Features

- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels
- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript
- **Personalized Prompts**: Contextual follow-up questions for tomorrow
- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)
- **Minimal Dependencies**: Built with Python 3.10+ and Pydantic only

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment (recommended)**:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.assistant import JournalingAssistant

assistant = JournalingAssistant()

input_data = {
    "transcript": "I had a really good day at work today. My presentation went well.",
    "entities": ["work", "presentation"],
    "prosody": {
        "mean_pitch_hz": 180.0,
        "pitch_var": 400.0,
        "rms_energy": 0.05,
        "speech_rate_wps": 2.5
    },
    "sentiment": {
        "valence": 0.7,
        "confidence": 0.85
    },
    "language": "en",
    "privacy": {
        "pii_redaction_enabled": False
    }
}

result = assistant.process(input_data)
print(result)  # Returns JSON string
```

## Input Schema

```python
{
    "transcript": str,              # 60-90 seconds of speech (required)
    "entities": List[str],          # Key people/events (optional, default: [])
    "prosody": {                    # Acoustic features (required)
        "mean_pitch_hz": float,     # Average pitch in Hz
        "pitch_var": float,         # Pitch variance
        "rms_energy": float,        # RMS energy level
        "speech_rate_wps": float    # Words per second
    },
    "sentiment": {                  # Text sentiment (required)
        "valence": float,           # -1 (negative) to 1 (positive)
        "confidence": float         # 0 to 1
    },
    "language": str,                # Language code (optional, default: "en")
    "privacy": {                    # Privacy settings (optional)
        "pii_redaction_enabled": bool  # default: False
    }
}
```

## Output Schema

```json
{
    "bullets": [
        "First-person reflection (≤110 chars)",
        "First-person reflection (≤110 chars)",
        "First-person reflection (≤110 chars)"
    ],
    "emotion": {
        "valence": 0.7,              // -1 to 1
        "arousal": 0.45,             // -1 to 1
        "label": "energized hopeful" // See emotion labels below
    },
    "next_prompt": "What momentum can you carry into tomorrow?" // ≤120 chars
}
```

## Emotion Labels

- `calm content` - Low arousal, positive valence
- `calm sad` - Low arousal, negative valence
- `tense worried` - High arousal, neutral/negative valence
- `tense angry` - High arousal, negative valence
- `energized hopeful` - High arousal, positive valence
- `energized anxious` - High arousal, neutral valence
- `neutral` - Near-zero valence and arousal

## Examples

Run the example script to see various use cases:

```bash
python examples/example_usage.py
```

This demonstrates:
- Basic journal entry processing
- PII redaction
- Low confidence handling (defaults to neutral)
- Different emotional states (anxious, calm sad, etc.)

## Project Structure

```
unposted-ai-assistant/
├── src/
│   ├── __init__.py
│   └── assistant.py        # Main JournalingAssistant class
├── examples/
│   └── example_usage.py    # Usage examples
├── tests/                  # Unit tests (future)
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## How It Works

1. **Input Validation**: Uses Pydantic models to ensure data integrity
2. **PII Redaction**: Regex-based redaction of sensitive information
3. **Emotion Calculation**:
   - Valence from text sentiment analysis
   - Arousal from prosodic features (pitch, energy, speech rate)
   - Low confidence or short transcripts → neutral
4. **Reflection Generation**: Extracts key moments from transcript, converts to first-person
5. **Prompt Generation**: Context-aware follow-up based on emotional state

## Privacy & Ethics

- **Non-judgmental**: No clinical diagnosis or prescriptive advice
- **Privacy-first**: Optional PII redaction
- **Grounded**: All reflections based on actual transcript content
- **Empathetic**: Supportive, warm tone without clichés

## Requirements

- Python 3.10 or higher
- pydantic >= 2.0.0

## License

MIT License - Feel free to use and modify for your projects.

## Contributing

Contributions are welcome! Please ensure code follows:
- Type hints for all functions
- Pydantic models for data validation
- Minimal dependencies
- Clear documentation

## Support

For issues or questions, please open an issue on the repository.
