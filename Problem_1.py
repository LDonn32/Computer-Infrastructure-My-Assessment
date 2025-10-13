# Problem 1: Data from yfinance
# Author: Laura Donnelly

import yfinance as yf
import os
from datetime import datetime

#Link 
# https://www.geeksforgeeks.org/python/how-to-use-yfinance-api-with-python/

#link 
#https://pythonfintech.com/articles/how-to-download-market-data-yfinance-python/


# Download historical market data from Yahoo Finance and save to CSV file
#define function to get data
def get_data():
    # Define the stock tickers and download data
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    # Download historical market data from Yahoo Finance
    data = yf.download(
        tickers=tickers,
        period='5d',
        interval='1h',
        group_by='ticker',
        auto_adjust=True,
        threads=True
    )
    # Save the data to a CSV file with a timestamped filename
    os.makedirs('data', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

    filename = f'data/{timestamp}.csv'

    # Save the data to a CSV file
    data.to_csv(filename)