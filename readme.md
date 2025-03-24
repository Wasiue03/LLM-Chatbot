# Personal Work Assistant Chatbot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-7C3AED?style=for-the-badge)

A CPU-optimized personal assistant chatbot using DeepSeek-R1 1.3B LLM through Ollama, with Streamlit interface and text-to-speech capabilities.

## Features

- 💡 Local AI assistant running on CPU
- 🎙️ Text-to-speech for interactive conversations
- ⚡ Optimized for low-resource machines (Intel i3/12GB RAM)
- 📁 Document processing capabilities
- 🔄 Conversation history
- 🛠️ Customizable settings

## Prerequisites

- Windows/Linux/macOS
- Python 3.8+
- 12GB+ RAM (minimum)
- Ollama installed ([installation guide](#ollama-installation))

## Installation

1. Clone the repository:
git clone https://github.com/Wasiue03/Chatbtt.git
cd personal-chatbot

2. Get Model:
ollama pull deepseek-coder:1.3b

3. Run App:
pip install -r requirements.txt
streamlit run app.py


4. Key Features
CPU-optimized (i3/12GB RAM compatible)
Voice responses (pyttsx3)
Adjustable response length
Conversation history