# from api.ai import Agent
#AUTHOR :  Aishik Bandyopadhyay
import json
import requests


API_TOKEN = "your api token"
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


def chat(q):
    data = query({"inputs": {"text": q}})
    result = data["generated_text"]
    return result

