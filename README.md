# 🎙️ Unposted AI Journaling Assistant# 🎙️ Unposted AI Journaling Assistant# 🎙️ Unposted AI Journaling Assistant# 🎙️ Unposted AI Journaling Assistant



> A private, AI-powered journaling assistant with emotional analysis and personalized news integration.



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)> A private, AI-powered journaling assistant with emotional analysis and personalized news integration.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)



Built for the **Arré Voice × AI Hackathon 2025**[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)> A private, AI-powered journaling assistant with emotional analysis and personalized news integration.> A private, AI-powered journaling assistant with emotional analysis and personalized news integration.



---[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)



## 📖 Overview[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)



Unposted combines voice journaling with emotional analysis and personalized news delivery. Speak your thoughts, receive AI-powered emotional insights, and stay informed with curated news tailored to your interests.



## ✨ FeaturesBuilt for the **Arré Voice × AI Hackathon 2025**[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



### 🎙️ AI Journaling

- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels

- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript---[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

- **Personalized Prompts**: Contextual follow-up questions for tomorrow

- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)



### 📰 Personalized News## 📖 Overview[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

- AI-curated news feed from NewsAPI

- Category and source filtering

- Reading history tracking

- Smart recommendations based on your behaviorUnposted combines voice journaling with emotional analysis and personalized news delivery. Speak your thoughts, receive AI-powered emotional insights, and stay informed with curated news tailored to your interests.



### 🔊 Voice Synthesis

- Text-to-speech for news articles using OpenAI TTS

- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)## ✨ Features Built for the **Arré Voice × AI Hackathon 2025**Built for the **Arré Voice × AI Hackathon 2025**

- Adjustable speed and tone



### 🔐 Authentication & Security

- JWT-based authentication via Supabase### 🎙️ AI Journaling

- Row-level security (RLS) for data protection

- User preferences and settings management- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels

- Todo/task management with CRUD operations

- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript------

---

- **Personalized Prompts**: Contextual follow-up questions for tomorrow

## 🚀 Quick Start

- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)

### Prerequisites

- Python 3.10+

- Git

- API keys: Supabase, NewsAPI, OpenAI, Anthropic (optional)### 📰 Personalized News## 📖 Overview## 📖 Overview



### 1. Clone Repository- AI-curated news feed from NewsAPI

```bash

git clone https://github.com/rahulrr-coder/unposted-ai-assistant.git- Category and source filtering

cd unposted-ai-assistant

```- Reading history tracking



### 2. Backend Setup- Smart recommendations based on your behaviorUnposted combines voice journaling with emotional analysis and personalized news delivery. Speak your thoughts, receive AI-powered emotional insights, and stay informed with curated news tailored to your interests.Unposted combines voice journaling with emotional analysis and personalized news delivery. Speak your thoughts, receive AI-powered emotional insights, and stay informed with curated news tailored to your interests.

```bash

cd backend



# Create virtual environment### 🔊 Voice Synthesis

python3 -m venv .venv

source .venv/bin/activate  # Windows: .venv\Scripts\activate- Text-to-speech for news articles using OpenAI TTS



# Install dependencies- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)## ✨ Features

pip install -r requirements.txt

- Adjustable speed and tone

# Configure environment

cp .env.example .env## ✨ Features

# Edit .env with your API keys

```### 🔐 Authentication & Security



### 3. Configure Supabase- JWT-based authentication via Supabase### 🎙️ AI Journaling

