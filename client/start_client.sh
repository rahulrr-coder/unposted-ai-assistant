#!/bin/bash

# Unposted AI Assistant - Streamlit Client Startup Script

echo "🎙️ Starting Unposted AI Assistant Client..."

# Check if virtual environment exists
if [ ! -d "../.venv" ]; then
    echo "❌ Virtual environment not found. Please run from project root:"
    echo "   python3 -m venv .venv"
    echo "   source .venv/bin/activate"
    exit 1
fi

# Activate virtual environment
source ../.venv/bin/activate

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found, using defaults"
    cp .env.example .env
fi

# Start Streamlit
echo "✅ Starting Streamlit on http://localhost:8501"
streamlit run app.py
