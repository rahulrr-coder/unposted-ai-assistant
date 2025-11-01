"""
Login page
"""
import streamlit as st
from utils.api_client import APIClient
from utils.auth import set_auth_token

st.set_page_config(
    page_title="Login - Unposted AI Assistant", 
    page_icon="🔐",
    layout="centered"
)

# Custom CSS for dark theme matching the screenshot
st.markdown("""
<style>
    /* Dark theme */
    .stApp {
        background-color: #1a1f2e;
    }
    
    /* Main content area */
    .main {
        background-color: #1a1f2e;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title with icon */
    .login-title {
        display: flex;
        align-items: center;
        gap: 1rem;
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle */
    .login-subtitle {
        color: #9ca3af;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Form container */
    .form-container {
        background-color: #0f1419;
        padding: 2.5rem;
        border-radius: 12px;
        max-width: 500px;
        margin: 2rem auto;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #1f2937 !important;
        color: #ffffff !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
    }
    
    /* Labels */
    .stTextInput > label {
        color: #e5e7eb !important;
        font-weight: 500 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Submit button */
    .stButton > button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100% !important;
        margin-top: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #1d4ed8 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4) !important;
    }
    
    /* Info message */
    .stAlert {
        background-color: #1e3a5f !important;
        color: #93c5fd !important;
        border: 1px solid #2563eb !important;
        border-radius: 8px !important;
    }
    
    /* Success message */
    .success-msg {
        background-color: #065f46 !important;
        color: #6ee7b7 !important;
        border: 1px solid #059669 !important;
    }
    
    /* Error message */
    .error-msg {
        background-color: #7f1d1d !important;
        color: #fca5a5 !important;
        border: 1px solid #dc2626 !important;
    }
    
    /* Divider */
    hr {
        border-color: #374151 !important;
        margin: 2rem 0 !important;
    }
    
    /* Bottom text */
    .bottom-text {
        color: #9ca3af;
        text-align: center;
        margin-top: 1.5rem;
    }
    
    /* Register link button */
    .register-btn {
        background-color: transparent !important;
        color: #60a5fa !important;
        border: 1px solid #374151 !important;
        margin-top: 0.5rem !important;
    }
    
    .register-btn:hover {
        background-color: #1f2937 !important;
        border-color: #60a5fa !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f1419;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #9ca3af;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Login page."""
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("### � Navigation")
        st.page_link("pages/login.py", label="�🔐 Login", icon="🔐")
        st.page_link("pages/register.py", label="📝 Register", icon="📝")
    
    # Main content
    st.markdown(
        '<div class="login-title">🔐 Login</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="login-subtitle">Login to your Unposted AI Assistant account</div>',
        unsafe_allow_html=True
    )
    
    # Login form
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            submit = st.form_submit_button("Login", use_container_width=True)
        with col2:
            demo_mode = st.form_submit_button("Demo", use_container_width=True)
        
        if demo_mode:
            # Demo mode - skip authentication
            st.session_state.auth_token = "demo_token_12345"
            st.session_state.user_data = {"email": "demo@unposted.ai", "full_name": "Demo User"}
            st.success("✅ Logged in as Demo User!")
            st.info("Redirecting to journal...")
            st.balloons()
            st.switch_page("pages/journal.py")
        
        if submit:
            # Validation
            if not email or not password:
                st.error("⚠️ Please fill in all fields")
            else:
                # Attempt login
                try:
                    with st.spinner("Logging in..."):
                        api_client = APIClient()
                        response = api_client.login(email=email, password=password)
                        
                        if response and 'access_token' in response:
                            # Store token
                            set_auth_token(response['access_token'])
                            st.session_state.user_data = {"email": email}
                            st.success("✅ Login successful!")
                            st.info("Redirecting to journal...")
                            st.balloons()
                            # Redirect to journal
                            st.switch_page("pages/journal.py")
                        else:
                            st.error("❌ Invalid email or password")
                            
                except Exception as e:
                    st.error(f"❌ Login error: {str(e)}")
                    st.info("💡 Tip: Click 'Demo' button to test without backend connection")
    
    # Don't have account section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="bottom-text">Don\'t have an account?</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Register", key="register_btn", use_container_width=True):
            st.switch_page("pages/register.py")

if __name__ == "__main__":
    main()
