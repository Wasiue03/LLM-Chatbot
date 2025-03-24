import streamlit as st
import ollama
import pyttsx3
import psutil
import time

# Initialize TTS
@st.cache_resource
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 0.8)
    return engine

tts_engine = init_tts()

# App UI
st.title("💻 My Ollama Assistant")
st.caption(f"Running DeepSeek-R1 1.3B on CPU (RAM: {psutil.virtual_memory().percent}% used)")

# Sidebar settings
with st.sidebar:
    st.header("Settings")
    voice_enabled = st.checkbox("Enable Voice", True)
    max_tokens = st.slider("Response Length", 64, 512, 256)
    st.markdown("---")
    st.markdown("**Current Model**")
    st.markdown("deepseek-coder:1.3b")
    st.button("Clear Memory", on_click=lambda: st.session_state.clear())

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your CPU-optimized AI assistant. How can I help with your work today?"}
    ]

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your work question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        try:
            message_placeholder = st.empty()
            full_response = ""
            
            # Stream the response
            for chunk in ollama.chat(
                model='deepseek-coder:1.3b',
                messages=st.session_state.messages,
                stream=True,
                options={
                    'num_predict': max_tokens,
                    'temperature': 0.7,
                    'num_thread': 4  # Match your CPU cores
                }
            ):
                token = chunk['message']['content']
                full_response += token
                time.sleep(0.05)  # Simulate typing
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            # Speak response if enabled
            if voice_enabled and len(full_response) < 300:  # Limit speech length
                tts_engine.say(full_response)
                tts_engine.runAndWait()
                
        except Exception as e:
            st.error("The assistant encountered an error. Please try a shorter prompt.")
            print(f"Error: {e}")