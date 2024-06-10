import alpaca_trade_api as tradeapi
import pandas as pd
import streamlit as st

API_KEY = st.secrets["api"]["API_KEY"]
SECRET_KEY = st.secrets["api"]["SECRET_KEY"]
BASE_URL = st.secrets["api"]["BASE_URL"]

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def get_historical_data(symbol, start, end):
    barset = api.get_barset(symbol, 'day', start=start, end=end)
    return barset[symbol].df

def get_latest_quote(symbol):
    quote = api.get_last_quote(symbol)
    return quote._raw
