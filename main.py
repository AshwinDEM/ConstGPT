import os
import streamlit as st
import pandas as pd

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.users = {}
    st.session_state.registering = False

# User authentication function
def login(username, password):
    # For simplicity, we use hardcoded credentials
    if username in st.session_state.users:
        return st.session_state.users[username] == password
    else:
        return False

def add_user(username, password):
    #st.session_state.users[username] = str(hash(password))
    pass


# Streamlit app
def main():
    st.title("Chat Application")

    # Login section
    if not st.session_state.logged_in and not st.session_state.registering:
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")
        if st.button("Register"):
            st.session_state.registering = True

    # Registration section
    if st.session_state.registering:
        st.header("Register")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            if new_username in st.session_state.users:
                st.error("Username already exists")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            else:
                st.session_state.users[new_username] = new_password
                st.success("Registered successfully! Please log in.")
                st.session_state.registering = False
        if st.button("Back to Login"):
            st.session_state.registering = False

    # Chat interface
    if st.session_state.logged_in:
        st.header("Chat with your friends")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Select which user is currently chatting
        users_list = list(st.session_state.users.keys())
        users_list.remove(st.session_state.username)
        if not users_list:
            st.warning("No other users to chat with")
            return

        chat_with = st.selectbox("Chat with", options=users_list)

        # Input for chat message
        message = st.text_input("Your Message")
        
        if st.button("Send"):
            if message:
                st.session_state.chat_history.append({"user": st.session_state.username, "message": message})
                st.experimental_rerun()  # Rerun the app to clear the input field

        # Display chat history
        st.header("Chat History")
        for chat in st.session_state.chat_history:
            st.write(f"**{chat['user']}**: {chat['message']}")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
