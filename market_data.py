import requests
import json

api_key = "WhZvG1WwRoLOE0vJQGsiS9b5XqTft5rK"

def get_fmp_data(symbol):
    # Quote
    quote_url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
    # RSI (14)
    rsi_url = f"https://financialmodelingprep.com/api/v3/technical_indicator/daily/{symbol}?period=14&type=rsi&apikey={api_key}"
    # SMA (50)
    sma_url = f"https://financialmodelingprep.com/api/v3/technical_indicator/daily/{symbol}?period=50&type=sma&apikey={api_key}"
    
    quote = requests.get(quote_url).json()
    rsi = requests.get(rsi_url).json()
    sma = requests.get(sma_url).json()
    
    return {
        "symbol": symbol,
        "price": quote[0]['price'] if quote else None,
        "rsi": rsi[0]['rsi'] if rsi else None,
        "sma": sma[0]['sma'] if sma else None,
        "change": quote[0]['changesPercentage'] if quote else None
    }

results = []
for sym in ["XAUUSD", "BTCUSD"]:
    results.append(get_fmp_data(sym))

print(json.dumps(results, indent=2))
