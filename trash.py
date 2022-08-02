import datetime
import json
import os
import requests
import wikipedia
from wit import Wit
import wolframalpha
from termcolor import colored, cprint
import speech_recognition as sr
from tts_linux import speak_linux
# from tts_windows import speak_windows
from sys import platform
import pyjokes
from googlesearch import search
import time
import pyttsx3
from search import search
from weather import weather

engine = pyttsx3.init()

def speak(text):
    # termcolor.cprint(text, 'red')
    engine.say(text)
    engine.runAndWait()


DIALOGPT_API_TOKEN = "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"
WOLFRAMALPHA_API_KEY = "AYAJ6Y-K686QW5UA3"
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"

headers = {"Authorization": f"Bearer {DIALOGPT_API_TOKEN}"}


wolframalpha_client = wolframalpha.Client(WOLFRAMALPHA_API_KEY)
def wolframalpha_search(query):
    res = wolframalpha_client.query(query)
    ans = next(res.results).text
    return ans

def query_wit(message):
    WIT_ACCESS_TOKEN = "OAGFU7QO7YG6KR3WEGWNA3SVWPQPOBDB"
    client = Wit(WIT_ACCESS_TOKEN)
    resp = client.message(message)
    return resp

def get_intent(message):
    WIT_ACCESS_TOKEN = "OAGFU7QO7YG6KR3WEGWNA3SVWPQPOBDB"
    client = Wit(WIT_ACCESS_TOKEN)
    resp = client.message(message)
    intent = resp["intents"][0]["name"]
    if intent:
        return intent
    else:
        return None
    
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))



def act_by_intent(query , inp):
    # print("ENTERED ACT BY INTENT METHOD!!!")
    # print("hullo")
    if "search" or "what is" in query:
        search(inp)

    elif "weather" in query:
        response = query_wit(inp)
        location = response["entities"]["wit$location:location"][0]["resolved"]["values"][0]["name"]
        weather(location)
        return ""

    elif "restart" and "computer" in query:
        res = "Restarting computer..."
        # if OS == "linux":
        #     os.system("reboot")
        # else:
        os.system("shutdown /r")
        return res

    elif "shutdown" or "shut the computer" or "poweroff the computer" in query:
        res = "Shutting the computer down..."
        # if OS == "linux":
        #     os.system("shutdown -h now")
        # else:
        os.system("shutdown /s")
        return res

    elif "joke" or "make me laugh" in query:
        # print("got joke intent")
        res = pyjokes.get_joke(category="all")
        return res


while True:
    q = input("User >> ")
    if q == None:
        continue
    cprint("USER : {}".format(q), "green")
    # intent = get_intent(q)
    # if intent != None:
        # final_result = act_by_intent(intent)
    # elif intent == None:
   
    final_result = act_by_intent(get_intent(q), q)
    if final_result:
        cprint(f"DialoGPT : {final_result}", "cyan")
        speak(final_result)
    else:
        data = query({"inputs": {"text": q}, "options": {"wait_for_model": True}})
        result = data["generated_text"]
        print(result)


# intent = get_intent(q)
# # print(1)
# if "wit$get_time" in intent:
#     # print(2)
#     res = datetime.now().strftime('%I:%M:%S')
#     # print(res)
# print("INTENT : ", intent)
# res = act_by_intent(intent, q)
# print(f"RESULT {res}")
# if res == None:
#     data = query({"inputs": {"text": q}, "options": {"wait_for_model": True}})
#     result = data["generated_text"]
#     # print("Result without intent", result)
# else:
#     result = res