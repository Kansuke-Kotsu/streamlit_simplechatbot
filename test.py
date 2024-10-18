import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


# Show title and description.
st.title("💬 Simple Chatbot")
st.write("This is a simple chatbot that uses several models to generate responses. ")
st.write("If you want to use OpenAI model, you need to input your API Key.")
st.write("If you want to use OpenSorce LLM model, you can use without your key.")

# API Keyをセット
#os.environ["GOOGLE_API_KEY"] = st.secrets["gemini_key"]
os.environ["GOOGLE_API_KEY"] = "AIzaSyDOkxdeIGiGBWnn93c-znm89dLZ5yf0flM"


# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message[0]):
        st.markdown(message[1])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append(["user", prompt])
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream the response to the chat using `st.write_stream`, then store it in 
    # session state.
    with st.chat_message("assistant"):
        ai_msg = llm.invoke(st.session_state.messages)
        st.markdown(ai_msg.content)
    st.session_state.messages.append(["assistant",ai_msg.content])
