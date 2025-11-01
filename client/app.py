"""
Unposted AI Assistant - Streamlit Frontend
Main application entry point
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unposted AI Assistant",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    """Main application entry point - redirect to landing page."""
    st.switch_page("pages/landing.py")

if __name__ == "__main__":
    main()
