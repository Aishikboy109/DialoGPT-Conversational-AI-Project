import json
import wikipedia
import wolframalpha
import requests
from termcolor import colored, cprint
import speech_recognition as sr
from tts import speak
from converse import chat
# import pyaudio
# from os import path


API_TOKEN = "api_JLDIPbbDrUTArOzRNJDQLMpPnrTkmeVBLZ"
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


from api.ai import Agent
import wolframalpha
agent = Agent(
    '<subscription-key>',
    'd7b00ed0ee08464c860a9f6e8eb7164e',
    '6fef320b63224ce6a42b443ec8428db1',
)


def chat_(inp):
    response = agent.query(inp)
    result = response['result']
    fulfillment = result['fulfillment']
    response = fulfillment['speech']
    return response


def get_intent(inp):
    response = agent.query(inp)
    result = response['result']
    intent = result['metadata']['intentName']
    return intent


client = wolframalpha.Client("U78Y2E-GR8KLU8U5U")


def wolframalpha_search(query):
    res = client.query(query)
    ans = next(res.results).text
    return ans


def get_audio():
    # use the audio file as the audio source
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now : ")
        # r.energy_threshold = 300
        # r.adjust_for_ambient_noise(source)
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)  # read the entire audio file

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't recognize audio")
    except sr.RequestError as e:
        cprint("Error; {0} \n\n\n".format(e), 'red')
        cprint("Terminating Program", 'red')
        exit(0)
def work(q):
    try:
        intent = get_intent(q)
        # print(f"GOT INTENT {intent}")
        result = act_by_intent(intent, q)
        if result == None:
            data = query( { "inputs" : {"text" : q} } )
            result = data["generated_text"]
            # print(result)
    except Exception as e:
        # print("DID NOT GET ANY INTENT!!")
        data = query( { "inputs" : {"text" : q} } )
        result = data["generated_text"]
        # print(result)
    return result


def act_by_intent(intent, inp):

    if "TellToSearch" in intent:
        response = agent.query(inp)
        result = response['result']
        searchstring = result['parameters']['searched_item']
        cprint(f"Searching for : {searchstring}",'orange')
        
        # if wikipedia.summary(searchstring,sentences = 2):
        try:
            res = wikipedia.summary(searchstring, sentences=2)
        # return res
    # res = wolframalpha_search(searchstring)
        except Exception as exception:
            try:
                res = wolframalpha_search(searchstring)
            except Exception as e:
                res = f"Could not find a result for {searchstring}"
        return res
# result=""

while True:
    q = get_audio()
    if q == None:
        continue
    cprint("USER : {}".format(q), 'green')
    # global result
    # if get_intent(q):
    #     intent = get_intent(q)
    # else:
    #     result = act_by_intent(intent, q)
    #     print("DID NOT GET ANY INTENT!!")
    #     data = query( { "inputs" : {"text" : q} } )
    #     result = data["generated_text"]
    #     print(result)
    # return result
    result = work(q)
    cprint(f"DialoGPT : {result}", 'cyan')
    speak(result)
    if "bye" in q:
        break

