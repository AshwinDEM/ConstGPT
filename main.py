import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Multi-Page Chat App", layout="centered")

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "home"

def main():
    st.title("Hello World")
    st.subheader("Ashwin")
    
    # col1, col2 = st.columns(2)
    
    # with col1:
    #     if st.button("Login"):
    #         st.session_state.page = "login_register"
    #         st.session_state.registering = False
    #         st.rerun()
    
    # with col2:
    #     if st.button("Register"):
    #         st.session_state.page = "login_register"
    #         st.session_state.registering = True
    #         st.rerun()

    if st.button("Login/Register"):
        st.session_state.page = "login_register"
        st.session_state.registering = False
        st.rerun()

if st.session_state.page == "home":
    main()
elif st.session_state.page == "login_register":
    from pages import login_register
    login_register.login_register()
elif st.session_state.page == "chat":
    from pages import chat
    chat.chat()
