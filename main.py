import streamlit as st
import pandas as pd
import os

# Path to the users CSV file
USER_FILE_PATH = "./users/users.csv"

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.registering = False

# Function to read users from CSV
def read_users():
    if os.path.exists(USER_FILE_PATH):
        return pd.read_csv(USER_FILE_PATH)
    else:
        return pd.DataFrame(columns=["username", "password"])

# Function to add a user to the CSV
def add_user(username, password):
    users_df = read_users()
    new_user = pd.DataFrame({"username": [username], "password": [password]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USER_FILE_PATH, index=False)

# User authentication function
def login(username, password):
    users_df = read_users()
    if not users_df.empty:
        user_row = users_df[users_df['username'] == username]
        if not user_row.empty and user_row.iloc[0]['password'] == password:
            return True
    return False

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
            if new_username in read_users()['username'].values:
                st.error("Username already exists")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            else:
                add_user(new_username, new_password)
                st.success("Registered successfully! Please log in.")
                st.session_state.registering = False
        if st.button("Back to Login"):
            st.session_state.registering = False

    # Chat interface
    if st.session_state.logged_in:
        st.header("Chat with your friends")
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Read users from CSV and prepare the users list
        users_list = read_users()['username'].tolist()
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
