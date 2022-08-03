import pyttsx3
from termcolor import cprint
engine = pyttsx3.init()

def speak(text):
    if len(text) > 150:
        cprint(text, 'blue')
        return
    else:
        cprint(text, 'blue')
        engine.say(text)
        engine.runAndWait()
