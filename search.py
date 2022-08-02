import urllib.parse
from dialogpt_request import query
import requests
import wolframalpha

APP_ID = "AYAJ6Y-K686QW5UA3"
wolframalpha_client = wolframalpha.Client(APP_ID)
def wolframalpha_search(q):
        encoded_string = urllib.parse.quote_plus(q)
        URL = f"https://api.wolframalpha.com/v1/result?i={encoded_string}&appid={APP_ID}"
        # print(URL)
        try:
            res = wolframalpha_client.query(q)
            ans = next(res.results).text
        except Exception as e:
            try:
                ans = requests.get(URL).text
                if ans == "Wolfram|Alpha did not understand your input":
                    raise Exception("wolframalpha failed")
            except Exception as e:
                try:
                    ans = query(q)
                except Exception as e:
                    ans = "Sorry, I don't know about that"           
        return ans
