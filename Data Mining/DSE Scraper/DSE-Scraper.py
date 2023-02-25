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


def download_img(current_url, save_name, s_cnt):
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1",



    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    ]
    random_user_agent = random.choice(user_agents)
    headers = {
    'User-Agent': random_user_agent, 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.google.com/',
    }
    s_cnt = s_cnt + 1 
    s_dir = save_name + str(s_cnt) + '.jpg'
    with open(s_dir, 'wb') as handle:
        response = requests.get(current_url, headers=headers, stream=True)
        if not response.ok:
            print(Fore.YELLOW, response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    print(Fore.GREEN, 'Saved ', str(s_cnt))
    print(Fore.WHITE)
    return s_dir
    # print('Saved image')


random.seed(time.time())

d = webdriver.Firefox()

d.implicitly_wait(7) # 30

d.maximize_window()



d.get('https://www.dsebd.org/displayCompany.php?name=AAMRANET')



soup = BeautifulSoup(d.find_elements(By.ID, 'section-to-print')[0].get_attribute('outerHTML'), 'html.parser')


# tables = soup.find_all('table')

# tables[0].findChildren()[0]

# soup.find_all('th')


table_0 = {}
tmp = d.find_elements(By.ID, 'company')[0].text
s_trading_code = tmp.find('Trading Code: ')
s_script_code = tmp.find('Scrip')
tmp[s_trading_code+ len(('Trading Code: ')):s_script_code-1]

table_0['trading_code'] = tmp[s_trading_code+ len(('Trading Code: ')):s_script_code-1]

company_name = d.find_elements(By.CLASS_NAME, 'BodyHead')[0].text
table_0['company_name'] = company_name[company_name.find(':')+2:]

market_info_date = d.find_elements(By.CLASS_NAME, 'BodyHead')[1].text
table_0['market_info_date'] = market_info_date[market_info_date.find(':')+2:]


d.find_elements(By.ID, 'company')[1].get_attribute('innerHTML')


# first we should find our table object:
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[1].get_attribute('innerHTML'), 'html.parser')
# # then we can iterate through each row and extract either header or row values:
# table_headers = []
# for x in soup.find_all('tr'):
#     for y in x.find_all('th'):
#         table_headers.append(y.text)

# table_headers


# table_rows = []
# for x in soup.find_all('tr')[1:]:
#     td_tags = x.find_all('td')
#     td_val = [y.text for y in td_tags]
#     table_rows.append(td_val)

# pd.DataFrame(table_rows,columns=table_headers)

# table_rows = soup.find_all('tr')
# data = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     data.append(row)



# soup.find_all('tr')[0]
# table_headers = []
# for x in soup.find_all('tr'):
#     for y in x.find_all('th'):
#         table_headers.append(y.text)

# table_headers


# table_rows = []
# for x in soup.find_all('tr')[1:]:
#     td_tags = x.find_all('td')
#     td_val = [y.text for y in td_tags]
#     table_rows.append(td_val)

# table_rows


# Table 1
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[1].get_attribute('innerHTML'), 'html.parser')
table_1 = {}
for row in soup.find_all('tr'):
    row_header = row.th.get_text()
    row_cell = row.td.get_text()
    table_1[row_header] = row_cell

table_1


# Table 2
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[2].get_attribute('innerHTML'), 'html.parser')
table_2 = {}
for row in soup.find_all('tr'):
    row_header = row.th.get_text()
    row_cell = row.td.get_text()
    table_2[row_header] = row_cell

table_2


# Table 3
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[3].get_attribute('innerHTML'), 'html.parser')
table_3 = {}
for row in soup.find_all('tr'):
    row_header = row.th.get_text()
    row_cell = row.td.get_text()
    table_3[row_header] = row_cell

table_3




# Large table - need to find what is important
# Table 4
# soup = BeautifulSoup(d.find_elements(By.ID, 'company')[4].get_attribute('innerHTML'), 'html.parser')
# result = {}
# for row in soup.find_all('tr'):
#     row_header = row.th.get_text()
#     row_cell = row.td.get_text()
#     result[row_header] = row_cell

# result


# Unaudited info table
# # Table 5
# soup = BeautifulSoup(d.find_elements(By.ID, 'company')[5].get_attribute('innerHTML'), 'html.parser')
# result = {}
# for row in soup.find_all('tr'):
#     row_header = row.th.get_text()
#     row_cell = row.td.get_text()
#     result[row_header] = row_cell

