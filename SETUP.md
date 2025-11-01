# Quick Setup Guide

Follow these steps to get the backend running:

## 1. Setup Environment

```bash
# Create virtual environment in backend
cd backend
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys:
# - SUPABASE_URL and SUPABASE_KEY (get from supabase.com)
# - NEWS_API_KEY (get from newsapi.org)
# - OPENAI_API_KEY (get from platform.openai.com)
# - ANTHROPIC_API_KEY (get from console.anthropic.com)
# - SECRET_KEY (generate a random string for JWT)
```

## 4. Start the Server

```bash
# From project root
cd ..
./start_backend.sh

# OR from backend directory
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 5. Test the API

Open your browser to:
- API Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

## 6. Run Examples

```bash
cd backend
python examples/example_usage.py
```

## 7. Run Tests

```bash
cd backend
python tests/test_ai_service.py
```

## Need Help?

- Check backend/README.md for detailed documentation
- API endpoints are documented at /docs when server is running
- Examples in backend/examples/ show usage patterns

## Next Steps

Once backend is running:
1. Test API endpoints using the docs UI
2. Wait for design team to complete UI mockups
3. Build Streamlit client in client/ directory
