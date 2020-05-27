import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
style.use('ggplot')

csv = pd.read_csv('apple.csv')

##Daily difference
csv['DaDif'] = csv['Open'] - csv['Adj Close']
##10 Day Average
##csv['10daav'] =  csv['']

print(csv)