import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


# API Keyをセット
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDOkxdeIGiGBWnn93c-znm89dLZ5yf0flM"

#genai.configure(api_key=st.secrets["gemini_key"])

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.text_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream the response to the chat using `st.write_stream`, then store it in 
    # session state.
    with st.chat_message("assistant"):
        ai_msg = llm.invoke(st.session_state.messages)
    st.session_state.messages.append(("assistant",ai_msg.content))