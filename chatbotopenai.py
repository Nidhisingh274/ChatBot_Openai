# Import necessary libraries
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Function to get response from OpenAI model
def get_openai_response(question):
    # Initialize OpenAI model with API key and parameters
    llm = OpenAI(
        openai_api_key=os.getenv("OPEN_API_KEY"),  # Fetch API key from environment variables
        model_name='text-davinci-003',  # Specify model
        temperature=0.6  # Set creativity level
    )
    response = llm(question)  # Generate response
    return response  # Return response

# Set Streamlit page title
st.set_page_config(page_title='Q&A Demo')

# Display header on the app
st.header('Langchain Application')

# Input field for user question
input = st.text_input('Input:', key='input')

# Generate OpenAI response
response = get_openai_response(input)

# Button to submit question
submit = st.button('Ask the question')

# Display response when button is clicked
if submit:
    st.subheader('The Response is')
    st.write(response)  # Display response
