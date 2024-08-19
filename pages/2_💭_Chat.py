import streamlit as st
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, logging
import requests
from dotenv import load_dotenv
import os
import subprocess
import torch

st.set_page_config(page_title="Chat", layout="centered")

# model = AutoModelForCausalLM.from_pretrained("models/llama/llama-2-7b-sciq1", device_map = 'auto')
# tokenizer = AutoTokenizer.from_pretrained("models/llama/llama-2-7b-sciq1")

# def get_response(prompt, length, variation, conciseness):
#     input_ids = tokenizer.encode(prompt, return_tensors="pt")
#     output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=50256)
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response


def get_pipe():
    model_id = "./models/llama-half/llama-half"
    tokenizer = "./models/llama-half/llama-half"
    logging.set_verbosity_error()
    return transformers.pipeline("text-generation", model=model_id, tokenizer = tokenizer, device_map="auto", max_length=75)

if st.session_state.pipe == 0:
    st.session_state.pipe = get_pipe()

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
    st.session_state.chat_history.append({"role": "user", "content": "What is your name?"})
    st.session_state.chat_history.append({"role": "assistant", "content": "I do not have a name."})
    st.session_state.chat_history.append({"role": "user", "content": "What is the boiling point of water?"})
    st.session_state.chat_history.append({"role": "assistant", "content": """ What is the boiling point of water? 
    Boiling point of water. (credit: modification of work by “Dave”/Flickr).
    The boiling point of water is 100°C. The boiling point of water is the temperature at which the water changes from a liquid to a gas. The boiling point of water is 100°C. The boiling point of water is the temperature at which the water changes from a liquid to a gas"""})
    st.session_state.chat_history.append({"role": "user", "content": "What is most harmless type of radiation?"})
    st.session_state.chat_history.append({"role": "assistant", "content": """ What is the most harmless type of radiation? [/INST]\n[INST] What is the most harmless type of radiation?\nA) Cosmic ray"""})
    st.session_state.chat_history.append({"role": "user", "content": "Solute potential is also called osmotic potential because solutes affect the direction of what?"})
    st.session_state.chat_history.append({"role": "assistant", "content": "' Solute potential is also called osmotic potential because solutes affect the direction of what? \n12.  The solute potential is the driving force for solute diffusion. "})

st.session_state.chat_user = st.session_state.username

st.session_state.num_messages = 0

# Replace with your actual server URL
# FLASK_SERVER_URL = "http://localhost:5000"

# def get_response_from_flask(question):
#     response = requests.post(f"{FLASK_SERVER_URL}/ask", json={"question": question})
#     return response.json().get("answer", "No answer received")

def chat():
    try:
        if not st.session_state.logged_in:
            st.write("Please log in to access the chat.")
            if st.button("Back to Home"):
                st.session_state.page = "home"
                st.switch_page("main.py")
            return

    except Exception as e:
        st.error(f"An error occurred: {e}")

    if st.session_state.page == "chat":
        col1, col2 = st.columns([3, 1])

        slider1 = slider2 = slider3 = 0
        with col2:
            st.header("Settings")
            slider1 = st.slider("Length", 0, 10, 5, 1)
            slider2 = st.slider("Conciseness", 0, 10, 5, 1)
            slider3 = st.slider("Variation", 0, 10, 5, 1)

        with col1:
            st.title("AI Bot")
            st.header("Chat History")
            for message in st.session_state.chat_history:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("What is up?"):
                st.chat_message("user").markdown(prompt)
                st.session_state.chat_history.append({"role": "user", "content": prompt})

                with st.spinner("Awaiting response..."):
                    if st.session_state.pipe == 0:
                        st.session_state.pipe = get_pipe()
                    response = st.session_state.pipe(prompt, max_length=slider1*10, num_return_sequences=1, do_sample=True, temperature=5/slider2, top_k=slider3*10)[0]["generated_text"]
                    # response = st.session_state.pipe(prompt, max_length = 100)[0]["generated_text"]
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
