from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random


from tqdm import tqdm

import pandas as pd

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup



def scroll(d):
    SCROLL_PAUSE_TIME = 0.5 
    # Get scroll height
    last_height = d.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = d.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def tqdm_sleep(sec):
    for i in tqdm(range(sec)):
        time.sleep(1)
        
        
random.seed(time.time())

d = webdriver.Firefox(executable_path='/media/scarlet/Project/Project Files/PythonEnvs/AutomationEnv/AutoDriver/geckodriver', service_log_path='/media/scarlet/Project/Project Files/geckodriver.log')



d.maximize_window()



d.get('https://www.dsebd.org/latest_share_price_scroll_l.php')

d.implicitly_wait(7) # 30

soup = BeautifulSoup(d.find_elements(By.CLASS_NAME, 'floatThead-wrapper')[0].get_attribute('outerHTML'), 'html.parser')


import re

# string_with_unwanted_chars = "Hello, @World! 123"
# clean_string = re.sub(r'[^a-zA-Z0-9]', '', string_with_unwanted_chars)
# print(clean_string)  # Output: "Hello World 123"

c = 0
for j in soup.findAll('tr')[1:]:
    for i in range(1, len(j.findAll('td'))):
             if (i%10==0):
                 if j.findAll('td')[i].text == '--':
                     volume = 0.0
                 else:
                     volume = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Volume: ', volume)
             elif i%9==0:
                 if j.findAll('td')[i].text == '--':
                     value_of_trades = 0
                 else:
                     value_of_trades = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Value of Trades: ', value_of_trades)
             elif (i%8==0):
                 if j.findAll('td')[i].text == '--':
                     number_of_trades = 0
                 else:
                     number_of_trades = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Number of Trades: ', number_of_trades)
             elif (i%7==0):
                 if j.findAll('td')[i].text == '--':
                     percentage_change = 0
                 else:
                     percentage_change = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Percentage Change: ', percentage_change)
             elif (i%6==0):
                 if j.findAll('td')[i].text == '--':
                     yesterday_close_price = 0
                 else: 
                     yesterday_close_price = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Yesterday Close Price: ', yesterday_close_price)
             elif (i%5==0):
                 if j.findAll('td')[i].text == '--':
                     close_price = 0
                 else:
                     close_price = float(j.findAll('td')[i].text.replace(',', ''))   
                 print(str(c), ' : Close Price: ', close_price)
             elif (i%4==0):
                 if j.findAll('td')[i].text == '--':
                     last_low = 0
                 else:
                     last_low = float(j.findAll('td')[i].text.replace(',', ''))
                 # last_high = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Last Low: ', last_low)
             elif (i%3==0):
                 if j.findAll('td')[i].text == '--':
                     last_high = 0
                 else:
                     last_high = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Last High: ', last_high)
             # elif (i%3==0):
             #     last_trading_price = float(j.findAll('td')[i].text.replace(',', ''))
             elif (i%2==0):
                 if j.findAll('td')[i].text == '--':
                     last_trading_price = 0
                 else:
                     last_trading_price = float(j.findAll('td')[i].text.replace(',', ''))
                 print(str(c), ' : Last Trading Price:', last_trading_price)
             elif (i%1==0):
                 if j.findAll('td')[i].text == '--':
                     trading_code = 'None'
                 else:
                     trading_code = re.sub(r'[^a-zA-Z0-9]', '', j.findAll('td')[i].text)
                 print(str(c), ' : Trading code: ', trading_code)
    print(c)
    curr_co_data = {
                    'trading_code':trading_code,
                    'last_trading_price':last_trading_price,
                    'last_high':last_high,
                    'last_low':last_low,
                    'close_price':close_price,
                    'yesterday_close_price':yesterday_close_price,
                    'percentage_change':percentage_change,
                    'number_of_trades':number_of_trades,
                    'value_of_trades':value_of_trades,
                    'volume':volume,                    
                   }
    c = c + 1
    print(curr_co_data)
    if c == 5:
        break





# for i in range(1, len(soup.findAll('tr')[394].findAll('td'))):
#          if (i%10==0):
#              volume = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif i%9==0:
#              value_of_trades = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%8==0):
#              number_of_trades = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%7==0):
#              percentage_change = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%6==0):
#              yesterday_close_price = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%5==0):
#              close_price = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))            
#          elif (i%4==0):
#              last_low = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#              last_high = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%3==0):
#              last_trading_price = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%2==0):
#              last_trading_price = float(soup.findAll('tr')[394].findAll('td')[i].text.replace(',', ''))
#          elif (i%1==0):
#             trading_code = re.sub(r'[^a-zA-Z0-9]', '', soup.findAll('tr')[394].findAll('td')[i].text)
#             print(str(i), ' : ', trading_code)


# >TRADING CODE</th>
# 1  :  <th width="12%">LTP*</th>
# 2  :  <th width="12%">HIGH</th>
# 3  :  <th width="12%">LOW</th>
# 4  :  <th width="12%">CLOSEP*</th>
# 5  :  <th width="12%">YCP*</th>
# 6  :  <th width="12%">CHANGE</th>
# 7  :  <th width="12%">TRADE</th>
# 8  :  <th width="12%">VALUE (mn)</th>
# 9  :  <th width="12%">VOLUME</th>

         
         # elif (i%10==0):
         #     print('Hello!')
             # volume = soup.findAll('tr')[394].findAll('td')[i].text
         #     print(str(i), ' : ', soup.findAll('tr')[394].findAll('td')[i].text)
         # time.sleep(60)
         # print(str(i), ' : ', soup.findAll('tr')[394].findAll('td')[i].text)
         # print('Mod: ', str(i), " : ", (i%9==0))
     