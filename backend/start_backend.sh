#!/bin/bash

# Start the Unposted AI Assistant Backend Server

echo "🚀 Starting Unposted AI Assistant Backend..."

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env not found!"
    echo "📝 Please copy .env.example to .env and configure your API keys"
    echo ""
    echo "Run: cp .env.example .env"
    echo "Then edit .env with your actual API keys"
    exit 1
fi

# Activate virtual environment from parent directory
if [ -d "../.venv" ]; then
    source ../.venv/bin/activate
else
    echo "❌ Virtual environment not found at ../.venv"
    echo "Please run from project root:"
    echo "  python3 -m venv .venv"
    echo "  source .venv/bin/activate"
    echo "  pip install -r backend/requirements.txt"
    exit 1
fi

# Start the FastAPI server
echo "✅ Starting server on http://0.0.0.0:8000"
echo "📚 API Documentation: http://localhost:8000/docs"
echo "📖 ReDoc: http://localhost:8000/redoc"
echo ""

cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
