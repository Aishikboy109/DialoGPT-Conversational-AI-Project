#AUTHOR :  Aishik Bandyopadhyay
import json
import requests
from termcolor import colored, cprint
import speech_recognition as sr
# from converse import speak,get_intent
# import pyaudio
# from os import path
API_TOKEN = "api_JLDIPbbDrUTArOzRNJDQLMpPnrTkmeVBLZ"
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	data = json.dumps(payload)
	response = requests.request("POST", API_URL, headers=headers, data=data)
	return json.loads(response.content.decode("utf-8"))

while True:
	q = input("USER : ") 

	cprint("USER : {}".format(q), 'green')

	data = query( {"inputs": {"text": q}, "options": {"wait_for_model": True } } )

	cprint(data["generated_text"], 'red')

	if "bye" in q:
		break






