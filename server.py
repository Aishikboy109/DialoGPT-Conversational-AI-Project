from black import main
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# eikhane main flask er code ta jabe....tui video ta dekh sob explain kora ache...aste aste korte thak ar kichuta progress korle github e push kore dis ar amay janash
# import sys
from flask_cors import CORS
# sys.path.append("D:scripts_on_d_drive/DialoGPT-Conversational-AI-Project/")

# from main import get_bot_response


import wolframalpha
import pyttsx3
from termcolor import cprint,colored
from act_by_intent import act_by_intent
from search import wolframalpha_search
from dialogpt_request import query


engine = pyttsx3.init()

def speak(text):
    if len(text) > 150:
        cprint(text, 'blue')
        return
    else:
        # cprint(text, 'blue')
        engine.say(text)
        engine.runAndWait()


def bot_response(q):
    if "bye" in q:
        speak("Goodbye")
        return "Goodbye"
        # exit()

    result = act_by_intent(q)
    if result == None:
        if ("what" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                return result
                # continue
        if ("how" ) in q:
            result = wolframalpha_search(q)
            # if result:
            #     cprint("BOT: ", 'green', end='')
            #     speak(result)
            #     return result
                # continue
        if ("when" ) in q:
            result = wolframalpha_search(q)
            # if result:
            #     cprint("BOT: ", 'green', end='')
            #     speak(result)
            #     return result
                # continue
        if ("search for" ) in q:
            result = wolframalpha_search(q)
            # if result:
            #     cprint("BOT: ", 'green', end='')
            #     speak(result)
            #     return result
                # continue
        if ("who" ) in q:
            result = wolframalpha_search(q)
            # if result:
            #     cprint("BOT: ", 'green', end='')
            #     speak(result)
            #     return result
                # continue
        
        else:
            res = query(q)
            if res:
                cprint("BOT: ", 'green', end='')
                # speak(res)
                # return res
                result = res
            else:
                result = "Sorry, I don't know about that"
                # speak("Sorry, I don't know the answer to that")
                # return "Sorry, I don't know the answer to that"
    speak(result)
    return result

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("bot.html")

@app.route("/api/<string:query>")
def get_bot_response(query):
    # user_input = request.args.get('input')
    print("inside get bot response")
    print(query)
    res = bot_response(query)
    print("res : " + res)
    return jsonify({"response": res})

if __name__ == "__main__":
    app.run(debug=True)
