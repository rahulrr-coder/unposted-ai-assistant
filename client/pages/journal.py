"""
Voice journaling page - Functional with backend integration
"""
import streamlit as st
from utils.api_client import APIClient
import base64

st.set_page_config(
    page_title="Speak. Reflect. Grow. - Unposted",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'recording_state' not in st.session_state:
    st.session_state.recording_state = 'idle'  # idle, recording, processing, done
if 'audio_data' not in st.session_state:
    st.session_state.audio_data = None
if 'journal_result' not in st.session_state:
    st.session_state.journal_result = None

# Custom CSS for the exact design
st.markdown("""
<style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Hide all Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Light gray background */
    .stApp {
        background-color: #F5F5F5 !important;
    }
    
    .main {
        background-color: #F5F5F5 !important;
    }
    
    /* Center everything */
    .block-container {
        padding-top: 5rem !important;
        padding-bottom: 5rem !important;
        max-width: 900px !important;
    }
    
    /* Heading - Teal color */
    h1 {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        color: #20AD96 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
        letter-spacing: -0.02em !important;
    }
    
    /* Subtitle - Gray color */
    .subtitle {
        font-size: 1.125rem !important;
        color: #6B7280 !important;
        text-align: center !important;
        margin-bottom: 3rem !important;
        line-height: 1.6 !important;
    }
    
    /* Card styling */
    .recorder-card {
        background: linear-gradient(135deg, #E8E8E8 0%, #D3D3D3 100%) !important;
        border-radius: 24px !important;
        padding: 4rem 6rem !important;
        text-align: center !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07) !important;
        display: inline-block !important;
        margin: 0 auto !important;
    }
    
    /* Microphone icon */
    .mic-icon {
        font-size: 5rem !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
    }
    
    /* Record button */
    .stButton {
        text-align: center !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    .stButton > button {
        background-color: #2D3E4E !important;
        color: white !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 0.75rem 2.5rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(45, 62, 78, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #1F2D3A !important;
        box-shadow: 0 6px 16px rgba(45, 62, 78, 0.35) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Recording state */
    .recording-indicator {
        color: #EF4444;
        font-weight: 600;
        text-align: center;
        margin-top: 1rem;
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Results styling */
    .journal-results {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    .emotion-badge {
        display: inline-block;
        background: #20AD96;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main heading
st.title("Speak. Reflect. Grow.")

# Subtitle
st.markdown(
    '<p class="subtitle">Your thoughts deserve to be heard — not judged. Record freely,<br>'
    'and let AI turn your voice into calm, clear reflections.</p>',
    unsafe_allow_html=True
)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Recorder card
st.markdown('<div class="recorder-card">', unsafe_allow_html=True)

# Microphone icon
st.markdown('<div class="mic-icon">🎙️</div>', unsafe_allow_html=True)

# Recording controls based on state
if st.session_state.recording_state == 'idle':
    if st.button("● Record", key="record_btn", type="primary"):
        st.session_state.recording_state = 'recording'
        st.rerun()

elif st.session_state.recording_state == 'recording':
    st.markdown('<p class="recording-indicator">🔴 Recording in progress...</p>', unsafe_allow_html=True)
    
    # Audio input
    audio_bytes = st.audio_input("Speak your thoughts")
    
    if audio_bytes is not None:
        st.session_state.audio_data = audio_bytes
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬛ Stop", key="stop_btn"):
                st.session_state.recording_state = 'idle'
                st.session_state.audio_data = None
                st.rerun()
        with col2:
            if st.button("📤 Process", key="process_btn", type="primary"):
                st.session_state.recording_state = 'processing'
                st.rerun()

elif st.session_state.recording_state == 'processing':
    with st.spinner("Processing your journal entry..."):
        try:
            # Get audio data
            if st.session_state.audio_data is not None:
                # Convert audio to base64
                audio_bytes = st.session_state.audio_data
                audio_b64 = base64.b64encode(audio_bytes.read()).decode()
            
            # Call backend API
            api_client = APIClient()
            
            # For demo purposes, we'll create a mock journal input
            # In production, you would use speech-to-text first
            journal_data = {
                "transcript": "This is a test journal entry from voice recording.",
                "prosody": {
                    "speaking_rate": 1.0,
                    "pitch_variance": 0.5,
                    "volume": 0.8
                },
                "sentiment": {
                    "polarity": 0.5,
                    "subjectivity": 0.6
                }
            }
            
            # Process journal
            result = api_client.process_journal(journal_data)
            st.session_state.journal_result = result
            st.session_state.recording_state = 'done'
            st.rerun()
            
        except Exception as e:
            st.error(f"Error processing journal: {str(e)}")
            st.info("💡 Note: Make sure the backend server is running on http://localhost:8000")
            st.session_state.recording_state = 'idle'

elif st.session_state.recording_state == 'done':
    st.success("✅ Journal processed successfully!")
    
    if st.button("🎙️ Record Another", key="new_record_btn"):
        st.session_state.recording_state = 'idle'
        st.session_state.audio_data = None
        st.session_state.journal_result = None
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Display results if available
if st.session_state.journal_result:
    st.markdown('<div class="journal-results">', unsafe_allow_html=True)
    
    st.subheader("📝 Your Journal Insights")
    
    result = st.session_state.journal_result
    
    # Emotion
    if 'emotion' in result:
        emotion = result['emotion']
        st.markdown(f'<div class="emotion-badge">Emotion: {emotion.get("label", "Unknown")}</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Valence", f"{emotion.get('valence', 0):.2f}")
        with col2:
            st.metric("Arousal", f"{emotion.get('arousal', 0):.2f}")
    
    # Bullet points
    if 'bullets' in result:
        st.markdown("### Key Takeaways")
        for bullet in result['bullets']:
            st.markdown(f"• {bullet}")
    
    # Next prompt
    if 'next_prompt' in result:
        st.markdown("### 💭 Reflection Prompt")
        st.info(result['next_prompt'])
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main function"""
    pass

if __name__ == "__main__":
    main()
