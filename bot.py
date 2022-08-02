import wolframalpha
import pyttsx3
from termcolor import cprint
# import json
# import requests
from act_by_intent import act_by_intent
# from bot import act_by_intent
from hello import query


engine = pyttsx3.init()

def speak(text):
    cprint(text, 'blue')
    if len(text) > 45:
        cprint(text, 'blue')
    else:
        engine.say(text)
        engine.runAndWait()

wolframalpha_client = wolframalpha.Client("AYAJ6Y-K686QW5UA3")
def wolframalpha_search(q):
    try:
        res = wolframalpha_client.query(q)
        ans = next(res.results).text
    except Exception as e:
        ans  = query(q)
        # ans = "Sorry, I don't know about that"
        # try:
        #     ans = query(query)
        # except Exception as e:
        #     ans = "Sorry, I don't know about that"
    return ans


# def act_by_intent(query):
#     # print("ENTERED ACT BY INTENT METHOD!!!")
#     # print("hullo")
#     # if "search" or "what is" in query:
#     #     search(inp)

#     # if "weather" in query:
#     #     response = query_wit(inp)
#     #     location = response["entities"]["wit$location:location"][0]["resolved"]["values"][0]["name"]
#     #     weather(location)
#     #     return ""

#     if ("restart" and "computer") in query:
#         res = "Restarting computer..."
#         # if OS == "linux":
#         #     os.system("reboot")
#         # else:
#         os.system("shutdown /r")
#         return res

#     elif ("shutdown" or "shut the computer" or "poweroff the computer") in query:
#         res = "Shutting the computer down..."
#         # if OS == "linux":
#         #     os.system("shutdown -h now")
#         # else:
#         os.system("shutdown /s")
#         return res

#     elif ("joke" or "jokes" or "make me laugh") in query:
#         # print("got joke intent")
#         res = pyjokes.get_joke(category="all")
#         return res

#     elif ("time" or "what does the clock say" or "what is the clock saying") in query:
#         return datetime.datetime.now().strftime("%I:%M %p")

#     else:
#         return None


while True:
    q = input(" User >>")
    if "bye" in q:
        speak("bye")
        exit()
    
    result = act_by_intent(q)
    # if ("what" or "how" or "when" or "search for" or "what do you know" or "who") in q:
    #     speak(wolframalpha_search(q))
    #     continue
    # # else:

# or "how" or "when" or "search for" or "what do you know" or "who" or "on the web"


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
        # if ("what" ) in q:
        #     result = wolframalpha_search(q)
        #     if result:
        #         cprint("WOLFRAMALPHA: ", 'green', end='')
        #         speak(result)
            
        
        else:
            res = query(q)
            if res:
                cprint("DialoGPT: ", 'yellow', end='')
                speak(res)
            else:
             speak("Sorry, I don't know the answer to that")
    else:
        speak(result)