"""
Reusable UI components
"""
import streamlit as st


def render_todo_card(todo: dict):
    """Render a todo card component."""
    with st.container():
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{todo.get('title', 'Untitled')}**")
            if todo.get('description'):
                st.caption(todo['description'])
        with col2:
            status = todo.get('status', 'pending')
            status_color = {
                'pending': '🟡',
                'in_progress': '🔵',
                'completed': '🟢',
                'archived': '⚫'
            }.get(status, '⚪')
            st.write(f"{status_color} {status.replace('_', ' ').title()}")
        with col3:
            priority = todo.get('priority', 'medium')
            priority_emoji = {
                'low': '🟢',
                'medium': '🟡',
                'high': '🟠',
                'urgent': '🔴'
            }.get(priority, '⚪')
            st.write(f"{priority_emoji} {priority.title()}")


def render_news_card(article: dict):
    """Render a news article card component."""
    with st.container():
        st.subheader(article.get('title', 'No title'))
        st.caption(article.get('source', {}).get('name', 'Unknown source'))
        if article.get('description'):
            st.write(article['description'])
        if article.get('url'):
            st.link_button("Read more", article['url'])


def render_emotion_widget(emotion: dict):
    """Render emotion analysis widget."""
    st.subheader("Emotional Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Valence", f"{emotion.get('valence', 0):.2f}")
    with col2:
        st.metric("Arousal", f"{emotion.get('arousal', 0):.2f}")
    
    st.info(f"**Emotion**: {emotion.get('label', 'Unknown')}")
