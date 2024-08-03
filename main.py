import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="GPTFeed", layout="centered")

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def main():
    st.title("Hello World")
    st.subheader("Ashwin")

    if st.button("Login/Register"):
        st.session_state.page = "login_register"
        st.session_state.registering = False
        st.rerun()

if st.session_state.page == "home":
    main()
elif st.session_state.page == "login_register":
    st.switch_page("pages/login_register.py")
elif st.session_state.page == "chat":
    st.switch_page("pages/chat.py")
else:
    st.error("Invalid page state")
