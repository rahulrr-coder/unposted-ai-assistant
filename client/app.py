"""
Unposted AI Assistant - Streamlit Frontend
Main application entry point
"""
import streamlit as st
from utils.api_client import APIClient
from utils.auth import check_authentication

# Page configuration
st.set_page_config(
    page_title="Unposted AI Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application entry point."""
    
    # Check authentication
    if not check_authentication():
        st.switch_page("pages/login.py")
        return
    
    # Main app content
    st.title("🎙️ Unposted AI Assistant")
    st.write("Welcome to your AI-powered journaling assistant")
    
    # Navigation
    st.sidebar.title("Navigation")
    st.sidebar.page_link("app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/journal.py", label="Journal", icon="🎙️")
    st.sidebar.page_link("pages/news.py", label="News", icon="📰")
    st.sidebar.page_link("pages/todos.py", label="Todos", icon="✅")
    st.sidebar.page_link("pages/preferences.py", label="Preferences", icon="⚙️")
    
    # Logout button
    if st.sidebar.button("Logout", type="secondary"):
        st.session_state.clear()
        st.rerun()

if __name__ == "__main__":
    main()
