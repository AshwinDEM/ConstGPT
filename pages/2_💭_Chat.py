import streamlit as st
from dotenv import load_dotenv
import os
from models.model import load_model, generate_text  # Import the load_model and generate_text functions

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
            return  # Exit early if not logged in

    except Exception as e:
        st.error(f"An error occurred: {e}")

    if st.session_state.page == "chat":
        # Display loading message
        with st.spinner("Loading the model..."):
            tokenizer, model = load_model("gpt2")

        # Create columns
        col1, col2 = st.columns([3, 1])  # Adjust column ratios as needed

        slider1 = slider2 = slider3 = 0
        with col2:
            st.header("Settings")
            slider1 = st.slider("Length", 0, 10, 5, 1)
            slider2 = st.slider("Variation", 0, 10, 5, 1)
            slider3 = st.slider("Conciseness", 0, 10, 5, 1)

        with col1:
            st.title("AI Bot")
            st.header("Chat History")
            for message in st.session_state.chat_history:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("What is up?"):
                st.chat_message("user").markdown(prompt)
                st.session_state.chat_history.append({"role": "user", "content": prompt})

                # Generate a response using the GPT-2 model
                with st.spinner("Awaiting response..."):
                    response = generate_text(tokenizer, model, prompt, max_length=100, temperature=0.7, top_p=0.9, repetition_penalty=1.2)
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()

            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.page = "home"
                st.rerun()
    else:
        st.switch_page("main.py")

if __name__ == "__main__":
    chat()
