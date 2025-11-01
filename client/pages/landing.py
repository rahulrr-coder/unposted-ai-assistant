"""
Landing page with login
"""
import streamlit as st

st.set_page_config(
    page_title="Unposted AI Assistant", 
    page_icon="🎙️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for landing page
st.markdown("""
<style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Light background */
    .stApp {
        background-color: #f5f5f5;
    }
    
    .main {
        background-color: #f5f5f5;
    }
    
    /* Title styling */
    .landing-title {
        font-size: 3rem;
        font-weight: 700;
        color: #2D9B9B;
        text-align: center;
        margin-top: 5rem;
        margin-bottom: 1rem;
    }
    
    /* Subtitle */
    .landing-subtitle {
        font-size: 1.2rem;
        color: #666666;
        text-align: center;
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    /* Login button */
    .stButton > button {
        background-color: #2D9B9B !important;
        color: white !important;
        border-radius: 24px !important;
        padding: 1rem 3rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(45, 155, 155, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #258080 !important;
        box-shadow: 0 6px 16px rgba(45, 155, 155, 0.4) !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Landing page."""
    
    # Title and subtitle
    st.markdown('<h1 class="landing-title">Speak. Reflect. Grow.</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="landing-subtitle">Your thoughts deserve to be heard — not judged.<br>'
        'Record freely, and let AI turn your voice into calm, clear reflections.</p>',
        unsafe_allow_html=True
    )
    
    # Login button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Login", key="login_btn", use_container_width=True):
            st.switch_page("pages/journal.py")

if __name__ == "__main__":
    main()
