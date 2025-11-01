"""
API Client for backend communication
"""
import requests
from typing import Optional, Dict, Any
import streamlit as st


class APIClient:
    """Client for communicating with the FastAPI backend."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.token: Optional[str] = None
    
    def set_token(self, token: str):
        """Set the authentication token."""
        self.token = token
        st.session_state.auth_token = token
    
    def get_headers(self) -> Dict[str, str]:
        """Get headers with authentication token."""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers
    
    # Authentication
    def register(self, email: str, password: str, full_name: str) -> Dict[str, Any]:
        """Register a new user."""
        response = requests.post(
            f"{self.base_url}/auth/register",
            json={"email": email, "password": password, "full_name": full_name}
        )
        response.raise_for_status()
        return response.json()
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login and get access token."""
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"email": email, "password": password}
        )
        response.raise_for_status()
        data = response.json()
        self.set_token(data.get("access_token"))
        return data
    
    def get_current_user(self) -> Dict[str, Any]:
        """Get current user profile."""
        response = requests.get(
            f"{self.base_url}/auth/me",
            headers=self.get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    # Todos
    def get_todos(self, status: Optional[str] = None, priority: Optional[str] = None):
        """Get all todos."""
        params = {}
        if status:
            params["status"] = status
        if priority:
            params["priority"] = priority
        
        response = requests.get(
            f"{self.base_url}/api/todos",
            headers=self.get_headers(),
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def create_todo(self, title: str, description: str = "", status: str = "pending", priority: str = "medium"):
        """Create a new todo."""
        response = requests.post(
            f"{self.base_url}/api/todos",
            headers=self.get_headers(),
            json={"title": title, "description": description, "status": status, "priority": priority}
        )
        response.raise_for_status()
        return response.json()
    
    def update_todo(self, todo_id: int, **kwargs):
        """Update a todo."""
        response = requests.put(
            f"{self.base_url}/api/todos/{todo_id}",
            headers=self.get_headers(),
            json=kwargs
        )
        response.raise_for_status()
        return response.json()
    
    def delete_todo(self, todo_id: int):
        """Delete a todo."""
        response = requests.delete(
            f"{self.base_url}/api/todos/{todo_id}",
            headers=self.get_headers()
        )
        response.raise_for_status()
    
    # News
    def get_news(self, category: Optional[str] = None):
        """Get personalized news feed."""
        params = {}
        if category:
            params["category"] = category
        
        response = requests.get(
            f"{self.base_url}/news/",
            headers=self.get_headers(),
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def search_news(self, query: str):
        """Search news articles."""
        response = requests.get(
            f"{self.base_url}/news/search",
            headers=self.get_headers(),
            params={"q": query}
        )
        response.raise_for_status()
        return response.json()
    
    # Voice & Journal
    def process_journal(self, journal_data: Dict[str, Any]):
        """Process a journal entry."""
        response = requests.post(
            f"{self.base_url}/voice/journal",
            headers=self.get_headers(),
            json=journal_data
        )
        response.raise_for_status()
        return response.json()
    
    def generate_speech(self, text: str, voice: str = "alloy"):
        """Generate speech from text."""
        response = requests.post(
            f"{self.base_url}/voice/generate",
            headers=self.get_headers(),
            json={"text": text, "voice": voice}
        )
        response.raise_for_status()
        return response.content
    
    # Preferences
    def get_preferences(self):
        """Get user preferences."""
        response = requests.get(
            f"{self.base_url}/preferences/",
            headers=self.get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    def update_preferences(self, preferences: Dict[str, Any]):
        """Update user preferences."""
        response = requests.put(
            f"{self.base_url}/preferences/",
            headers=self.get_headers(),
            json=preferences
        )
        response.raise_for_status()
        return response.json()
