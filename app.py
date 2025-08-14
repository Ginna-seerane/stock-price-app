import yfinance as yf
import streamlit as st
from datetime import date

# App title
st.title("📈 Simple Stock Price App")

# Sidebar inputs
st.sidebar.header("Stock Selection")
tickerSymbol = st.sidebar.text_input("Enter stock symbol (e.g., GOOGL, AAPL, MSFT):", "GOOGL")

# Date range selection
start_date = st.sidebar.date_input("Start date", date(2015, 1, 1))
end_date = st.sidebar.date_input("End date", date.today())

# Fetch stock data
try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(start=start_date, end=end_date)

    # Company info
    st.subheader(f"Showing data for {tickerSymbol}")
    st.write(f"**Company Name:** {tickerData.info.get('longName', 'N/A')}")
    st.write(f"**Sector:** {tickerData.info.get('sector', 'N/A')}")
    st.write(f"**Industry:** {tickerData.info.get('industry', 'N/A')}")

    # Closing price chart
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    # Volume chart
    st.subheader("Trading Volume")
    st.line_chart(tickerDf.Volume)

except Exception as e:
    st.error(f"⚠️ Could not load data: {e}")
