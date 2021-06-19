API_TOKEN = "api_JLDIPbbDrUTArOzRNJDQLMpPnrTkmeVBLZ"

import json
import requests
from termcolor import colored, cprint
import speech_recognition as sr
from converse import speak,get_intent
# import pyaudio
# from os import path

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	data = json.dumps(payload)
	response = requests.request("POST", API_URL, headers=headers, data=data)
	return json.loads(response.content.decode("utf-8"))

def get_audio():
# use the audio file as the audio source
	r = sr.Recognizer()

	with sr.Microphone() as source:
	    print("Speak now : ")
	    # r.energy_threshold = 300
	    # r.adjust_for_ambient_noise(source)
	    r.adjust_for_ambient_noise(source, duration=0.2)
	    audio = r.listen(source)  # read the entire audio file

	USERNAME = "1eb9030c-2914-4282-a27d-5a3e3fc6df9b"
	PASSWORD = "JzElIu2LNzENv8Qb7oA2Q0LY1tWwW0hFjVfiRw5Z7WXN"

	try:
	    return r.recognize_ibm(audio,username=USERNAME, password=PASSWORD)
	except sr.UnknownValueError:
	    return "Could not understand audio"
	except sr.RequestError as e:
	    return "Error; {0}".format(e)

# speak("Hello world")
while True:
	q = get_audio() 

	cprint("USER : {}".format(q), 'green')

	data = query( {"inputs": {"text": q} } )

	cprint(data["generated_text"], 'red')

	if "bye" in q:
		break






