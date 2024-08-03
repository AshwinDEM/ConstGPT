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
def login_register():
    st.title("Login / Register")

    # Dropdown to select Login or Register
    action = st.selectbox("Select Action", ["Login", "Register"])

    if action == "Register":
        st.session_state.registering = True
    else:
        st.session_state.registering = False

    if not st.session_state.logged_in:
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
                    try:
                        st.experimental_rerun()
                    except AttributeError as e:
                        pass

                    
        else:
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if login(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.page = "chat"
                    st.rerun()
                else:
                    st.error("Invalid username or password")
                
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    login_register()
