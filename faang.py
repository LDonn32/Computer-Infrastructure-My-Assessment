#! /usr/bin/env python

# Author: Laura Donnelly

# Import necessary libraries.

# Yahoo Finance for the financial data.
import yfinance as yf 

# Pandas for data analyis.
import pandas as pd 

# Datetime for working timestamps.
import datetime as dt 

# Working with the operating systems.
import os  

# Assist file patterns to be matching.
import glob            


# Define the function.
def get_data():

    # Download historical stock data for FAANG companies from the last 5 days, with 1 hour intervals.
    data = yf.download(["META", "AAPL", "AMZN", "NFLX", "GOOG"], period="5d", interval="1h")
    # Save the downloaded data to a CSV file in the 'data' directory, with a timestamp in the filename.
    data.to_csv(f"data/{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    # Return the DataFrame.
    return data


# Call the function to fetch dataa. 
get_data()  

def plot_data():
    # Find all CSV files in the 'data' directory.
    list_of_files = glob.glob('data/*.csv')
    # Select the most recently created CSV file (latest data).
    latest_file = max(list_of_files, key=os.path.getctime)
    # Read the CSV file into a DataFrame, using multi-level headers and parsing the index as dates.
    data = pd.read_csv(latest_file, header=[0, 1], index_col=0, parse_dates=True)
    # Plot the 'Close' prices for all stocks.
    fig = data.plot(
        y='Close',  # Plot the 'Close' price column for each stock.
        title='FAANG Stock Prices Over the Last 5 Days',  
        xlabel='Date',    
        ylabel='Closing Price', 
        rot=30,           # Rotate x-axis labels for better readability.
        legend=True       
    )
    # Save the plot as a PNG file in the 'plots' directory, using the CSV filename as the image name.
    fig.figure.savefig(f"plots/{os.path.splitext(latest_file)[0][5:]}.png")

plot_data()  # Call the function to generate and save the plot.














