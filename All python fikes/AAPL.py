import datetime as dt
from matplotlib import style
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
style.use('ggplot')


##1start = dt.datetime(2000, 1, 1)
##1end = dt.datetime(2020, 1, 1)
##1Replace AAPL with any Nasdaq code for stock numbers##
##1df = web.DataReader('AAPL', 'yahoo', start, end)
##1df.to_csv('AAPL.csv')

df = pd.read_csv('AAPL.csv', parse_dates=True, index_col=0)

df['Dtrend'] = df['Close'] - df['Open']
df['Tavg'] = df['Dtrend'].rolling(window=100, min_periods=0).mean()
print(df)

ax1 = plt.subplot2grid((6, 1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan=1, colspan=1, sharex=ax1)


ax1.plot(df.index, df['Tavg'])
ax2.bar(df.index, df['Volume'])
##plt.show()