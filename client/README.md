# Streamlit Client

Streamlit-based frontend for the Unposted AI Journaling Assistant.

## 📁 Folder Structure

```
client/
├── app.py                      # Main application entry point
├── pages/                      # Streamlit pages
│   ├── login.py               # Login page
│   ├── register.py            # Registration page
│   ├── journal.py             # Voice journaling page
│   ├── news.py                # News feed page
│   ├── todos.py               # Todo management page
│   └── preferences.py         # User preferences page
├── components/                 # Reusable UI components
│   ├── __init__.py
│   └── ui_components.py       # Todo cards, news cards, emotion widgets
├── utils/                      # Utility functions
│   ├── __init__.py
│   ├── api_client.py          # Backend API client
│   └── auth.py                # Authentication helpers
├── styles/                     # Custom CSS
│   └── custom.css             # Theme and styling
├── assets/                     # Images, icons, etc.
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Backend API running on http://localhost:8000

### Installation

1. **Install dependencies**:
```bash
cd client
pip install -r requirements.txt
```

2. **Configure environment**:
```bash
cp .env.example .env
# Edit .env if needed
```

3. **Run the app**:
```bash
streamlit run app.py
```

The app will open at http://localhost:8501

## 📄 Pages

- **Home** (`app.py`) - Dashboard and navigation
- **Login** (`pages/login.py`) - User authentication
- **Register** (`pages/register.py`) - New user registration
- **Journal** (`pages/journal.py`) - Voice journaling with AI analysis
- **News** (`pages/news.py`) - Personalized news feed
- **Todos** (`pages/todos.py`) - Task management
- **Preferences** (`pages/preferences.py`) - User settings

## 🎨 Components

Reusable UI components in `components/ui_components.py`:
- `render_todo_card()` - Todo item display
- `render_news_card()` - News article card
- `render_emotion_widget()` - Emotion analysis display

## 🔧 Utils

- **API Client** (`utils/api_client.py`) - Backend communication
- **Auth** (`utils/auth.py`) - Authentication helpers

## 📝 Notes

- UI implementation pending design review
- Ready for custom component integration
- Folder structure follows Streamlit best practices
