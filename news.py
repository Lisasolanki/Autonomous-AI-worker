import requests

API_KEY = "YOUR_NEWSAPI_KEY"

def fetch_news(query="technology"):
    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "pageSize": 5, "apiKey": API_KEY}
    r = requests.get(url, params=params)
    data = r.json()
    return [a["title"] + " " + (a.get("description") or "") for a in data["articles"]]