# result




# Audited table
# # Table 6
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[6].get_attribute('innerHTML'), 'html.parser')
pe_ratio_latest_audited_basic_eps = []
pe_ratio_latest_audited_diluted_eps = []
# for row in soup.find_all('tr'):
#     row_header = row.th.get_text()
#     row_cell = row.td.get_text()
#     result[row_header] = row_cell
c = 0
for row in soup.find_all('td'):
    # row_header = row.th.get_text()
    row_cell = row.get_text()
    # result[row_header] = row_cell
    print(c)
    print(row_cell)
    if c==8:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==9:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==10:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==11:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==12:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==13:
        pe_ratio_latest_audited_basic_eps.append(row_cell)
    # elif c==14:
    #     pe_ratio_latest_audited_basic_eps.append(row_cell)
    elif c==15:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    elif c==16:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    elif c==17:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    elif c==18:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    elif c==19:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    elif c==20:
        pe_ratio_latest_audited_diluted_eps.append(row_cell)
    # elif c==21:
    #     pe_ratio_latest_audited_diluted_eps.append(row_cell)
    c = c + 1

table_6 = {}
table_6['pe_ratio_latest_audited_basic_eps'] = pe_ratio_latest_audited_basic_eps
table_6['pe_ratio_latest_audited_diluted_eps'] = pe_ratio_latest_audited_diluted_eps
table_6


# # Table 7
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[7].get_attribute('innerHTML'), 'html.parser')
table_7 = {}

c = 0
for row in soup.find_all('td'):
    # row_header = row.th.get_text()
    row_cell = row.get_text()
    # result[row_header] = row_cell
    print(c)
    print(row_cell)
    if c == 19:
        table_7['first_year'] = row_cell
    elif c == 26: # 16 17
        table_7['first_year_nav_per_share_original'] = row_cell
    elif c == 27:
        table_7['first_year_nav_per_share_restated'] = row_cell
    elif c == 28:
        table_7['first_year_nav_per_share_diluted'] = row_cell
    elif c == 29:
        table_7['first_year_profit_continuing_operations'] = row_cell
    elif c == 30:
        table_7['first_year_profit'] = row_cell
    elif c == 31:
        table_7['first_year_total_comprehensive_income'] = row_cell
    elif c == 32:
        table_7['second_year'] = row_cell
    elif c == 39: # 16 17
        table_7['second_year_nav_per_share_original'] = row_cell
    elif c == 40:
        table_7['second_year_nav_per_share_restated'] = row_cell
    elif c == 41:
        table_7['second_year_nav_per_share_diluted'] = row_cell
    elif c == 42:
        table_7['second_year_profit_continuing_operations'] = row_cell
    elif c == 43:
        table_7['second_year_profit'] = row_cell
    elif c == 44:
        table_7['second_year_total_comprehensive_income'] = row_cell
    elif c == 45:
        table_7['third_year'] = row_cell
    elif c == 45 + 7: # 16 17
        table_7['third_year_nav_per_share_original'] = row_cell
    elif c == 45 + 8:
        table_7['third_year_nav_per_share_restated'] = row_cell
    elif c == 45 + 9:
        table_7['third_year_nav_per_share_diluted'] = row_cell
    elif c == 45 + 10:
        table_7['third_year_profit_continuing_operations'] = row_cell
    elif c == 45 + 11:
        table_7['third_year_profit'] = row_cell
    elif c == 45 + 12:
        table_7['third_year_total_comprehensive_income'] = row_cell
    elif c == 58:
        table_7['fourth_year'] = row_cell
    elif c == 58 + 7: # 16 17
        table_7['fourth_year_nav_per_share_original'] = row_cell
    elif c == 58 + 8:
        table_7['fourth_year_nav_per_share_restated'] = row_cell
    elif c == 58 + 9:
        table_7['fourth_year_nav_per_share_diluted'] = row_cell
    elif c == 58 + 10:
        table_7['fourth_year_profit_continuing_operations'] = row_cell
    elif c == 58 + 11:
        table_7['fourth_year_profit'] = row_cell
    elif c == 58 + 12:
        table_7['fourth_year_total_comprehensive_income'] = row_cell
    elif c == 71:
        table_7['fifth_year'] = row_cell
    elif c == 71 + 7: # 16 17
        table_7['fifth_year_nav_per_share_original'] = row_cell
    elif c == 71 + 8:
        table_7['fifth_year_nav_per_share_restated'] = row_cell
    elif c == 71 + 9:
        table_7['fifth_year_nav_per_share_diluted'] = row_cell
    elif c == 71 + 10:
        table_7['fifth_year_profit_continuing_operations'] = row_cell
    elif c == 71 + 11:
        table_7['fifth_year_profit'] = row_cell
    elif c == 71 + 12:
        table_7['fifth_year_total_comprehensive_income'] = row_cell
    c = c + 1

