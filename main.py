import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="GPTFeed", layout="centered")

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Custom CSS to center the title and add transparency to "ruct"
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
    # Centered title with transparency for "ruct"
    st.markdown(
        """
        <div class="centered-title">
            <span>Const<span class="transparent-ruct">ruct</span></span>
            <span>GPT</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
    # st.subheader("Ashwin")

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






# import streamlit as st

# # Set up Streamlit page configuration
# st.set_page_config(page_title="GPTFeed", layout="centered")

# # Initialize session state variables
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.username = ""

# def main():
#     st.title("Hello World")
#     st.subheader("Ashwin")

#     if st.button("Login/Register"):
#         st.session_state.page = "login_register"
#         st.session_state.registering = False
#         st.rerun()

# if st.session_state.page == "home":
#     main()
# elif st.session_state.page == "login_register":
#     st.switch_page("pages/login_register.py")
# elif st.session_state.page == "chat":
#     st.switch_page("pages/chat.py")
# else:
#     st.error("Invalid page state")



# import streamlit as st

# # Set up Streamlit page configuration
# st.set_page_config(page_title="ConstGPT", layout="centered")

# # CSS for styling the header and subtitle
# css = """
#     <style>
#     .centered-title {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         height: 100vh;
#         flex-direction: column;
#     }
#     .title {
#         font-size: 4rem;
#         font-weight: bold;
#         color: #333;
#     }
#     .subtitle {
#         font-size: 2rem;
#         color: #666;
#     }
#     .button-container {
#         margin-top: 2rem;
#     }
#     .button {
#         background-color: #007bff;
#         color: white;
#         border: none;
#         padding: 10px 20px;
#         font-size: 1.2rem;
#         border-radius: 5px;
#         cursor: pointer;
#         transition: background-color 0.3s ease;
#         margin: 0.5rem;
#     }
#     .button:hover {
#         background-color: #0056b3;
#     }
#     </style>
# """

# # Initialize session state variables
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.username = ""

# def main():
#     st.markdown(css, unsafe_allow_html=True)
    
#     st.markdown('<div class="centered-title">', unsafe_allow_html=True)
#     st.markdown('<div class="title">Hello World</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtitle">Ashwin</div>', unsafe_allow_html=True)
    
#     if st.button("Login/Register"):
#         st.session_state.page = "login_register"
#         st.session_state.registering = False
#         st.rerun()
    
#     st.markdown('</div>', unsafe_allow_html=True)

# if st.session_state.page == "home":
#     main()
# elif st.session_state.page == "login_register":
#     st.switch_page("pages/login_register.py")
# elif st.session_state.page == "chat":
#     st.switch_page("pages/chat.py")
# else:
#     st.error("Invalid page state")
