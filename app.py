import streamlit as st
from components import auth, data, strategy
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Algo Trading App", layout="wide")

if auth.login():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Trade", "Logout"])

    if page == "Dashboard":
        st.title("Dashboard")
        symbol = st.text_input("Enter Stock Symbol", "AAPL")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        if st.button("Get Data"):
            df = data.get_historical_data(symbol, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            st.line_chart(df['close'])
            st.write(df)

    elif page == "Trade":
        st.title("Trade")
        st.write("Implement trade execution here.")

    elif page == "Logout":
        auth.logout()
else:
    st.title("Login")
