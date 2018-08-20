import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like # Pandas version compatibility
style.use('ggplot')
"""
The purpose of this program is to read a csv file of stock prices and parse through it to return the simple moving 
average for 100 days. A simple moving average is the mean of prices over a given time period.In this case we are getting
the closing price for the past 100 days adding them all up and then dividing by a 100. The program is also designed
to return a graph of the moving average with the closing price. 
"""

# Parse csv file by dates and get rid of row number index.
df = pd.read_csv('NVDA.csv', parse_dates= True,index_col=0)

# Create a new column called 100 ma that takes the closing  price of past 100 days and returns the mean.
# If data for 100 prior days is not available  NaN  will be returned.
df['100 ma'] = df['close'].rolling(window=100).mean()


# This prints the last 3 days of data from the csv to the console.
print(df.tail(3))

# This plots the 100 day moving average that was calculated.
df[['100 ma', 'close']].plot()
plt.show()
