# 🧠 ChatAI

**ChatAI** is an interactive AI chatbot powered by Google Gemini AI models. Built with **Streamlit**, this app allows users to chat with an AI model and receive intelligent responses in real time.

---

## 🚀 Features

- Select from multiple AI models (Gemini 2.0 Flash, Pro, Gemma 3, etc.).
- Interactive chat interface with real-time responses.
- Maintains chat history for a seamless experience.
- Simple and user-friendly UI built with Streamlit.
- Secure API key management using Streamlit Secrets.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/lakpriyaguru/chatai.git
cd chatai
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

Store your **Google Gemini AI API Key** securely in Streamlit secrets.

1. Rename `secrets.toml.example` to `secrets.toml`.
2. Obtain your API key from [Google AI Studio](https://aistudio.google.com/apikey).
3. Add your API key to the `secrets.toml` file:
   ```toml
   GOOGLE_GEMINI_KEY = "your_google_genai_api_key"
   ```
4. If deploying on **Streamlit Cloud**, add the secret under _App Settings > Secrets_.

---

## ▶️ Run the App

Start the Streamlit app by running:

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the web interface.
2. Choose an AI model from the dropdown menu.
3. Type a question in the chat input box and press Enter.
4. Get responses from the AI in real-time!

---

## 📌 Project Structure

```
📂 chatai/
├── 📂 .streamlit/
│   ├── secrets.toml        # Stores API key securely
├── 📜 app.py               # Main Streamlit application
├── 📜 requirements.txt     # Essential dependencies
├── 📜 requirements_all.txt # Full dependency list
├── 📜 README.md            # Project documentation
```

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 📧 Contact

Have questions or feedback? I'd love to hear from you! Feel free to reach out via [lakpriyaguru.me](https://lakpriyaguru.me).

If you found this project helpful, consider giving it a ⭐ on GitHub!

Follow me for more updates and new projects. Happy coding! 🚀
