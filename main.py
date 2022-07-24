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
from tts_windows import speak_windows
from sys import platform
import pyjokes
from googlesearch import search
import time
from dotenv import load_dotenv

load_dotenv()

if platform == "linux" or platform == "linux2":
    OS = "linux"
elif platform == "darwin":
    OS = "mac"
elif platform == "win32":
    OS = "windows"

import pyttsx3

engine = pyttsx3.init()

def speak_windows(text):
    # termcolor.cprint(text, 'red')
    engine.say(text)
    engine.runAndWait()

def speak(text):
    # if OS == "linux":
    #     speak_linux(text)
    # else:
        speak_windows(text)


# WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")
WIT_ACCESS_TOKEN = "SD6F55A65VDP6RIAML7L3H4RWNOEFABP"
WEATHER_API_KEY = "bb41e4817b91ff70028671598e6c4714"
DIALOGPT_API_TOKEN = "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"
WOLFRAMALPHA_API_KEY = "AYAJ6Y-K686QW5UA3"
# DIALOGPT_API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {DIALOGPT_API_TOKEN}"}



wolframalpha_client = wolframalpha.Client(WOLFRAMALPHA_API_KEY)
def wolframalpha_search(query):
    res = wolframalpha_client.query(query)
    ans = next(res.results).text
    return ans

def query_wit(message):
    client = Wit(WIT_ACCESS_TOKEN)
    resp = client.message(message)
    return resp

def get_intent(message):
    client = Wit(WIT_ACCESS_TOKEN)
    resp = client.message(message)
    intent = resp["intents"][0]["name"]
    return intent
    


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def weather(city):
    # WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    # speak("Enter the name of the city : ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    results = requests.request(method="POST", url=url)
    jsondata = results.json()
    weather_description = jsondata["weather"][0]["description"]
    temp = round(float(jsondata["main"]["temp"]) - 273, ndigits=2)
    temp_min = round(float(jsondata["main"]["temp_min"]) - 273, ndigits=2)
    temp_max = round(float(jsondata["main"]["temp_max"]) - 273, ndigits=2)
    pressure = jsondata["main"]["pressure"]
    humidity = jsondata["main"]["humidity"]
    wind_speed = jsondata["wind"]["speed"]
    cprint(f"Weather in {city} is {weather_description}", "blue")
    speak(f"{weather_description}")
    time.sleep(0.6)
    cprint("DialoGPT : Do you want to hear more about the weather?(Type 'y' or 'n')", "cyan")
    speak("Do you want to hear more about the weather?(Type 'y' or 'n')")
    ans = input(">>")
    if ans == "y":
        weather_data = f"""
        temperature {temp}  degree celsius
        maximum temperature {temp_max}  degree celsius      
        minimum temperature {temp_min}  degree celsius
        Pressure {pressure}    millibars
        Humidity {humidity}
        wind speed {wind_speed}  knots
        """
        cprint(f"{weather_data}", "blue")
        speak(weather_data)
    else:
        return

searchstring = ""

# def tell_time():
#     time = time.strftime("%I:%M:%S")
#     return f"The time is {time}"

# def tell_date():
#     date = time.strftime("%d/%m/%Y")
#     return f"The date is {date}"

def act_by_intent(intent, inp):
    # print("ENTERED ACT BY INTENT METHOD!!!")
    # print("hullo")
    if "search" in intent:
        client = Wit(WIT_ACCESS_TOKEN)
        resp = client.message(inp)
        # print("GOT RESPONSE FROM WIT.AI : ".format(resp))
        searchstring = resp["entities"]["wit$search_query:search_query"][0]["value"]
        # print(f"GOT SEARCH STRING {searchstring}")
        print(f"Searching for : {searchstring}")
        google_results = search(searchstring, num=10, stop=10, pause=2)
        # if wikipedia.summary(searchstring,sentences = 2):
        try:
            res = (
                wikipedia.summary(searchstring, sentences=2)
                + f"\nHere is more about {searchstring} : "
            )
            for i in google_results:
                # res += f"\n{i}"
                print(f"\n{i}")
        # return res
        # res = wolframalpha_search(searchstring)
        except Exception as exception:
            try:
                res = (
                    wolframalpha_search(searchstring)
                    + f"\nHere is more about {searchstring} : "
                )
                for i in google_results:
                    res += f"\n{i}"
            except Exception as e:

                res = (
                    f"Could not find a result for {searchstring}"
                    + f"\nHere is more about {searchstring} : "
                )
                for i in google_results:
                    # res += f"\n{i}"
                    print(f"\n{i}")

        return res
    # elif "wit$get_time" in intent:
    #     # print("hullo0")
    #     res = datetime.now().strftime('%I:%M:%S')
    #     return res
        # print("hullo0" + res)            
        # return res
    # elif "wit$get_date" in intent:
    #     res = tell_date()
    #     return res
    elif "wit$get_weather" in intent:
        response = query_wit(inp)
        location = response["entities"]["wit$location:location"][0]["resolved"]["values"][0]["name"]
        weather(location)
        return ""
        
    elif "restart_computer" in intent:
        res = "Restarting computer..."
        if OS == "linux":
            os.system("reboot")
        else:
            os.system("shutdown /r")
        return res
    elif "shutdown_computer" in intent:
        res = "Shutting the computer down..."
        if OS == "linux":
            os.system("shutdown -h now")
        else:
            os.system("shutdown /s")
        return res
    elif "joke" in intent:
        # print("got joke intent")
        res = pyjokes.get_joke(category="all")
        return res

    else:
        # print("hullo2")
        return None

    #TODO
#def wish():


def work(q):
    # if "weather" in q:
    try:
        intent = get_intent(q)
        # print(1)
        if "wit$get_time" in intent:
            # print(2)
            res = datetime.now().strftime('%I:%M:%S')
            # print(res)
        print("INTENT : ", intent)
        res = act_by_intent(intent, q)
        # print(f"RESULT {res}")
        if res == None:
            data = query({"inputs": {"text": q}, "options": {"wait_for_model": True}})
            result = data["generated_text"]
            # print("Result without intent", result)
        else:
            result = res
    except Exception as e:
        # print("DID NOT GET ANY INTENT!!")
        # print(f"ERROR : {e}")
        data = query({"inputs": {"text": q}})
        result = data["generated_text"]
        
    return result


def get_audio():
    # use the audio file as the audio source
    r = sr.Recognizer()

    with sr.Microphone() as source:
        cprint("Speak now : ", "green")
        # r.energy_threshold = 300
        # r.adjust_for_ambient_noise(source)
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)  # read the entire audio file

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        cprint("Couldn't recognize audio", "red")
    except sr.RequestError as e:
        cprint("Error; {0} \n\n\n".format(e), "red")
        cprint("Terminating Program", "red")
        exit(0)


while True:
    q = input("User >> ")
    if q == None:
        continue
    cprint("USER : {}".format(q), "green")
    final_result = work(q)
    if final_result:
        cprint(f"DialoGPT : {final_result}", "cyan")
    if OS == "linux":
        speak_linux(final_result)
    elif OS == "windows":
        speak_windows(final_result)

    if "bye" in q:
        break
