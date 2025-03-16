# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Function to retrieve the API key from Streamlit secrets
def get_api_key():
  try:
    return st.secrets["GOOGLE_GEMINI_KEY"]
  except KeyError:
    st.error("API key not found. Please add it to Streamlit secrets.")
    st.stop()

# Configure the API key for the generative AI service
api_key = get_api_key()
genai.configure(api_key=api_key)

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

# Dropdown to select the model
model_options = [
  "gemini-2.0-flash",
  "gemini-2.0-flash-lite",
  "gemini-2.0-pro-exp-02-05",
  "gemini-2.0-flash-thinking-exp-01-21",
  "gemma-3-27b-it"
]
selected_model = st.selectbox("Select a model", model_options)

# Initialize the generative AI model based on the selected model
model = genai.GenerativeModel(selected_model)

# Initialize chat history
if "chat" not in st.session_state:
  st.session_state.chat = model.start_chat(history=[])

# Display chat history
for role, message in st.session_state.chat.history:
  st.chat_message(role).markdown(message)

# Interactive chat input and response
if prompt := st.chat_input("Ask me anything..."):
  # Immediately show user prompt in chat
  st.session_state.chat.history.append(("user", prompt))
  st.chat_message("user").markdown(prompt)
  
  # Generate response from the model
  response = model.generate_content(prompt)
  st.session_state.chat.history.append(("assistant", response.text))
  st.chat_message("assistant").markdown(response.text)
