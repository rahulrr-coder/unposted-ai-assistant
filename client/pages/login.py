"""
Login page
"""
import streamlit as st

st.set_page_config(page_title="Login - Unposted", page_icon="🔐")

def main():
    st.title("🔐 Login")
    st.write("Login to your Unposted AI Assistant account")
    
    # Login form placeholder
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            st.info("Login functionality will be implemented here")
    
    st.divider()
    st.write("Don't have an account?")
    if st.button("Register"):
        st.switch_page("pages/register.py")

if __name__ == "__main__":
    main()
