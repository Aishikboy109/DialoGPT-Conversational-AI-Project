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


def get_bot_response(q):
    if "bye" in q:
        speak("Goodbye")
        return "Goodbye"
        exit()

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
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                return result
                # continue
        if ("when" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                return result
                # continue
        if ("search for" ) in q:
            result = wolframalpha_search(q)
            if result:
                cprint("BOT: ", 'green', end='')
                speak(result)
                return result
                # continue
        if ("who" ) in q:
            result = wolframalpha_search(q)
            if result != "No short answer available":
                cprint("BOT: ", 'green', end='')
                speak(result)
                return result
            
        
        else:
            res = query(q)
            if res:
                cprint("BOT: ", 'green', end='')
                speak(res)
                return res
            else:
                speak("Sorry, I don't know the answer to that")
                return res
    else:
        speak(result)
        return result

res = get_bot_response("hello")
print(res)