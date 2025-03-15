# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set the configuration for the Streamlit page
st.set_page_config(page_title="ChatAI", page_icon="🧠", layout="wide")

# Display the title and description in a centered div
st.markdown('''
  <div style="text-align: center;">
    <h1>🧠 ChatAI: Chat with AI</h1>
    <h3>I am here to help you. Ask me anything!</h3>
    <p>Powered by Google AI<br>Made with ❤️ by <a href="https://lakpriyaguru.me" target="_blank">@lakpriyaguru</a></p>
  </div>
''', unsafe_allow_html=True)