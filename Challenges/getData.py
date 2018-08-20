import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like  # Pandas version compatibility
import pandas_datareader.data as web

"""
The purpose of this program is to get the daily stock prices over a period of time and then put them into a csv file.
"""
# Setting a start and end date with datetime
start = dt.datetime(2017,1,1)
end= dt.datetime(2018,8,31)

# Using data reader from pandas to retrieve stock data from IEX for Nvidia's stock
df = web.DataReader('NVDA', 'iex', start ,end )

# This prints the last 5 days of available data.
print(df.tail())

# Creates a csv file of the data we retrieved.
df.to_csv('NVDA.csv')


