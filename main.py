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


def speak(text):
    if OS == "linux":
        speak_linux(text)
    else:
        speak_windows(text)


wit_access_token = os.getenv("WIT_ACCESS_TOKEN")

DIALOGPT_API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {DIALOGPT_API_TOKEN}"}

wolframalpha_client = wolframalpha.Client(os.getenv("WOLFRAMALPHA_API_KEY"))


def wolframalpha_search(query):
    res = wolframalpha_client.query(query)
    ans = next(res.results).text
    return ans


def get_intent(message):
    client = Wit(wit_access_token)
    resp = client.message(message)
    intent = resp["intents"][0]["name"]
    return intent
    


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def weather():
    weather_api_key = os.getenv("WEATHER_API_KEY")
    speak("Enter the name of the city : ")
    city = get_audio()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    results = requests.request(method="POST", url=url)
    jsondata = results.json()
    weather_description = jsondata["weather"][0]["description"]
    temp = round(float(jsondata["main"]["temp"]) - 273, ndigits=2)
    temp_min = round(float(jsondata["main"]["temp_min"]) - 273, ndigits=2)
    temp_max = round(float(jsondata["main"]["temp_max"]) - 273, ndigits=2)
    pressure = jsondata["main"]["pressure"]
    humidity = jsondata["main"]["humidity"]
    wind_speed = jsondata["wind"]["speed"]

    speak(f"{weather_description}")
    time.sleep(0.6)

    weather_data = f"""
    temperature {temp}  degree celsius
    maximum temperature {temp_max}  degree celsius      
    minimum temperature {temp_min}  degree celsius
    Pressure {pressure}    millibars
    Humidity {humidity}
    wind speed {wind_speed}  knots
    """

    speak(weather_data)


searchstring = ""


def act_by_intent(intent, inp):
    # print("ENTERED ACT BY INTENT METHOD!!!")
    if "search" in intent:
        client = Wit(wit_access_token)
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
                res += f"\n{i}"
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
                    res += f"\n{i}"
        return res

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
        return None


def work(q):

    try:
        intent = get_intent(q)
        res = act_by_intent(intent, q)
        # print(f"RESULT {res}")
        if res == None:
            data = query({"inputs": {"text": q}, "options": {"wait_for_model": True}})
            result = data["generated_text"]
            print("Result without intent", result)
        else:
            result = res
    except Exception as e:
        # print("DID NOT GET ANY INTENT!!")
        # print(f"ERROR : {e}")
        data = query({"inputs": {"text": q}})
        result = data["generated_text"]
        # print(result)
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
    cprint(f"DialoGPT : {final_result}", "cyan")
    # if OS == "linux":
    #     speak_linux(result)
    # elif OS == "windows":
    #     speak_windows(result)

    if "bye" in q:
        break
