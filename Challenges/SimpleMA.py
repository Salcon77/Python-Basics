import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like # Pandas version compatibility
import pandas_datareader.data as web
style.use('ggplot')


df = pd.read_csv('crm.csv',parse_dates=True,  index_col=0)

df['100 ma'] = df['close'].rolling(window=100, min_periods=0).mean()


print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0), rowspawn=5,colspan=1)
ax2 = plt.subplot2grid(*(6,1), (5,0), rowspan=1, colspan=1)

ax1.plot(df.index, df["open"])
ax1.plot(df.index, df["100ma"])
ax2.plot(df.index, df['close'])
plt.show
