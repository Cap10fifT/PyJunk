import pandas as pd
# import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import os
from pandas import ExcelWriter
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt
import xlrd
from time import sleep

yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")
print(stock)

startyear = 2005
startmonth = 1
startday = 1

exportList = pd.DataFrame(columns=['stock', 'Daily', 'Date', 'close', 'Buy/Sell'])

start = dt.datetime(startyear, startmonth, startday)

now = dt.datetime.now()

# df = pdr.get_data_yahoo(stock, start, now)
ticker = yf.Ticker(stock)


emasUsed = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]

pos = 0
num = 0
percentchange = []
buy = None
y = 0
z = 0
df = ticker.history(period="7d", interval="2m")
df = df.iloc[60:]
for x in emasUsed:
    ema = x
    # df.iloc[:,4] selects the 4th column (close or whatever)
    df["Ema_" + str(ema)] = round(df.iloc[:, 4].ewm(span=ema, adjust=False).mean(), 2)
for i in df.index:

    cmin = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i], )
    cmax = max(df["Ema_30"][i], df["Ema_35"][i], df["Ema_40"][i], df["Ema_45"][i], df["Ema_50"][i], df["Ema_60"][i], )

    close = df["Close"][i]
    day = round(df["Close"][i], 2)
    Date = str(i.date())
    print(df["Close"].tail(2))


    if (cmin > cmax):
        # print("Red White Blue", day, Date)
        RWB = "RWB"
        if (pos == 0):
            bp = close
            pos = 1
            print("Buying now at " + str(bp))
            buy = "Buy"
            z += 1
        #insert webull buy protocol
        else:
            buy = None
    #            buy.append(["Buy"])
    # exportList.append({"Buy/Sell": buy}, ignore_index=True)

    elif (cmin < cmax):
        # print("Blue White Red", day, Date)
        RWB = "BWR"

        if (pos == 1):
            pos = 0
            sp = close
            print("Selling now at " + str(sp))
            pc = (sp / bp - 1) * 100
            percentchange.append(pc)
            buy = "Sell"
            z -= 1
        # insert webull sell protocol
        else:
            buy = None

    if (num == df["Close"].count() - 1 and pos == 1):
        pos = 0
        sp = close
        print("Selling now at " + str(sp), day, i)
        pc = (sp / bp - 1) * 100
        percentchange.append(pc)
        buy = "Sell"
        z -= 1
    #insert webull sell protocol
    # elif (pos == 1):
    # 	buy = None

    #        buy.append(["Sell"])
    # exportList.append({"Buy/Sell": sell}, ignore_index=True)
    exportList = exportList.append({"stock": stock, """Daily": RWB,""" "Date": Date, "close": close, "Buy/Sell": buy}, ignore_index=True)

    num += 1
#    sleep(2)

#print(percentchange)

gains = 0
ng = 0
losses = 0
nl = 0
totalR = 1

for i in percentchange:
    if (i > 0):
        gains += i
        ng += 1
    else:
        losses += i
        nl += 1
    totalR = totalR * ((i / 100) + 1)

totalR = round((totalR - 1) * 100, 2)

if (ng > 0):
    avgGain = gains / ng
    maxR = str(max(percentchange))
else:
    avgGain = 0
    maxR = "undefined"

if (nl > 0):
    avgLoss = losses / nl
    maxL = str(min(percentchange))
    ratio = str(-avgGain / avgLoss)
else:
    avgLoss = 0
    maxL = "undefined"
    ratio = "inf"

if (ng > 0 or nl > 0):
    battingAvg = ng / (ng + nl)
else:
    battingAvg = 0

print("Results for " + stock + " Sample size: " + str(ng+nl) + " trades")
print("EMAs used: "+str(emasUsed))
print("Batting Avg: "+ str(battingAvg))
print("Gain/loss ratio: "+ ratio)
print("Average Gain: "+ str(avgGain))
print("Average Loss: "+ str(avgLoss))
print("Max Return: "+ maxR)
print("Max Loss: "+ maxL)
print("Total return over "+str(ng+nl)+ " trades: "+ str(totalR)+"%" )
#print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )
print(z)

newFile = os.path.dirname(r'C:\Users\gusta\PycharmProjects\Finance\fine ants.py')+ str(stock) + ".xlsx"

writer = ExcelWriter(newFile)
exportList.to_excel(writer, "Sheet1")
writer.save()

#For fine ants.py, X = Date, Y = Adj Close
# x_values = close

# plt.plot(x_values)

# plt.show()





'''
	if(cmin>cmax):
		print("Red White Blue")
		if(pos==0):
			bp = close
			pos=1
			print("Buying now at "+str(bp
	if(cmin<cmax):
		print("Blue White Red")
		if(pos==1):
			pos= 0
			sp= close
			print("selling now at "+str(sp))
			pc=(sp/bp-1)*100
			percentchange.append(pc)

	if(num==df["Adj Close"].count()-1 and pos==1)
		pos=0
		sp=close
		print("selling now at "+str(sp))
		pc=(sp/bp-1)*100
		percentchange.append(pc)
	num+=1
'''
'''
ma=50
smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
df=df.iloc[ma:]
print(df)

numH = 0
numC = 0

    if(df["Adj Close"][i]>df[smaString][i]):
        print("The Close is higher")
        numH+=1
    else:
        print("The close is lower")
        numC+=1
    print(df.iloc[""][i])
print(str(numH))
print(str(numC))'''