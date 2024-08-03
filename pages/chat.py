import streamlit as st
import random

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.session_state.num_messages = 0

# Streamlit app
def chat():
    try:
        if not st.session_state.logged_in:
            st.write("Please log in to access the chat.")
            if st.button("Back to Home"):
                st.session_state.page = "home"
                st.switch_page("main.py")
                # st.rerun() Code is unreachable
            st.stop()
    except Exception as e:
        pass

    st.title(f"Chat with AI")

    # Display chat history
    st.header("Chat History")
    for chat_message in st.session_state.chat_history:
        st.write(chat_message)

    # Input message and send button
    message = st.text_input("Your Message")
    
    if st.button("Send"):
        if message:
            # Append the user's message to the chat history
            st.session_state.chat_history.append(f"{st.session_state.num_messages}: {""}")
            st.session_state.chat_history.append(f"{st.session_state.username}: {message}")
            # Respond with a random number and append to the chat history
            response = random.randint(1, 100)
            st.session_state.chat_history.append(f"Response: {response}")
            st.rerun()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    chat()
