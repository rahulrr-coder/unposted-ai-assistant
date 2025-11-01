"""
Registration page
"""
import streamlit as st

st.set_page_config(page_title="Register - Unposted", page_icon="📝")

def main():
    st.title("📝 Register")
    st.write("Create your Unposted AI Assistant account")
    
    # Registration form placeholder
    with st.form("register_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")
        
        if submit:
            st.info("Registration functionality will be implemented here")
    
    st.divider()
    st.write("Already have an account?")
    if st.button("Login"):
        st.switch_page("pages/login.py")

if __name__ == "__main__":
    main()