table_7




# # # Table 8
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[8].get_attribute('innerHTML'), 'html.parser')
table_8 = {}

c = 0
for row in soup.find_all('td'):
    # row_header = row.th.get_text()
    row_cell = row.get_text()
    # result[row_header] = row_cell
    # print(c)
    # print(row_cell)
    if c == 14:
        table_8['first_year'] = row_cell
    elif c == 15: # 16 17
        table_8['first_year_eps_original'] = row_cell
    elif c == 16:
        table_8['first_year_eps_restated'] = row_cell
    elif c == 17:
        table_8['first_year_eps_diluted'] = row_cell
    elif c == 18:
        table_8['first_year_eps_original_continuing_operation'] = row_cell
    elif c == 19:
        table_8['first_year_eps_restated_continuing_operation'] = row_cell
    elif c == 21:
        table_8['first_year_dividend'] = row_cell
    elif c == 22:
        table_8['first_year_dividend_yeild'] = row_cell
    #
    elif c == 23:  # 14
        table_8['second_year'] = row_cell
    elif c == 24: # 15
        table_8['second_year_eps_original'] = row_cell
    elif c == 25:
        table_8['second_year_eps_restated'] = row_cell
    elif c == 26:
        table_8['second_year_eps_diluted'] = row_cell
    elif c == 27:
        table_8['second_year_eps_original_continuing_operation'] = row_cell
    elif c == 28:
        table_8['second_year_eps_restated_continuing_operation'] = row_cell
    elif c == 29:
        table_8['second_year_eps_diluted_continuing_operation'] = row_cell
    elif c == 30:
        table_8['second_year_dividend'] = row_cell
    elif c == 31:
        table_8['second_year_dividend_yeild'] = row_cell
    #
    #
    elif c == 32:  # 14
        table_8['third_year'] = row_cell
    elif c == 33: # 15
        table_8['third_year_eps_original'] = row_cell
    elif c == 34:
        table_8['third_year_eps_restated'] = row_cell
    elif c == 35:
        table_8['third_year_eps_diluted'] = row_cell
    elif c == 36:
        table_8['third_year_eps_original_continuing_operation'] = row_cell
    elif c == 37:
        table_8['third_year_eps_restated_continuing_operation'] = row_cell
    elif c == 38:
        table_8['third_year_eps_diluted_continuing_operation'] = row_cell
    elif c == 39:
        table_8['third_year_dividend'] = row_cell
    elif c == 40:
        table_8['third_year_dividend_yeild'] = row_cell
    #
    #
    elif c == 41:  # 14
        table_8['fourth_year'] = row_cell
    elif c == 42: # 15
        table_8['fourth_year_eps_original'] = row_cell
    elif c == 43:
        table_8['fourth_year_eps_restated'] = row_cell
    elif c == 44:
        table_8['fourth_year_eps_diluted'] = row_cell
    elif c == 45:
        table_8['fourth_year_eps_original_continuing_operation'] = row_cell
    elif c == 46:
        table_8['fourth_year_eps_restated_continuing_operation'] = row_cell
    elif c == 47:
        table_8['fourth_year_eps_diluted_continuing_operation'] = row_cell
    elif c == 48:
        table_8['fourth_year_dividend'] = row_cell
    elif c == 49:
        table_8['fourth_year_dividend_yeild'] = row_cell
    #
    #
    elif c == 50:  # 14
        table_8['fifth_year'] = row_cell
    elif c == 51: # 15
        table_8['fifth_year_eps_original'] = row_cell
    elif c == 52:
        table_8['fifth_year_eps_restated'] = row_cell
    elif c == 53:
        table_8['fifth_year_eps_diluted'] = row_cell
    elif c == 54:
        table_8['fifth_year_eps_original_continuing_operation'] = row_cell
    elif c == 55:
        table_8['fifth_year_eps_restated_continuing_operation'] = row_cell
    elif c == 56:
        table_8['fifth_year_eps_diluted_continuing_operation'] = row_cell
    elif c == 57:
        table_8['fifth_year_dividend'] = row_cell
    elif c == 58:
        table_8['fifth_year_dividend_yeild'] = row_cell
    #
    c = c + 1

