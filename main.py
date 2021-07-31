import datetime
from nsepy import get_history
from datetime import date, datetime
import os
from tradingview_ta import TA_Handler, Interval, Exchange
import time
from selenium import webdriver

os.system("figlet -c Python Trading Bot ")
Today = date.today()
y = Today.strftime("%Y")
m = Today.strftime("%m")
# d = Today.strftime("%d")
d = "30"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#last order
last_order="sell"

#load chrome driver 
driver = webdriver.Chrome(executable_path="/Users/mrm/Downloads/chromedriver")
driver.maximize_window()
driver.get("https://in.tradingview.com/")
time.sleep(120)

#initiating tradingview handler to get the recomendation for sonata software for 15 min interval
ssw = TA_Handler(
    symbol="SONATSOFTW",
    screener="india",
    exchange="NSE",
    interval=Interval.INTERVAL_5_MINUTES
)


while True:
    if(current_time >= "09:30:00" and current_time <= "15:00:00"):

        rec = ssw.get_analysis()
        RSI = rec.indicators["RSI"]
        MACD = rec.indicators["MACD.macd"]
        EMA = rec.moving_averages["COMPUTE"]["EMA10"]

        if ( RSI >= 30 and last_order=="sell" and MACD >= 0 and EMA == "BUY" and RSI <=70):
            print("Buying 1 stock of SONATSOFTW")
            last_order="buy"
            #buy 1 stock of SONATSOFTW
            driver.find_element_by_xpath("//div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]").click()
            #click on buy 1 NES:
            driver.find_element_by_xpath("//div[1]/div[1]/div[6]/button[1]/         div[1]/span[2]").click()
        elif( RSI >= 30 and last_order=="buy" and EMA == "SELL"):
            print("Selling 1 stock of SONATSOFTW")
            last_order="sell"
            #sell 1 stock of SONATSOFTW 
            driver.find_element_by_xpath("//body[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
            time.sleep(2)
            driver.find_element_by_xpath("//button[1]/div[1]/span[2]").click            ()
        elif( RSI >= 70 and last_order=="sell" and EMA == "SELL"):
            print("Selling 1 stock of SONATSOFTW")
            last_order="sell"
            #sell 1 stock of SONATSOFTW 
            driver.find_element_by_xpath("//body[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
            time.sleep(2)
            driver.find_element_by_xpath("//button[1]/div[1]/span[2]").click 
        else:
            print("No trade")
    elif(current_time >= "15:00:00"):
        print("Time to close for the day")
        # #fetch open profit
        open_profit = driver.find_element_by_xpath("//div[4]/div[1]/div     [1]/div[1]/div[2]/div[3]/div[1]").text
        # print(open_profit)
        # P = "1000"
        print("Calculating profit :",open_profit)
        break
    else:
        if(current_time >= "09:05:00"):
            print("==========Getting Nifty and Bank Nifty opening price==========","\n\n")
            nifty = get_history(symbol='NIFTY 50',
                               start=date(int(y), int(m), int(d)),
                               end=date(int(y), int(m), int(d)),
                               index=True)

            niftyBank = get_history(symbol='NIFTY BANK',
                               start=date(int(y), int(m), int(d)),
                               end=date(int(y), int(m), int(d)),
                               index=True)

            print("====NIFTY 50====")
            print(nifty,"\n")
            print("====BANK NIFTY====")
            print(niftyBank,"\n")
        else:
            print("Waiting for market to open and bot to analyse market till 9:30")
    
    time.sleep(300)