# Unposted AI Assistant# Unposted AI Assistant# Unposted AI Journaling Assistant



A private, AI-powered journaling assistant with personalized news integration. Built for the Arré Voice × AI Hackathon.



## OverviewA private, AI-powered journaling assistant with personalized news integration. Built for the Arré Voice × AI Hackathon.A private, non-judgmental journaling assistant that processes spoken journal transcripts and provides emotional analysis with personalized reflections.



Unposted combines voice journaling with emotional analysis and personalized news delivery. Users can speak their thoughts, receive AI-powered insights about their emotional state, and stay informed with curated news tailored to their interests.



## Features## Overview## Features



### 🎙️ AI Journaling

- Process spoken journal transcripts with emotional analysis

- 2-D emotion mapping (valence & arousal)Unposted combines voice journaling with emotional analysis and personalized news delivery. Users can speak their thoughts, receive AI-powered insights, and stay informed with curated news tailored to their interests.- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels

- Three concise, first-person reflections

- Personalized follow-up prompts- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript

- Privacy-first with PII redaction

## Features- **Personalized Prompts**: Contextual follow-up questions for tomorrow

### 📰 Personalized News

- AI-curated news feed from NewsAPI- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)

- Category and source filtering

- Reading history tracking### 🎙️ Voice Journaling- **Minimal Dependencies**: Built with Python 3.10+ and Pydantic only

- Smart recommendations based on user behavior

- Process spoken journal transcripts with emotional analysis

### 🔊 Voice Synthesis

- Text-to-speech for news articles using OpenAI- 2-D emotion mapping (valence & arousal)## Installation

- Multiple voice options

- Adjustable speed- Three concise, first-person reflections



### 🔐 User Management- Personalized follow-up prompts1. **Clone or download this repository**

- JWT-based authentication

- User preferences and settings- Privacy-first with PII redaction

- Supabase backend integration

2. **Create a virtual environment (recommended)**:

## Project Structure

### 📰 Personalized News```bash

```

unposted-ai-assistant/- AI-curated news feed based on preferencespython3 -m venv .venv

├── backend/                    # FastAPI backend server

│   ├── app/- Category and source filteringsource .venv/bin/activate  # On Linux/Mac

│   │   ├── main.py            # Application entry point

│   │   ├── config.py          # Environment configuration- Reading history tracking# or

│   │   ├── database.py        # Supabase client

│   │   ├── models/- Smart recommendations.venv\Scripts\activate  # On Windows

│   │   │   └── schemas.py     # Pydantic models

│   │   ├── services/```

│   │   │   ├── ai_service.py  # Journal processing

│   │   │   ├── news_service.py # News API integration### 🔊 Voice Synthesis

│   │   │   ├── voice_service.py # TTS service

│   │   │   └── personalization.py # Recommendations- Text-to-speech for news articles3. **Install dependencies**:

│   │   └── api/

│   │       ├── auth.py        # Authentication endpoints- Multiple voice options```bash

│   │       ├── news.py        # News endpoints

│   │       ├── preferences.py # User preferences- Adjustable speed and tonepip install -r requirements.txt

│   │       └── voice.py       # Voice & journal endpoints

│   ├── tests/                 # Unit tests```

│   ├── examples/              # Usage examples

│   ├── requirements.txt       # Python dependencies### 🔐 Authentication & Privacy

│   ├── .env.example          # Environment template

│   └── README.md             # Backend documentation- Secure user authentication with JWT## Quick Start

├── client/                    # Streamlit UI (coming soon)

├── start_backend.sh          # Backend start script- Supabase backend

└── README.md                 # This file

```- Privacy controls and PII redaction```python



## Quick Startfrom src.assistant import JournalingAssistant



### 1. Backend Setup## Architecture



```bashassistant = JournalingAssistant()

# Navigate to backend directory

cd backend```



# Create virtual environmentunposted-ai-assistant/input_data = {

python3 -m venv .venv

source .venv/bin/activate  # On Windows: .venv\Scripts\activate├── backend/               # FastAPI server    "transcript": "I had a really good day at work today. My presentation went well.",



# Install dependencies│   ├── app/    "entities": ["work", "presentation"],

pip install -r requirements.txt

│   │   ├── main.py       # Application entry    "prosody": {

# Set up environment variables

cp .env.example .env│   │   ├── config.py     # Configuration        "mean_pitch_hz": 180.0,

# Edit .env with your API keys

```│   │   ├── database.py   # Supabase client        "pitch_var": 400.0,



### 2. Configure API Keys│   │   ├── models/       # Pydantic schemas        "rms_energy": 0.05,



Edit `backend/.env` with your credentials:│   │   ├── services/     # Business logic        "speech_rate_wps": 2.5



- **Supabase**: Database and authentication│   │   └── api/          # API endpoints    },

- **NewsAPI**: News articles

- **Anthropic**: Claude AI (optional, for future features)│   ├── .env.example      # Environment template    "sentiment": {

- **OpenAI**: Text-to-speech

│   └── README.md         # Backend documentation        "valence": 0.7,

### 3. Start the Server

├── examples/             # Usage examples        "confidence": 0.85

```bash