table_8




# # Table 9
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[9].get_attribute('innerHTML'), 'html.parser')
table_9 = {}
for row in soup.find_all('tr'):
    row_header = row.th.get_text()
    row_cell = row.td.get_text()
    table_9[row_header] = row_cell

table_9



# print(soup.prettify(formatter='html'))


# Skipping this table for NOW
# # # Table 10
# soup = BeautifulSoup(d.find_elements(By.ID, 'company')[10].get_attribute('innerHTML'), 'html.parser')
# result = {}
# for row in soup.find_all('tr'):
#     row_header = row.th.get_text()
#     row_cell = row.td.get_text()
#     result[row_header] = row_cell

# result




# This table not needed - contact info ase
# # # Table 12
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[12].get_attribute('innerHTML'), 'html.parser')
result = {}

c = 0
for row in soup.find_all('td'):
    # row_header = row.th.get_text()
    row_cell = row.get_text()
    # result[row_header] = row_cell
    # print(c)
    # print(row_cell)
    if c == 5:
        result['present_shortterm_loan'] = row_cell
    elif c == 7:
        result['present_longterm_loan'] = row_cell
    elif c == 9:
        result['latest_dividend_status'] = row_cell
    elif c == 13:
        result['latest_credit_rating_shortterm_status'] = row_cell
    elif c == 15:
        result['latest_credit_rating_shortterm_status'] = row_cell
    elif c == 17:
        result['otc_delisting_relisting'] = row_cell
    c = c + 1

result




# # # Table 11
soup = BeautifulSoup(d.find_elements(By.ID, 'company')[11].get_attribute('innerHTML'), 'html.parser')
table_11 = {}

c = 0
for row in soup.find_all('td'):
    # row_header = row.th.get_text()
    row_cell = row.get_text()
    # result[row_header] = row_cell
    print(c)
    print(row_cell)
    if c == 5:
        table_11['present_shortterm_loan'] = row_cell
    elif c == 7:
        table_11['present_longterm_loan'] = row_cell
    elif c == 9:
        table_11['latest_dividend_status'] = row_cell
    elif c == 13:
        table_11['latest_credit_rating_shortterm_status'] = row_cell
    elif c == 15:
        table_11['latest_credit_rating_shortterm_status'] = row_cell
    elif c == 17:
        table_11['otc_delisting_relisting'] = row_cell
    c = c + 1

table_11



data_dict = {}
data_dict = table_0 | table_1 | table_2 | table_3 | table_6 | table_7 | table_8 | table_9 | table_11


# from collections import OrderedDict
# data_dict = OrderedDict(data_dict)
# data_dict = {}
# for d in [table_0, table_1, table_2, table_3, table_6, table_7, table_8, table_9, table_11]:
#     for k, v in d.items():  # d.items() in Python 3+
#         data_dict.setdefault(k, []).append(v)

import json
def pprint_dict(dic):
    print(json.dumps(dic,
                  sort_keys=False, indent=4))



pprint_dict(data_dict)


graph_idx = 4 # 4, 5, 6
options_idx = 0 # 0, 1, 2, 3, 4, 5
options = ['1 month', '3 monthes', '6 monthes', '9 monthes', '1 year', '2 years', ] 
d.find_elements(By.CLASS_NAME, 'form-control')[4].send_keys(options[options_idx])
d.switch_to.window(d.window_handles[1])
if graph_idx == 4:
    graph_type = 'Closing Price'
elif graph_idx == 5:
    graph_type = 'Total Trade'
elif graph_idx == 6:
    graph_type = 'Total Volume'
tmp = '/media/scarlet/Project/Project Files/DSE Scraper/Charts/' + data_dict['company_name'] + ' - ' + graph_type + ' - ' +  options[options_idx]  + '.jpeg'
d.save_full_page_screenshot(tmp)
d.close()
d.switch_to.window(d.window_handles[0])


# for row in soup.find_all('tr'):
#     columns = row.find_all('td')
#     if columns:
#         for i in columns:
#             print(i.text)




# for i in range(len(soup.find_all('td'))):
#      print(soup.find_all('td')[i])
#      print(i)
#      print()
