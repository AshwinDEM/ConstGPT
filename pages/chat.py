import streamlit as st
import random

st.set_page_config(page_title="Chat", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "chat"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_user" not in st.session_state:
    st.session_state.chat_user = ""

# If a user logs out, clear the chat history
# Otherwise, the chat history will be retained between users
if st.session_state.username != st.session_state.chat_user:
    st.session_state.chat_history = []

st.session_state.chat_user = st.session_state.username

st.session_state.num_messages = 0

def chat():
    try:
        if not st.session_state.logged_in:
            st.write("Please log in to access the chat.")
            if st.button("Back to Home"):
                st.session_state.page = "home"
                st.switch_page("main.py")
            
    except Exception as e:
        pass

    if st.session_state.page == "chat":
        st.title(f"AI Bot")

        st.header("Chat History")
        for chat_message in st.session_state.chat_history:
            pass
            # st.write(chat_message)

        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                pass
                st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.chat_message("user").markdown(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            response = f"{prompt}"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "home"
            st.rerun()
    else:
        st.switch_page("main.py")

if __name__ == "__main__":
    chat()
