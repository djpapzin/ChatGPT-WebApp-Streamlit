import os
import langchain
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables or input box
api_key = os.getenv("OPENAI_API_KEY")

# Check if the app is running locally or on Streamlit Cloud
is_local = streamlit.config.get_option("server.address") == "localhost"

# If the app is running locally and the API key is not found, raise an exception
if is_local and api_key is None:
    raise Exception("Please set OPENAI_API_KEY as an environment variable")

# If the app is running on Streamlit Cloud and the API key is not found, ask the user to input it
if not is_local and api_key is None:
    st.text("Enter your OpenAI API Key or get one [here](https://platform.openai.com/account/api-keys).")
    api_key = st.text_input("API Key", type='password')

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

    # Display loading indicator
    with st.spinner("Generating response..."):
        # Call the chat method to get AI response as an AIMessage object
        ai_msg = chat(messages)

    # Hide loading indicator
    st.spinner()

    # Display AI response on the Streamlit app
    st.write(ai_msg.content)

    # Append AI response to messages list for future reference
    messages.append(ai_msg)
