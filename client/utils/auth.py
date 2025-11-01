"""
Authentication utilities
"""
import streamlit as st
from typing import Optional


def check_authentication() -> bool:
    """Check if user is authenticated."""
    return st.session_state.get("auth_token") is not None


def get_auth_token() -> Optional[str]:
    """Get the current authentication token."""
    return st.session_state.get("auth_token")


def set_auth_token(token: str):
    """Set the authentication token."""
    st.session_state.auth_token = token


def clear_auth():
    """Clear authentication data."""
    if "auth_token" in st.session_state:
        del st.session_state.auth_token
    if "user_data" in st.session_state:
        del st.session_state.user_data


def require_auth(func):
    """Decorator to require authentication for a page."""
    def wrapper(*args, **kwargs):
        if not check_authentication():
            st.warning("Please login to access this page")
            st.switch_page("pages/login.py")
            return
        return func(*args, **kwargs)
    return wrapper
