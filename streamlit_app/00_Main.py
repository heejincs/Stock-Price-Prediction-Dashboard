import streamlit as st

st.set_page_config(
    page_title="Stock Price Prediction Dashboard",
    page_icon="📊",
)

st.markdown(
    """# 📈 **Stock Price Prediction Dashboard**
### **Predicting Stock Prices using Machine Learning**

**Stock Price Prediction Dashboard is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## **How It's Built**

Stock Price Prediction Dashboard is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices


## **Future Work**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

##  **Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)