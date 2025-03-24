import streamlit as st
from llm import load_deepseek, generate_response
from tts import TTS  # Reusing the same TTS implementation
import time

# Initialize components
@st.cache_resource
def load_components():
    model, tokenizer = load_deepseek()
    tts = TTS()
    return model, tokenizer, tts

model, tokenizer, tts = load_components()

# App UI
st.title("🧠 My DeepSeek Assistant")
st.caption("A personal work assistant powered by DeepSeek-R1 1.3B")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Settings sidebar
with st.sidebar:
    st.header("Settings")
    voice_enabled = st.checkbox("Enable Voice", True)
    max_tokens = st.slider("Max Response Length", 64, 512, 256)
    temp = st.slider("Creativity", 0.1, 1.0, 0.7)
    st.markdown("---")
    st.markdown("**DeepSeek-R1 1.3B**")
    st.markdown("A compact 1.3B parameter model")

# Chat input
if prompt := st.chat_input("Ask your work-related question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()