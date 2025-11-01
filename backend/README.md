# Unposted AI Assistant - Backend

FastAPI backend for the Unposted AI journaling assistant with personalized news integration.

## Features

- **AI Journaling**: Process voice transcripts with emotional analysis
- **News Integration**: Personalized news feed from NewsAPI
- **Voice Synthesis**: Text-to-speech using OpenAI
- **User Authentication**: JWT-based auth with Supabase
- **Personalization**: User preferences and recommendations

## Architecture

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Environment configuration
│   ├── database.py          # Supabase client
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── services/
│   │   ├── ai_service.py    # Journal processing
│   │   ├── news_service.py  # NewsAPI integration
│   │   ├── voice_service.py # OpenAI TTS
│   │   └── personalization.py # User recommendations
│   └── api/
│       ├── auth.py          # Authentication endpoints
│       ├── news.py          # News endpoints
│       ├── preferences.py   # User preferences
│       └── voice.py         # Voice & journal endpoints
└── .env.example             # Environment template
```

## Setup

### 1. Create Environment File

```bash
cp backend/.env.example backend/.env
```

### 2. Configure API Keys

Edit `backend/.env` and add your API keys:

```env
# Supabase
SUPABASE_URL="https://your-project.supabase.co"
SUPABASE_KEY="your-supabase-anon-key"

# News API
NEWS_API_KEY="your-newsapi-key"

# Anthropic Claude
ANTHROPIC_API_KEY="your-anthropic-api-key"

# OpenAI
OPENAI_API_KEY="your-openai-api-key"

# Security
SECRET_KEY="generate-a-random-secret-key"
```

### 3. Install Dependencies

```bash
# From project root
pip install -r requirements.txt
```

### 4. Run the Server

```bash
# From project root
./start_backend.sh

# Or manually:
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Documentation

Once the server is running, visit:

- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get token
- `GET /auth/me` - Get current user

### News

- `GET /news/` - Get personalized news feed
- `GET /news/search?q=query` - Search news
- `GET /news/recommendations` - AI-recommended articles

### Preferences

- `GET /preferences/` - Get user preferences
- `PUT /preferences/` - Update preferences
- `POST /preferences/track-interaction` - Track article interactions

### Voice & Journal

- `POST /voice/generate` - Generate speech from text
- `GET /voice/voices` - Get available voices
- `POST /voice/journal` - Process voice journal entry

## Environment Variables

See `backend/.env.example` for all available options.

## Development

### Running Tests

```bash
python tests/test_ai_service.py
```

### Running Examples

```bash
python examples/example_usage.py
```

## API Keys Required

1. **Supabase**: https://supabase.com
2. **NewsAPI**: https://newsapi.org
3. **Anthropic**: https://anthropic.com
4. **OpenAI**: https://openai.com

## Tech Stack

- **Framework**: FastAPI 0.104+
- **Database**: Supabase (PostgreSQL)
- **AI**: Claude 3.5 Sonnet (Anthropic)
- **Voice**: OpenAI TTS
- **News**: NewsAPI
- **Auth**: JWT with python-jose
