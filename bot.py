import wolframalpha
import pyttsx3
from termcolor import cprint,colored
# from colorama import Fore
# import json
# import requests
from act_by_intent import act_by_intent
from search import wolframalpha_search
from dialogpt_request import query


engine = pyttsx3.init()

def speak(text):
    if len(text) > 150:
        cprint(text, 'blue')
        return
    else:
        cprint(text, 'blue')
        engine.say(text)
        engine.runAndWait()


while True:
    user_prompt = text = colored('User >> ', 'magenta')
    q = input(user_prompt)
    if "bye" in q:
        speak("Goodbye")
        exit()
    
    result = act_by_intent(q)
    if result == None:
        if ("what" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                continue
        if ("how" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                continue
        if ("when" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                continue
        if ("search for" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                continue
        if ("who" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                continue
        
        else:
            res = query(q)
            if res:
                cprint("BOT: ", 'green', end='')
                speak(res)
            else:
             speak("Sorry, I don't know the answer to that")
    else:
        speak(result)