from newsapi import NewsApiClient

api = NewsApiClient(api_key='37f2607dcff648e391b3d365742ebbc6')

def get_headlines():
    results = api.get_top_headlines(sources='bbc-news')

    headlines = []
    for i in range(0,results["totalResults"]):
        headlines.append(results["articles"][i]["title"])

    return headlines