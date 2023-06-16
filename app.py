import os
import langchain
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI object with your model name and API key
chat = langchain.chat_models.ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)

# Create Streamlit app with a text input and button
st.title("Chat with ChatGPT")
user_input = st.text_input("Enter your message")
if st.button("Send"):
    # Create a list of messages and append user input as a HumanMessage object
    messages = []
    usr_msg = langchain.schema.HumanMessage(content=user_input)
    messages.append(usr_msg)

    # Call the chat method to get AI response as an AIMessage object
    ai_msg = chat(messages)

    # Display AI response on the Streamlit app
    st.write(ai_msg.content)

    # Append AI response to messages list for future reference
    messages.append(ai_msg)