1. Create account at [supabase.com](https://supabase.com)

2. Copy project URL and anon key to `.env`- Row-level security (RLS) for data protection

3. Run migration in SQL Editor:

   - Open Supabase SQL Editor- User preferences and settings management- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels### 🎙️ AI Journaling

   - Copy `backend/migrations/001_initial_schema.sql`

   - Execute migration- Todo/task management with CRUD operations



### 4. Start Server- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript- **Emotional Analysis**: 2-D emotion mapping (valence & arousal) with human-readable labels

```bash

# From project root---

./start_backend.sh

- **Personalized Prompts**: Contextual follow-up questions for tomorrow- **Reflection Bullets**: Three concise, first-person reflections grounded in your transcript

# Or manually

cd backend## 🚀 Quick Start

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)- **Personalized Prompts**: Contextual follow-up questions for tomorrow



### 5. Access API### Prerequisites

- **API**: http://localhost:8000

- **Interactive Docs**: http://localhost:8000/docs- Python 3.10+- **Privacy First**: Optional PII redaction (emails, phone numbers, addresses)

- **ReDoc**: http://localhost:8000/redoc

- Git

---

- API keys: Supabase, NewsAPI, OpenAI, Anthropic (optional)### 📰 Personalized News

## 📚 API Endpoints



### Authentication

- `POST /auth/register` - Register new user### 1. Clone Repository- AI-curated news feed from NewsAPI### 📰 Personalized News

- `POST /auth/login` - Login and get JWT token

- `GET /auth/me` - Get current user profile```bash



### Todosgit clone https://github.com/rahulrr-coder/unposted-ai-assistant.git- Category and source filtering- AI-curated news feed from NewsAPI

- `GET /api/todos` - List all todos (with filters)

- `POST /api/todos` - Create new todocd unposted-ai-assistant

- `GET /api/todos/{id}` - Get single todo

- `PUT /api/todos/{id}` - Update todo```- Reading history tracking- Category and source filtering

- `DELETE /api/todos/{id}` - Delete todo



### Voice & Journaling

- `POST /voice/journal` - Process journal entry with emotional analysis### 2. Backend Setup- Smart recommendations based on your behavior- Reading history tracking

- `POST /voice/generate` - Generate speech from text (TTS)

- `GET /voice/voices` - List available voice options```bash



### Newscd backend- Smart recommendations based on your behavior

- `GET /news/` - Get personalized news feed

- `GET /news/search` - Search news articles

- `GET /news/recommendations` - Get AI-recommended articles

# Create virtual environment### 🔊 Voice Synthesis

### Preferences

- `GET /preferences/` - Get user preferencespython3 -m venv .venv

- `PUT /preferences/` - Update preferences

- `POST /preferences/track-interaction` - Track article interactionsource .venv/bin/activate  # Windows: .venv\Scripts\activate- Text-to-speech for news articles using OpenAI TTS### 🔊 Voice Synthesis



📖 **Full Documentation**: http://localhost:8000/docs



---# Install dependencies- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)- Text-to-speech for news articles using OpenAI TTS



## 🏗️ Project Structurepip install -r requirements.txt



```- Adjustable speed and tone- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)

unposted-ai-assistant/

├── backend/# Configure environment

│   ├── app/

│   │   ├── main.py              # Application entry pointcp .env.example .env- Adjustable speed and tone

│   │   ├── config.py            # Environment configuration

│   │   ├── database.py          # Supabase client# Edit .env with your API keys

│   │   ├── models/

│   │   │   └── schemas.py       # Pydantic models```### 🔐 Authentication & Security

│   │   ├── services/

│   │   │   ├── ai_service.py        # Journal processing

│   │   │   ├── news_service.py      # News API

│   │   │   ├── voice_service.py     # TTS service### 3. Configure Supabase- JWT-based authentication via Supabase### 🔐 Authentication & Security

│   │   │   └── personalization.py   # Recommendations

│   │   └── api/1. Create account at [supabase.com](https://supabase.com)

│   │       ├── auth.py          # Authentication

│   │       ├── todos.py         # Todo CRUD2. Copy project URL and anon key to `.env`- Row-level security (RLS) for data protection- JWT-based authentication via Supabase

│   │       ├── news.py          # News endpoints

│   │       ├── preferences.py   # User preferences3. Run migration in SQL Editor:

│   │       └── voice.py         # Voice & journal

│   ├── migrations/              # Database migrations   - Open Supabase SQL Editor- Secure password hashing- Row-level security (RLS) for data protection

│   ├── tests/                   # Unit tests

│   ├── examples/                # Usage examples   - Copy `backend/migrations/001_initial_schema.sql`

│   ├── requirements.txt

│   ├── .env.example   - Execute migration- User preferences and settings management- Secure password hashing

│   ├── TESTING.md

│   └── README.md

├── start_backend.sh

└── README.md### 4. Start Server- User preferences and settings management

```

```bash

---

# From project root---

## 🛠️ Tech Stack

./start_backend.sh

### Backend

- **FastAPI** - Modern Python web framework---│   │       ├── auth.py        # Authentication endpoints- Multiple voice options```bash

- **Pydantic v2** - Data validation

- **Supabase** - PostgreSQL database with auth# Or manually

- **NewsAPI** - News aggregation

- **OpenAI** - Text-to-speechcd backend## 🚀 Quick Start

- **Anthropic Claude 3.5** - AI analysis

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

---

```│   │       ├── news.py        # News endpoints

## 💻 Usage Example



```python

from backend.app.services.ai_service import ai_service### 5. Access API### Prerequisites

from backend.app.models.schemas import JournalInput, Prosody, Sentiment

- **API**: http://localhost:8000

input_data = JournalInput(

    transcript="I had a great day today. Everything went well.",- **Interactive Docs**: http://localhost:8000/docs- Python 3.10+│   │       ├── preferences.py # User preferences- Adjustable speed and tonepip install -r requirements.txt

    entities=["work"],

    prosody=Prosody(- **ReDoc**: http://localhost:8000/redoc

        mean_pitch_hz=180.0,

        pitch_var=400.0,- Git

        rms_energy=0.05,

        speech_rate_wps=2.5---

    ),

    sentiment=Sentiment(valence=0.7, confidence=0.85)- API keys from: Supabase, NewsAPI, OpenAI, Anthropic (optional)│   │       └── voice.py       # Voice & journal endpoints

)

## 📚 API Endpoints

result = ai_service.process_journal(input_data)

print(result.model_dump_json(indent=2))

```

### Authentication

Run examples:

```bash- `POST /auth/register` - Register new user### 1. Clone Repository│   ├── tests/                 # Unit tests```

cd backend

python examples/example_usage.py- `POST /auth/login` - Login and get JWT token

```

- `GET /auth/me` - Get current user profile```bash

---



## 🧪 Testing

### Todosgit clone https://github.com/rahulrr-coder/unposted-ai-assistant.git│   ├── examples/              # Usage examples

```bash

cd backend- `GET /api/todos` - List all todos (with filters)



# Run tests- `POST /api/todos` - Create new todocd unposted-ai-assistant

python tests/test_ai_service.py

- `GET /api/todos/{id}` - Get single todo

# Or with pytest

pytest tests/- `PUT /api/todos/{id}` - Update todo```│   ├── requirements.txt       # Python dependencies### 🔐 Authentication & Privacy

```

- `DELETE /api/todos/{id}` - Delete todo

See `backend/TESTING.md` for comprehensive API testing guide.



---

### Voice & Journaling

## 🔑 Environment Variables

- `POST /voice/journal` - Process journal entry with emotional analysis### 2. Set Up Backend│   ├── .env.example          # Environment template

Required in `backend/.env`:

- `POST /voice/generate` - Generate speech from text (TTS)

```env

# Supabase- `GET /voice/voices` - List available voice options```bash

SUPABASE_URL=your-supabase-url

SUPABASE_KEY=your-supabase-anon-key



# APIs### Newscd backend│   └── README.md             # Backend documentation- Secure user authentication with JWT## Quick Start

NEWS_API_KEY=your-newsapi-key

OPENAI_API_KEY=your-openai-key- `GET /news/` - Get personalized news feed

ANTHROPIC_API_KEY=your-anthropic-key  # Optional

- `GET /news/search` - Search news articles

# Security

SECRET_KEY=your-jwt-secret-key- `GET /news/recommendations` - Get AI-recommended articles

```

# Create virtual environment├── client/                    # Streamlit UI (coming soon)

### Get API Keys

1. **Supabase** - [supabase.com](https://supabase.com)### Preferences

2. **NewsAPI** - [newsapi.org](https://newsapi.org)

3. **OpenAI** - [openai.com](https://openai.com)- `GET /preferences/` - Get user preferencespython3 -m venv .venv

4. **Anthropic** - [anthropic.com](https://anthropic.com)

- `PUT /preferences/` - Update preferences

---

- `POST /preferences/track-interaction` - Track article interactionsource .venv/bin/activate  # On Windows: .venv\Scripts\activate├── start_backend.sh          # Backend start script- Supabase backend

## 🔒 Security & Privacy



- **JWT Authentication** - Secure token-based auth via Supabase

- **Row-Level Security** - Database policies ensure data isolation📖 **Full Documentation**: http://localhost:8000/docs

- **PII Redaction** - Optional removal of sensitive information

- **Encrypted Storage** - Data encrypted at rest in PostgreSQL

- **Password Hashing** - Secure bcrypt hashing

---# Install dependencies└── README.md                 # This file

---



## 📄 License

## 🏗️ Project Structurepip install -r requirements.txt

MIT License



Copyright (c) 2025 Rahul RR

``````- Privacy controls and PII redaction```python

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

unposted-ai-assistant/

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

├── backend/# Configure environment

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

│   ├── app/

---

│   │   ├── main.py              # Application entry pointcp .env.example .env

## 📞 Contact & Support

│   │   ├── config.py            # Environment configuration

**Developer**: Rahul RR  

**GitHub**: [@rahulrr-coder](https://github.com/rahulrr-coder)  │   │   ├── database.py          # Supabase client# Edit .env with your API keys

**Repository**: [unposted-ai-assistant](https://github.com/rahulrr-coder/unposted-ai-assistant)

│   │   ├── models/

**Support**:

- 🐛 [Report issues](https://github.com/rahulrr-coder/unposted-ai-assistant/issues)│   │   │   └── schemas.py       # Pydantic models```## Quick Startfrom src.assistant import JournalingAssistant

- 📖 [Documentation](backend/README.md)

- 🧪 [Testing guide](backend/TESTING.md)│   │   ├── services/



---│   │   │   ├── ai_service.py        # Journal processing



**Built for the Arré Voice × AI Hackathon 2025** 🎉│   │   │   ├── news_service.py      # News API


│   │   │   ├── voice_service.py     # TTS service### 3. Configure Supabase

│   │   │   └── personalization.py   # Recommendations

│   │   └── api/1. Go to your [Supabase Dashboard](https://supabase.com)

│   │       ├── auth.py          # Authentication

│   │       ├── todos.py         # Todo CRUD2. Copy your project URL and anon key to `.env`### 1. Backend Setup## Architecture

│   │       ├── news.py          # News endpoints

│   │       ├── preferences.py   # User preferences3. Run the migration in SQL Editor:

│   │       └── voice.py         # Voice & journal

│   ├── migrations/              # Database migrations   - Open Supabase SQL Editor

│   ├── tests/                   # Unit tests

│   ├── examples/                # Usage examples   - Copy contents from `backend/migrations/001_initial_schema.sql`

│   ├── requirements.txt

│   ├── .env.example   - Execute the migration```bashassistant = JournalingAssistant()

│   ├── TESTING.md

│   └── README.md

├── start_backend.sh

└── README.md### 4. Start the Server# Navigate to backend directory

```

```bash

---

# From project rootcd backend```

## 🛠️ Tech Stack

./start_backend.sh

### Backend

- **FastAPI** - Modern Python web framework

- **Pydantic v2** - Data validation

- **Supabase** - PostgreSQL database with auth# Or from backend directory

- **NewsAPI** - News aggregation

- **OpenAI** - Text-to-speechcd backend# Create virtual environmentunposted-ai-assistant/input_data = {

- **Anthropic Claude 3.5** - AI analysis

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

---

```python3 -m venv .venv

## 💻 Usage Example



```python

from backend.app.services.ai_service import ai_service### 5. Access the APIsource .venv/bin/activate  # On Windows: .venv\Scripts\activate├── backend/               # FastAPI server    "transcript": "I had a really good day at work today. My presentation went well.",

from backend.app.models.schemas import JournalInput, Prosody, Sentiment

- **API**: http://localhost:8000

input_data = JournalInput(

    transcript="I had a great day today. Everything went well.",- **Interactive Docs**: http://localhost:8000/docs

    entities=["work"],

    prosody=Prosody(- **ReDoc**: http://localhost:8000/redoc

        mean_pitch_hz=180.0,

        pitch_var=400.0,# Install dependencies│   ├── app/    "entities": ["work", "presentation"],

        rms_energy=0.05,

        speech_rate_wps=2.5---

    ),

    sentiment=Sentiment(valence=0.7, confidence=0.85)pip install -r requirements.txt

)

## 📚 API Endpoints

result = ai_service.process_journal(input_data)

print(result.model_dump_json(indent=2))│   │   ├── main.py       # Application entry    "prosody": {

```

### Authentication

Run examples:

```bash- `POST /auth/register` - Register new user# Set up environment variables

cd backend

python examples/example_usage.py- `POST /auth/login` - Login and get JWT token

```

- `GET /auth/me` - Get current user profilecp .env.example .env│   │   ├── config.py     # Configuration        "mean_pitch_hz": 180.0,

---



## 🧪 Testing

### Todos (Task Management)# Edit .env with your API keys

```bash

cd backend- `GET /api/todos` - List all todos (with filters)



# Run tests- `POST /api/todos` - Create new todo```│   │   ├── database.py   # Supabase client        "pitch_var": 400.0,

python tests/test_ai_service.py

- `GET /api/todos/{id}` - Get single todo

# Or with pytest

pytest tests/- `PUT /api/todos/{id}` - Update todo

```

- `DELETE /api/todos/{id}` - Delete todo

See `backend/TESTING.md` for API testing guide.

### 2. Configure API Keys│   │   ├── models/       # Pydantic schemas        "rms_energy": 0.05,

---

### Voice & Journaling

## 🔑 Environment Variables

- `POST /voice/journal` - Process journal entry with emotional analysis

Required in `backend/.env`:

- `POST /voice/generate` - Generate speech from text (TTS)

```env

# Supabase- `GET /voice/voices` - List available voice optionsEdit `backend/.env` with your credentials:│   │   ├── services/     # Business logic        "speech_rate_wps": 2.5

SUPABASE_URL=your-supabase-url

SUPABASE_KEY=your-supabase-anon-key



# APIs### News

NEWS_API_KEY=your-newsapi-key

OPENAI_API_KEY=your-openai-key- `GET /news/` - Get personalized news feed

ANTHROPIC_API_KEY=your-anthropic-key  # Optional

- `GET /news/search?q=query` - Search news articles- **Supabase**: Database and authentication│   │   └── api/          # API endpoints    },

# Security

SECRET_KEY=your-jwt-secret-key- `GET /news/recommendations` - Get AI-recommended articles

```

- **NewsAPI**: News articles

### Get API Keys

1. **Supabase** - [supabase.com](https://supabase.com)### Preferences

2. **NewsAPI** - [newsapi.org](https://newsapi.org)

3. **OpenAI** - [openai.com](https://openai.com)- `GET /preferences/` - Get user preferences- **Anthropic**: Claude AI (optional, for future features)│   ├── .env.example      # Environment template    "sentiment": {

4. **Anthropic** - [anthropic.com](https://anthropic.com)

- `PUT /preferences/` - Update user preferences

---

- `POST /preferences/track-interaction` - Track article interaction- **OpenAI**: Text-to-speech

## 🔒 Security & Privacy



- **JWT Authentication** - Secure token-based auth via Supabase

- **Row-Level Security** - Database policies ensure data isolation📖 **Full API Documentation**: Visit http://localhost:8000/docs after starting the server│   └── README.md         # Backend documentation        "valence": 0.7,

- **PII Redaction** - Optional removal of sensitive information

- **Encrypted Storage** - Data encrypted at rest in PostgreSQL

- **Password Hashing** - Secure bcrypt hashing

---### 3. Start the Server

---



## 📄 License

## 🏗️ Project Structure├── examples/             # Usage examples        "confidence": 0.85

MIT License



Copyright (c) 2025 Rahul RR

``````bash

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

unposted-ai-assistant/

---

├── backend/                    # FastAPI backend server# From project root├── tests/                # Unit tests    },

## 📞 Contact & Support

│   ├── app/

**Developer**: Rahul RR  

**GitHub**: [@rahulrr-coder](https://github.com/rahulrr-coder)  │   │   ├── main.py            # Application entry point./start_backend.sh

**Repository**: [unposted-ai-assistant](https://github.com/rahulrr-coder/unposted-ai-assistant)

│   │   ├── config.py          # Environment configuration

**Support**:

- 🐛 [Report issues](https://github.com/rahulrr-coder/unposted-ai-assistant/issues)│   │   ├── database.py        # Supabase client└── requirements.txt      # Python dependencies    "language": "en",

- 📖 [Documentation](backend/README.md)

- 🧪 [Testing guide](backend/TESTING.md)│   │   ├── models/



---│   │   │   └── schemas.py     # Pydantic models# Or from backend directory



**Built for the Arré Voice × AI Hackathon 2025** 🎉│   │   ├── services/


│   │   │   ├── ai_service.py      # Journal processingcd backend```    "privacy": {

│   │   │   ├── news_service.py    # News API integration

│   │   │   ├── voice_service.py   # TTS serviceuvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

│   │   │   └── personalization.py # Recommendations

│   │   └── api/```        "pii_redaction_enabled": False

│   │       ├── auth.py        # Authentication endpoints

│   │       ├── todos.py       # Todo CRUD endpoints

│   │       ├── news.py        # News endpoints

│   │       ├── preferences.py # Preferences endpointsThe API will be available at:## Quick Start    }

│   │       └── voice.py       # Voice & journal endpoints

│   ├── migrations/            # Database migrations- **API**: http://localhost:8000

│   ├── tests/                 # Unit tests

│   ├── examples/              # Usage examples- **Docs**: http://localhost:8000/docs}

│   ├── requirements.txt       # Python dependencies

│   ├── .env.example          # Environment template- **ReDoc**: http://localhost:8000/redoc

│   ├── TESTING.md            # API testing guide

│   └── README.md             # Backend documentation### 1. Clone Repository

├── client/                    # Streamlit UI (coming soon)

├── start_backend.sh          # Backend start script## API Endpoints

└── README.md                 # This file

```result = assistant.process(input_data)



---### Authentication



## 🛠️ Tech Stack- `POST /auth/register` - Register new user```bashprint(result)  # Returns JSON string



### Backend- `POST /auth/login` - Login and get JWT token

- **FastAPI**: Modern Python web framework with automatic API docs

- **Pydantic v2**: Data validation and settings management- `GET /auth/me` - Get current usergit clone https://github.com/rahulrr-coder/unposted-ai-assistant.git```

- **Supabase**: PostgreSQL database with built-in authentication

- **NewsAPI**: News aggregation and search

- **OpenAI**: Text-to-speech (TTS) voice generation

- **Anthropic Claude 3.5 Sonnet**: AI analysis (planned)### Voice & Journalingcd unposted-ai-assistant



### Planned Client- `POST /voice/journal` - Process journal entry

- **Streamlit**: Interactive web UI

- **Audio Recording**: Browser-based voice capture- `POST /voice/generate` - Generate speech from text```## Input Schema

- **Real-time Processing**: Live emotional analysis

- `GET /voice/voices` - List available voices

---



## 💻 Usage Examples

### News

### Process a Journal Entry

- `GET /news/` - Get personalized news feed### 2. Create Virtual Environment```python

```python

from backend.app.services.ai_service import ai_service- `GET /news/search?q=query` - Search news

from backend.app.models.schemas import JournalInput, Prosody, Sentiment, Privacy

- `GET /news/recommendations` - Get AI recommendations{

input_data = JournalInput(

    transcript="I had a great day today. Everything went well.",

    entities=["work"],

    prosody=Prosody(### Preferences```bash    "transcript": str,              # 60-90 seconds of speech (required)

        mean_pitch_hz=180.0,

        pitch_var=400.0,- `GET /preferences/` - Get user preferences

        rms_energy=0.05,

        speech_rate_wps=2.5- `PUT /preferences/` - Update preferencespython3 -m venv .venv    "entities": List[str],          # Key people/events (optional, default: [])

    ),

    sentiment=Sentiment(- `POST /preferences/track-interaction` - Track article interaction

        valence=0.7,

        confidence=0.85source .venv/bin/activate  # On Linux/Mac    "prosody": {                    # Acoustic features (required)

    ),

    privacy=Privacy(pii_redaction_enabled=False)## Running Examples

)

```        "mean_pitch_hz": float,     # Average pitch in Hz

result = ai_service.process_journal(input_data)

print(result.model_dump_json(indent=2))```bash

```

cd backend        "pitch_var": float,         # Pitch variance

### Run Examples

```bashpython examples/example_usage.py

cd backend

python examples/example_usage.py```### 3. Install Dependencies        "rms_energy": float,        # RMS energy level

```



---

## Running Tests        "speech_rate_wps": float    # Words per second

## 🧪 Testing



### Run Tests

```bash```bash```bash    },

cd backend

python tests/test_ai_service.pycd backend



# Or with pytestpython tests/test_ai_service.pypip install -r requirements.txt    "sentiment": {                  # Text sentiment (required)

pytest tests/

```



### Test API with Bruno/Postman# Or with pytest (if installed)```        "valence": float,           # -1 (negative) to 1 (positive)

See `backend/TESTING.md` for comprehensive API testing guide including:

- Authentication flowpytest tests/

- CRUD operations for todos

- News feed testing```        "confidence": float         # 0 to 1

- Voice synthesis testing



---

## Tech Stack### 4. Configure Environment    },

## 🔑 Environment Variables



Required API keys in `backend/.env`:

### Backend    "language": str,                # Language code (optional, default: "en")

```env

# Supabase (Database & Auth)- **FastAPI**: Modern Python web framework

SUPABASE_URL=your-supabase-url

SUPABASE_KEY=your-supabase-anon-key- **Pydantic**: Data validation```bash    "privacy": {                    # Privacy settings (optional)



# News API- **Supabase**: Database and authentication

NEWS_API_KEY=your-newsapi-key

- **NewsAPI**: News aggregationcp backend/.env.example backend/.env        "pii_redaction_enabled": bool  # default: False

# OpenAI (Text-to-Speech)

OPENAI_API_KEY=your-openai-key- **OpenAI**: Text-to-speech



# Anthropic (AI Processing - Optional)- **Anthropic Claude**: AI analysis (planned)# Edit backend/.env with your API keys    }

ANTHROPIC_API_KEY=your-anthropic-key



# Security

SECRET_KEY=your-jwt-secret-key### Planned Client```}

```

- **Streamlit**: Interactive web UI

### Get API Keys:

1. **Supabase** - [supabase.com](https://supabase.com) - Database and authentication- **Audio recording**: Browser-based voice capture```

2. **NewsAPI** - [newsapi.org](https://newsapi.org) - News articles (100 requests/day free)

3. **OpenAI** - [openai.com](https://openai.com) - Text-to-speech- **Real-time processing**: Live emotional analysis

4. **Anthropic** - [anthropic.com](https://anthropic.com) - Claude 3.5 Sonnet (optional)

### 5. Start Backend Server

---

## Environment Variables

## 🎭 Emotion Labels

## Output Schema

The AI maps emotions on a 2D space (valence × arousal):

See `backend/.env.example` for all required variables:

| Label | Valence | Arousal | Description |

|-------|---------|---------|-------------|```bash

| `calm content` | Positive | Low | Peaceful, satisfied |

| `calm sad` | Negative | Low | Melancholy, withdrawn |```env

| `neutral` | ~0 | ~0 | Balanced, neither positive nor negative |

| `tense worried` | Neutral/Negative | High | Anxious, concerned |# Core./start_backend.sh```json

| `tense angry` | Negative | High | Frustrated, irritated |

| `energized hopeful` | Positive | High | Excited, optimistic |SUPABASE_URL=your-supabase-url

| `energized anxious` | Neutral | High | Restless, on edge |

SUPABASE_KEY=your-supabase-key```{

---

NEWS_API_KEY=your-newsapi-key

## 🔒 Privacy & Ethics

OPENAI_API_KEY=your-openai-key    "bullets": [

- **Non-judgmental**: No clinical diagnosis or prescriptive advice

- **Privacy-first**: Optional PII redaction for sensitive informationANTHROPIC_API_KEY=your-anthropic-key

- **Grounded**: All reflections based on actual transcript content

- **Empathetic**: Supportive, warm tone without clichésThe API will be available at:        "First-person reflection (≤110 chars)",

- **Secure**: JWT authentication, encrypted storage, RLS policies

# Security

---

SECRET_KEY=your-jwt-secret-key- **API**: http://localhost:8000        "First-person reflection (≤110 chars)",

## 🗺️ Roadmap

```

- [x] Backend API with FastAPI

- [x] AI journaling service with emotion analysis- **Docs**: http://localhost:8000/docs        "First-person reflection (≤110 chars)"

- [x] News integration with personalization

- [x] Voice synthesis (TTS)## Development Roadmap

- [x] User authentication with Supabase

- [x] Todo/task management endpoints- **ReDoc**: http://localhost:8000/redoc    ],

- [ ] Streamlit web UI

- [ ] Audio recording in browser- [x] Backend API with FastAPI

- [ ] Real-time emotion visualization

- [ ] Historical journal analytics- [x] AI journaling service    "emotion": {

- [ ] Multi-language support

- [ ] Mobile app (future)- [x] News integration

- [ ] Calendar integration

- [x] Voice synthesis## API Keys Required        "valence": 0.7,              // -1 to 1

---

- [x] User authentication

## 🤝 Contributing

- [ ] Streamlit client UI        "arousal": 0.45,             // -1 to 1

Contributions are welcome! Please ensure:

- Type hints for all functions- [ ] Audio recording in browser

- Pydantic models for data validation

- Tests for new features- [ ] Real-time emotion visualizationYou'll need API keys from:        "label": "energized hopeful" // See emotion labels below

- Clear documentation

- [ ] Mobile app (future)

### Development Workflow

```bash    },

# Fork the repo

git clone https://github.com/YOUR_USERNAME/unposted-ai-assistant.git## Contributing



# Create a feature branch1. **Supabase** - Database and authentication    "next_prompt": "What momentum can you carry into tomorrow?" // ≤120 chars

git checkout -b feature/amazing-feature

Contributions welcome! Please ensure:

# Make your changes and commit

git commit -m "feat: add amazing feature"- Type hints for all functions   - Sign up: https://supabase.com}



# Push to your fork- Pydantic models for data validation

git push origin feature/amazing-feature

- Tests for new features   - Create a project and copy your URL and anon key```

# Open a Pull Request

```- Clear documentation



---



## 📄 License## License



MIT License - Feel free to use and modify for your projects.2. **NewsAPI** - News articles## Emotion Labels



---MIT License - Feel free to use and modify for your projects.



## 💬 Support   - Sign up: https://newsapi.org



For issues or questions:## Support

- 🐛 Open an issue on [GitHub](https://github.com/rahulrr-coder/unposted-ai-assistant/issues)

- 📖 Check the [documentation](backend/README.md)   - Free tier: 100 requests/day- `calm content` - Low arousal, positive valence

- 🧪 See [testing guide](backend/TESTING.md)

For issues or questions, please open an issue on the repository.

---

- `calm sad` - Low arousal, negative valence

## 🙏 Acknowledgments

---

Built with ❤️ for the **Arré Voice × AI Hackathon 2025**

3. **Anthropic** - Claude for AI processing- `tense worried` - High arousal, neutral/negative valence

Special thanks to:

- Arré for hosting the hackathonBuilt with ❤️ for the Arré Voice × AI Hackathon

- Anthropic for Claude AI

- OpenAI for TTS capabilities   - Sign up: https://anthropic.com- `tense angry` - High arousal, negative valence

- Supabase for the backend infrastructure

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
