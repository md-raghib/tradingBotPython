import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.maximize_window()
driver.get("https://in.tradingview.com/")
time.sleep(120)
#buy
#Click on buy buttonb
driver.find_element_by_xpath("//div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]").click()
#click on buy 1 NES:
driver.find_element_by_xpath("//div[1]/div[1]/div[6]/button[1]/div[1]/span[2]").click()
time.sleep(5)
#sell
# sell = driver.find_element_by_xpath("//body[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").text
# print(sell)
driver.find_element_by_xpath("//body[1]/div[2]/div[8]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]").click()
# sell_b =driver.find_element_by_xpath("//button[1]/div[1]/span[2]").text
time.sleep(2)
# print(sell_b)
driver.find_element_by_xpath("//button[1]/div[1]/span[2]").click()
# #fetch open profit
open_profit = driver.find_element_by_xpath("//div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]").text
print(open_profit)
