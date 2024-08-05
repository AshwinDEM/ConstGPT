import streamlit as st

st.set_page_config(page_title="ConstGPT", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

st.markdown(
    """
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh;
        font-size: 5em;
        flex-direction: column;
        font-weight: bold;
        
    }
    .transparent-ruct {
        opacity: 0.3;
    }
    .stButton button {
        background-color: #4CAF50; /* Green */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown(
        """
        <div class="centered-title">
            <span>Const<span class="transparent-ruct">ruct</span></span>
            <span>GPT</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

    button = st.button("Login/Register")
    if button:
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
