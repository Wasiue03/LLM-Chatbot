import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed percent
        self.engine.setProperty('volume', 0.9)  # Volume 0-1
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()