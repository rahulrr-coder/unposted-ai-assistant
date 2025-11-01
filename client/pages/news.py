"""
News feed page
"""
import streamlit as st

st.set_page_config(page_title="News - Unposted", page_icon="📰", layout="wide")

def main():
    st.title("📰 Personalized News")
    st.write("Stay informed with AI-curated news tailored to your interests")
    
    # News feed placeholder
    st.info("News feed interface will be implemented here")

if __name__ == "__main__":
    main()
