import wikipedia
from googlesearch import search
from wit import Wit
import wolframalpha

WOLFRAMALPHA_API_KEY = "AYAJ6Y-K686QW5UA3"

wolframalpha_client = wolframalpha.Client(WOLFRAMALPHA_API_KEY)
def wolframalpha_search(query):
    res = wolframalpha_client.query(query)
    ans = next(res.results).text
    return ans


def search(searchstring):
    # WIT_ACCESS_TOKEN = "SD6F55A65VDP6RIAML7L3H4RWNOEFABP"
    # client = Wit(WIT_ACCESS_TOKEN)
    # resp = client.message(inp)
    # print("GOT RESPONSE FROM WIT.AI : ".format(resp))
    # searchstring = resp["entities"]["wit$search_query:search_query"][0]["value"]
    # print(f"GOT SEARCH STRING {searchstring}")
    # print(f"Searching for : {searchstring}")
    # google_results = search(searchstring,  stop=10, pause=2)

    try:
        # print("entering try block")
        res = (
            wolframalpha_search(searchstring)
            # + f"\nHere is more about {searchstring} : "
        )
        print(res)
        # for i in google_results:
        #     extra_urls += f"\n{i}"
    
    except Exception as e:
        try:
            # print("entering try block inside exception block")
            res = (
                wikipedia.summary(searchstring, sentences=2)
                # + f"\nHere is more about {searchstring} : "
            )
            # for i in google_results:
            #     # res += f"\n{i}"
            #     print(f"\n{i}")

        except Exception as e:
            print("Cannot find any results")

search(input(" User >> "))