import os
from sys import platform
import pyjokes
import datetime
from speak import speak
from news import get_headlines

def act_by_intent(query):
    if platform == "linux" or platform == "linux2":
        OS = "linux"
    elif platform == "darwin":
        OS = "mac"
    elif platform == "win32":
        OS = "windows"
    else:
        OS = "unknown"

    if ("restart" and "computer") in query:
        res = "Restarting computer..."
        if OS == "linux":
            os.system("reboot")
        else:
            os.system("shutdown /r")
        return res

    elif ("shutdown" or "shut the computer" or "poweroff the computer") in query:
        res = "Shutting the computer down..."
        if OS == "linux":
            os.system("shutdown -h now")
        else:
            os.system("shutdown /s")
        return res

    elif ("joke" or "jokes" or "make me laugh") in query:
        # print("got joke intent")
        res = pyjokes.get_joke(category="all")
        return res

    elif ("time" or "what does the clock say" or "what is the clock saying") in query:
        return datetime.datetime.now().strftime("%I:%M %p")
    
    elif ("news" or "headlines") in query:
        speak("Here is the top news headlines")
        headlines = get_headlines()
        for i in headlines:
            speak(i)
    else:
        return None
