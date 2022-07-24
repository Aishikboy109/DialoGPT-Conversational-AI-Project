import pyttsx3

engine = pyttsx3.init()

def speak_windows(text):
    # termcolor.cprint(text, 'red')
    engine.say(text)
    engine.runAndWait()