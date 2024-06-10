import streamlit as st

def login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if username == 'user' and password == 'pass':  # Replace with secure auth
                st.session_state.logged_in = True
            else:
                st.error("Invalid username or password")
        return False

def logout():
    st.session_state.logged_in = False
    st.experimental_rerun()
