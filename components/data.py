import alpaca_trade_api as tradeapi
import pandas as pd

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def get_historical_data(symbol, start, end):
    barset = api.get_barset(symbol, 'day', start=start, end=end)
    return barset[symbol].df

def get_latest_quote(symbol):
    quote = api.get_last_quote(symbol)
    return quote._raw
