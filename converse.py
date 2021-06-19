# from api.ai import Agent
# import wolframalpha
# agent = Agent(
#      '<subscription-key>',
#      'd7b00ed0ee08464c860a9f6e8eb7164e',
#      '6fef320b63224ce6a42b443ec8428db1',
# )
# def chat(inp):
#     response = agent.query(inp)
#     result = response['result']
#     fulfillment = result['fulfillment']
#     response = fulfillment['speech']
#     return response

# def get_intent(inp):
#     response = agent.query(inp)
#     result = response['result']
#     intent = result['metadata']['intentName']
#     return intent

# client=wolframalpha.Client("U78Y2E-GR8KLU8U5U")

# def wolframalpha_search(query):
#     while True:

#         res=client.query(query)
#         ans=next(res.results).text
#         return ans


# if "TellToSearch" in intent:
# 	response = agent.query(inp)
# 	result = response['result']
# 	searchstring = result['parameters']['searched_item']
# 	print(f"Searched item : {searchstring}")
# 	results = wikipedia.summary(searchstring,sentences = 2)
# 	speak(results)


import json
import requests


API_TOKEN = "api_JLDIPbbDrUTArOzRNJDQLMpPnrTkmeVBLZ"
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

