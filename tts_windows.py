import pyttsx3

engine = pyttsx3.init('sapi5')

def speak_windows(text):
    engine.say(text)
    engine.runAndWait()