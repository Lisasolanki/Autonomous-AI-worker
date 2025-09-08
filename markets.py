import requests

API_KEY = "YOUR_ALPHA_KEY"

def fetch_market(symbol="AAPL"):
    url = "https://www.alphavantage.co/query"
    params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "apikey": API_KEY}
    r = requests.get(url, params=params)
    js = r.json()
    ts = js.get("Time Series (Daily)", {})
    return str(list(ts.items())[:5])  # just keep 5 days for demo
