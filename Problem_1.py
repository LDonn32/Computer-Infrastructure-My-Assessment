# Problem 1: Data from yfinance
# Author: Laura Donnelly


'''
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
'''

'''
import os
import yfinance as yf
import pandas as pd
from datetime import datetime


# Define function to get data
# This function will download the data hourly for the last 5 days for FAANG stocks
def get_data():
    

    

    # Define FAANG tickers
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    
    # Download data using yfinance (hourly interval, past 5 days)
    print("Downloading hourly data for FAANG stocks...")
    data = yf.download(
        tickers=tickers,
        period="5d",
        interval="1h",
        group_by='ticker'
    )

    # Create 'data' directory in the repo root if it doesn't exist
    data_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(data_dir, exist_ok=True)

    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.csv"
    filepath = os.path.join(data_dir, filename)

    # Save the combined dataframe to CSV
    data.to_csv(filepath)

    print(f"Data successfully saved to: {filepath}")
    return filepath

# Call the function 
get_data()

'''


# Dates and times.
import datetime as dt

# Data frames.
import pandas as pd

# Yahoo Finance data.
import yfinance as yf