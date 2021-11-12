import pandas as pd
import yfinance as yf
import datetime as dt
import os
from pandas import ExcelWriter

stock = input("Enter a stock ticker symbol: ")
print(stock)

exportList = pd.DataFrame(columns=['stock', 'Close', 'Buy'])

ticker = yf.Ticker(stock)
percentchange = []
pos = 0
num = 0

emasUsed = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]
class tradeBot():
    pos = 0
    def __init__(self, cmin, cmax, pos, bp, close, buy, z, sp, percentchange, exportList, df, num, Date):
        pos = 0
        if (cmin > cmax):
            # print("Red White Blue", day, Date)
            RWB = "RWB"
            if (pos == 0):
                bp = close
                pos = 1
                print("Buying now at " + str(bp))
                buy = "Buy"
                z += 1
            # insert webull buy protocol
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
            print("Selling now at " + str(sp))
            pc = (sp / bp - 1) * 100
            percentchange.append(pc)
            buy = "Sell"
            z -= 1
        exportList = exportList.append(
            {"stock": stock, """Daily": RWB,""" "Date": Date, "close": close, "Buy/Sell": buy}, ignore_index=True)

        num += 1

    #    sleep(2)

    def setDataFrame(self):
        df = ticker.history(period="6h", interval="2m")
        df = df.iloc[60:]

        for x in emasUsed:
            ema = x
            # may need to change iloc val depending on where it is pulling info from
            df["EMA_" + str(ema)] = round(df.iloc[:,4].ewm(span=ema, adjust=False).mean(), 2)

        for i in df.index:
            cmin = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i],
                       df["Ema_15"][i], )
            cmax = max(df["Ema_30"][i], df["Ema_35"][i], df["Ema_40"][i], df["Ema_45"][i], df["Ema_50"][i],
                       df["Ema_60"][i], )

            close = df["Close"][i]
            day = round(df["Close"][i], 2)
            Date = str(i.date())
            ndf = df.iloc[-1]
            return cmin, cmax, df, close, Date

tB = tradeBot()
print(tradeBot.setDataFrame())
# tradeBot(cmin, cmax, 0, 0, close, 0, 0, 0, percentchange, exportList, df, num, Date)

