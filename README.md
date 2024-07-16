# Stock Value Prediction Script

<p align="center">
  <img src="https://github.com/user-attachments/assets/135d4a5f-8bfb-49b5-b9f0-a37f0c3a5fde">
</p>

**DISCLAIMER: THIS IS NOT MEANT TO BE FINANCIAL ADVICE, THIS SCRIPT WAS CREATED FOR MY OWN ENTERTAINMENT.**

With the power of machine learning and python, I present to you all, a stock value prediction tool made in python.

## Overview

The application:
- Downloads historical stock data using `yfinance`.
- Uses `Prophet` to forecast future stock prices.
- Visualizes the actual and predicted stock prices using `Plotly`.
- Serves the results through a Flask web server.

## Requirements

- Flask
- yfinance
- prophet
- plotly

The setup is very simple. Follow these steps to setup your own stock prediction tool!

## Setup ##
1. Clone repo by running ```git clone https://github.com/tr4xnz/stock-value-prediction/``` in terminal.
2. Navigate into the directory by running ```cd stock-price-prediction```
3. Install required modules by running ```pip install -r requirements.txt``` in terminal.
4. Run main.py by running ```python main.py``` in terminal
5. Open up your web browser and visit https://127.0.0.1:5001/predict/{STOCK_TICKER} (Replace {STOCK_TICKER} with the ticker of the stock you want to predict)

<p align="center">
  <img src="https://github.com/user-attachments/assets/43465fa0-6c80-422e-b436-5908e024972c">
</p>


**What is a "ticker"?**
A stock ticker is a unique series of letters assigned to a publicly traded company, used to identify and track its stock on exchanges. It typically consists of one to four letters. For example, "AAPL" is the stock ticker for Apple Inc., "GOOGL" for Alphabet Inc. (Google's parent company), and "TSLA" for Tesla Inc.

**How to find tickers?**
For starters, you can find tickers by visiting (Yahoo Finance)[https://finance.yahoo.com/markets/stocks/gainers/] and looking in the row that says "Symbol".

**Created by tr4xnz/co.v3rt**