# From project root├── tests/                # Unit tests    },

./start_backend.sh

└── requirements.txt      # Python dependencies    "language": "en",

# Or from backend directory

cd backend```    "privacy": {

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

```        "pii_redaction_enabled": False



The API will be available at:## Quick Start    }

- **API**: http://localhost:8000

- **Docs**: http://localhost:8000/docs}

- **ReDoc**: http://localhost:8000/redoc

### 1. Clone Repository

## API Endpoints

result = assistant.process(input_data)

### Authentication

- `POST /auth/register` - Register new user```bashprint(result)  # Returns JSON string

- `POST /auth/login` - Login and get JWT token

- `GET /auth/me` - Get current usergit clone https://github.com/rahulrr-coder/unposted-ai-assistant.git```



### Voice & Journalingcd unposted-ai-assistant

- `POST /voice/journal` - Process journal entry

- `POST /voice/generate` - Generate speech from text```## Input Schema

- `GET /voice/voices` - List available voices



### News

- `GET /news/` - Get personalized news feed### 2. Create Virtual Environment```python

- `GET /news/search?q=query` - Search news

- `GET /news/recommendations` - Get AI recommendations{



### Preferences```bash    "transcript": str,              # 60-90 seconds of speech (required)

- `GET /preferences/` - Get user preferences

- `PUT /preferences/` - Update preferencespython3 -m venv .venv    "entities": List[str],          # Key people/events (optional, default: [])

- `POST /preferences/track-interaction` - Track article interaction

source .venv/bin/activate  # On Linux/Mac    "prosody": {                    # Acoustic features (required)

## Running Examples

```        "mean_pitch_hz": float,     # Average pitch in Hz

```bash

cd backend        "pitch_var": float,         # Pitch variance

python examples/example_usage.py

```### 3. Install Dependencies        "rms_energy": float,        # RMS energy level



## Running Tests        "speech_rate_wps": float    # Words per second



```bash```bash    },

cd backend

python tests/test_ai_service.pypip install -r requirements.txt    "sentiment": {                  # Text sentiment (required)



# Or with pytest (if installed)```        "valence": float,           # -1 (negative) to 1 (positive)

pytest tests/

```        "confidence": float         # 0 to 1



## Tech Stack### 4. Configure Environment    },



### Backend    "language": str,                # Language code (optional, default: "en")

- **FastAPI**: Modern Python web framework

- **Pydantic**: Data validation```bash    "privacy": {                    # Privacy settings (optional)

- **Supabase**: Database and authentication

- **NewsAPI**: News aggregationcp backend/.env.example backend/.env        "pii_redaction_enabled": bool  # default: False

- **OpenAI**: Text-to-speech

- **Anthropic Claude**: AI analysis (planned)# Edit backend/.env with your API keys    }



### Planned Client```}

- **Streamlit**: Interactive web UI

- **Audio recording**: Browser-based voice capture```

- **Real-time processing**: Live emotional analysis

### 5. Start Backend Server

## Environment Variables

## Output Schema

See `backend/.env.example` for all required variables:

```bash

```env

# Core./start_backend.sh```json

SUPABASE_URL=your-supabase-url

SUPABASE_KEY=your-supabase-key```{

NEWS_API_KEY=your-newsapi-key

OPENAI_API_KEY=your-openai-key    "bullets": [

ANTHROPIC_API_KEY=your-anthropic-key

The API will be available at:        "First-person reflection (≤110 chars)",

# Security

SECRET_KEY=your-jwt-secret-key- **API**: http://localhost:8000        "First-person reflection (≤110 chars)",

```

- **Docs**: http://localhost:8000/docs        "First-person reflection (≤110 chars)"

## Development Roadmap

- **ReDoc**: http://localhost:8000/redoc    ],

- [x] Backend API with FastAPI

- [x] AI journaling service    "emotion": {

- [x] News integration

- [x] Voice synthesis## API Keys Required        "valence": 0.7,              // -1 to 1

- [x] User authentication

- [ ] Streamlit client UI        "arousal": 0.45,             // -1 to 1

- [ ] Audio recording in browser

- [ ] Real-time emotion visualizationYou'll need API keys from:        "label": "energized hopeful" // See emotion labels below

- [ ] Mobile app (future)

    },

## Contributing

1. **Supabase** - Database and authentication    "next_prompt": "What momentum can you carry into tomorrow?" // ≤120 chars

Contributions welcome! Please ensure:

- Type hints for all functions   - Sign up: https://supabase.com}

- Pydantic models for data validation

- Tests for new features   - Create a project and copy your URL and anon key```

- Clear documentation



## License

2. **NewsAPI** - News articles## Emotion Labels

MIT License - Feel free to use and modify for your projects.

   - Sign up: https://newsapi.org

## Support

   - Free tier: 100 requests/day- `calm content` - Low arousal, positive valence

For issues or questions, please open an issue on the repository.

- `calm sad` - Low arousal, negative valence

---

3. **Anthropic** - Claude for AI processing- `tense worried` - High arousal, neutral/negative valence

Built with ❤️ for the Arré Voice × AI Hackathon

   - Sign up: https://anthropic.com- `tense angry` - High arousal, negative valence

   - Model: Claude 3.5 Sonnet- `energized hopeful` - High arousal, positive valence

- `energized anxious` - High arousal, neutral valence

4. **OpenAI** - Text-to-speech- `neutral` - Near-zero valence and arousal

   - Sign up: https://openai.com

   - Used for TTS voice generation## Examples



## Usage ExamplesRun the example script to see various use cases:



### Process a Journal Entry```bash

python examples/example_usage.py

```python```

from backend.app.services.ai_service import ai_service

from backend.app.models.schemas import JournalInput, Prosody, Sentiment, PrivacyThis demonstrates:

- Basic journal entry processing

input_data = JournalInput(- PII redaction

    transcript="I had a great day today. Everything went well.",- Low confidence handling (defaults to neutral)

    entities=["work"],- Different emotional states (anxious, calm sad, etc.)

    prosody=Prosody(

        mean_pitch_hz=180.0,## Project Structure

        pitch_var=400.0,

        rms_energy=0.05,```

        speech_rate_wps=2.5unposted-ai-assistant/

    ),├── src/

    sentiment=Sentiment(│   ├── __init__.py

        valence=0.7,│   └── assistant.py        # Main JournalingAssistant class

        confidence=0.85├── examples/

    ),│   └── example_usage.py    # Usage examples

    privacy=Privacy(pii_redaction_enabled=False)├── tests/                  # Unit tests (future)

)├── requirements.txt        # Python dependencies

├── .gitignore

result = ai_service.process_journal(input_data)└── README.md

print(result.model_dump_json(indent=2))```

```

## How It Works

### Run Examples

1. **Input Validation**: Uses Pydantic models to ensure data integrity

```bash2. **PII Redaction**: Regex-based redaction of sensitive information

python examples/example_usage.py3. **Emotion Calculation**:

```   - Valence from text sentiment analysis

   - Arousal from prosodic features (pitch, energy, speech rate)

### Run Tests   - Low confidence or short transcripts → neutral

4. **Reflection Generation**: Extracts key moments from transcript, converts to first-person

```bash5. **Prompt Generation**: Context-aware follow-up based on emotional state

python tests/test_ai_service.py

```## Privacy & Ethics



## API Endpoints- **Non-judgmental**: No clinical diagnosis or prescriptive advice

- **Privacy-first**: Optional PII redaction

### Authentication- **Grounded**: All reflections based on actual transcript content

- `POST /auth/register` - Register new user- **Empathetic**: Supportive, warm tone without clichés

- `POST /auth/login` - Login and get token

- `GET /auth/me` - Get current user profile## Requirements



### News- Python 3.10 or higher

- `GET /news/` - Get personalized news feed- pydantic >= 2.0.0

- `GET /news/search` - Search news articles

- `GET /news/recommendations` - AI-recommended news## License



### PreferencesMIT License - Feel free to use and modify for your projects.

- `GET /preferences/` - Get user preferences

- `PUT /preferences/` - Update preferences## Contributing

- `POST /preferences/track-interaction` - Track reading

Contributions are welcome! Please ensure code follows:

### Voice & Journal- Type hints for all functions

- `POST /voice/generate` - Generate speech from text- Pydantic models for data validation

- `GET /voice/voices` - List available voices- Minimal dependencies

- `POST /voice/journal` - Process journal entry- Clear documentation



## Tech Stack## Support



- **Backend**: FastAPI, Python 3.10+For issues or questions, please open an issue on the repository.

- **Database**: Supabase (PostgreSQL)
- **AI**: Claude 3.5 Sonnet (Anthropic)
- **Voice**: OpenAI TTS
- **News**: NewsAPI
- **Auth**: JWT with python-jose
- **Validation**: Pydantic v2

## Development

### Project Structure

- `backend/app/main.py` - FastAPI application
- `backend/app/services/` - Business logic
- `backend/app/api/` - API routes
- `backend/app/models/` - Data schemas
- `examples/` - Usage examples
- `tests/` - Unit tests

### Running in Development Mode

```bash
./start_backend.sh
```

This runs with hot-reload enabled.

## Privacy & Ethics

- **Non-judgmental**: No clinical diagnosis or prescriptive advice
- **Privacy-first**: Optional PII redaction
- **Grounded**: Reflections based on actual content
- **Empathetic**: Supportive, warm tone
- **Secure**: JWT authentication, encrypted storage

## Contributing

Contributions welcome! Please ensure:
- Type hints for all functions
- Pydantic models for validation
- Tests for new features
- Clear documentation

## License

MIT License

## Support

For issues or questions, please open an issue on GitHub.

## Roadmap

- [ ] Streamlit web UI
- [ ] Voice recording integration
- [ ] Historical journal analytics
- [ ] Multi-language support
- [ ] Mobile app
- [ ] Calendar integration

## Acknowledgments

Built for the Arré Voice × AI Hackathon 2025
