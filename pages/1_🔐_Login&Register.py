import streamlit as st
import pandas as pd
import os
from time import sleep

st.set_page_config(page_title="Login/Register", layout="centered")

USER_FILE_PATH = "./users/users.csv"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.registering = False


def read_users():
    if os.path.exists(USER_FILE_PATH):
        return pd.read_csv(USER_FILE_PATH)
    else:
        return pd.DataFrame(columns=["username", "password"])


def add_user(username, password):
    users_df = read_users()
    new_user = pd.DataFrame({"username": [username], "password": [password]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USER_FILE_PATH, index=False)


def login(username, password):
    users_df = read_users()
    if not users_df.empty:
        user_row = users_df[users_df['username'] == username]
        if not user_row.empty and user_row.iloc[0]['password'] == password:
            return True
    return False


def login_register():
    st.title("Login / Register")

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
                    st.success("Registered successfully! Please log in.")
                    add_user(new_username, new_password)
                    # sleep(2)
                    # st.switch_page("pages/login_register.py")
                    st.session_state.registering = False
                    try:
                        # Despite the fact that this will throw an Exception every time,
                        # (since this is not experimental anymore), however rerun does not work
                        # and switch_page does not work, for some damn reason only for st.success,
                        # works fine for st.error and st.warning, so I have to use the following
                        # workaround to make the page show the success, and then reload, instead
                        # of just reloading the page.
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
                    st.switch_page("pages/2_💭_Chat.py")
                else:
                    st.error("Invalid username or password")
    else:
        st.write(f"Welcome, {st.session_state.username}!")
                
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    login_register()
