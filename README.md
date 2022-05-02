# tradingBotPython
Trading bot to backtest on tradeview

prerequisite :
1. Python3.*
2. pip3 install nsepy
3. pip3 install selenium
4. pip3 install webdriver_manager


Reference Document - 

1. chromedriver - https://sites.google.com/a/chromium.org/chromedriver/getting-started
2. Tradingview sample code - https://python-tradingview-ta.readthedocs.io/en/latest/overview.html

Working - 
1. Run python3 main.py at 9:00 AM on open market days
2. bot tries to read the nifty and banknifty current value
3. bot runs forever, starting from 9:00AM till 03:00 PM in the interval of 5 mins.
4. bot used strategies based on RSI and EMA ( please refer to google to understand more about these )

Steps to run - 
1. execute - python3 main.py - this will open a browser, login to your tradeview account and connect to paper trading. 
2. Open the trading box by clicking on the icon shown in the image below -
![alt text](https://github.com/md-raghib/tradingBotPython/blob/access/tradingWindow.png)
3. Let the code run. It will close at 3:00PM and sums up your profit for the day.
