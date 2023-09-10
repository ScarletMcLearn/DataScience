# vars
DSE_URL = "https://dsebd.org/"
DSE_ALT_URL = "https://dsebd.com.bd/"

DSE_LSP_URL = "latest_share_price_scroll_l.php"
DSE_DEA_URL = "day_end_archive.php"
DSE_AGM_URL = "Company_AGM.htm"
DSE_LPE_URL = "latest_PE_all.php"
DSE_LPE_URL_2 = "latest_PE.php"
DSE_NEWS_URL = "old_news.php"
DSE_CLOSE_PRICE_URL = "dse_close_price_archive.php"
DSE_COMPANY_LIST_URL = "company_listing.php"

DSE_MARKET_INF_URL = "recent_market_information.php"
DSE_MARKET_INF_MORE_URL = "recent_market_information_more.php"
DSE_MARKET_DEPTH_URL = "ajax/load-instrument.php"

DSEX_INDEX_VALUE = "dseX_share.php"

CSE_URL = "https://www.cse.com.bd/"
CSE_LSP_URL = "market/current_price"


################################################
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
# from bdshare.util import vars as vs
from numpy import empty



from random import randint
import time, random
from datetime import datetime
import random
from tqdm import tqdm
import re
################################################

# import pandas as pd
# import bdshare as ds
# import os



# class Store(object):

#     def __init__(self, data=None, name=None, path=None):
#         if isinstance(data, pd.DataFrame):
#             self.data = data
#         else:
#             raise RuntimeError('data type is incorrect')
#         self.name = name
#         self.path = path

#     def save_as(self, name, path, to='csv'):
#         if name is None:
#             name = self.name
#         if path is None:
#             path = self.path
#         file_path = '%s%s%s.%s'
#         if isinstance(name) and name != '':
#             if (path is None) or (path == ''):
#                 file_path = '.'.join([name, to])
#             else:
#                 try:
#                     if os.path.exists(path) is False:
#                         os.mkdir(path) 
#                     file_path = file_path%(path, '/', name, to)
#                 except:
#                     pass
            
#         else:
#             print('input error')
            

################################################


def get_current_trade_data(symbol=None, retry_count=1, pause=0.001):
    """
        get last stock price.
        :param symbol: str, Instrument symbol e.g.: 'ACI' or 'aci'
        :return: dataframecd 
    """

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            r = requests.get(DSE_URL+DSE_LSP_URL)
            if r.status_code != 200:
                r = requests.get(DSE_ALT_URL+DSE_LSP_URL)
        except Exception as e:
            print(e)
        else:
            soup = BeautifulSoup(r.content, 'html5lib')
            quotes = []  # a list to store quotes
            table = soup.find('table', attrs={
                                'class': 'table table-bordered background-white shares-table fixedHeader'})

            # print(table)
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                quotes.append({'symbol': cols[1].text.strip().replace(",", ""),
                       'ltp': cols[2].text.strip().replace(",", ""),
                       'high': cols[3].text.strip().replace(",", ""),
                       'low': cols[4].text.strip().replace(",", ""),
                       'close': cols[5].text.strip().replace(",", ""),
                       'ycp': cols[6].text.strip().replace(",", ""),
                       'change': cols[7].text.strip().replace("--", "0"),
                       'trade': cols[8].text.strip().replace(",", ""),
                       'value': cols[9].text.strip().replace(",", ""),
                       'volume': cols[10].text.strip().replace(",", "")
                       })
            df = pd.DataFrame(quotes)
            if symbol:
                df = df.loc[df.symbol == symbol.upper()]
                return df
            else:
                return df


################################################

def get_dsex_data(symbol=None, retry_count=1, pause=0.001):
    """
        get dseX share price.
        :param symbol: str, Instrument symbol e.g.: 'ACI' or 'aci'
        :return: dataframe
    """

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            r = requests.get(DSE_URL+DSEX_INDEX_VALUE)
            if r.status_code != 200:
                r = requests.get(DSE_ALT_URL+DSEX_INDEX_VALUE)
        except Exception as e:
            print(e)
        else:
            soup = BeautifulSoup(r.content, 'html5lib')
            quotes = []  # a list to store quotes
            table = soup.find('table', attrs={
                                'class': 'table table-bordered background-white shares-table'})

            # print(table)
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                quotes.append({'symbol': cols[1].text.strip().replace(",", ""),
                       'ltp': cols[2].text.strip().replace(",", ""),
                       'high': cols[3].text.strip().replace(",", ""),
                       'low': cols[4].text.strip().replace(",", ""),
                       'close': cols[5].text.strip().replace(",", ""),
                       'ycp': cols[6].text.strip().replace(",", ""),
                       'change': cols[7].text.strip().replace("--", "0"),
                       'trade': cols[8].text.strip().replace(",", ""),
                       'value': cols[9].text.strip().replace(",", ""),
                       'volume': cols[10].text.strip().replace(",", "")
                       })
            df = pd.DataFrame(quotes)
            if symbol:
                df = df.loc[df.symbol == symbol.upper()]
                return df
            else:
                return df


################################################

def get_current_trading_code():
    """
        get last stock codes.
        :return: dataframe
    """
    try:
        r = requests.get(DSE_URL+DSE_LSP_URL)
        if r.status_code != 200:
            r = requests.get(DSE_ALT_URL+DSE_LSP_URL)
    except Exception as e:
            print(e)
    #soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.content, 'html5lib')
    quotes = []  # a list to store quotes
    table = soup.find('table', attrs={
                                'class': 'table table-bordered background-white shares-table fixedHeader'})
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        quotes.append({'symbol': cols[1].text.strip().replace(",", "")})
    df = pd.DataFrame(quotes)
    return df


################################################


def get_hist_data(start=None, end=None, code='All Instrument'):
    """
        get historical stock price.
        :param start: str, Start date e.g.: '2020-03-01'
        :param end: str, End date e.g.: '2020-03-02'
        :param code: str, Instrument symbol e.g.: 'ACI'
        :return: dataframe
    """
    # data to be sent to post request
    data = {'startDate': start,
            'endDate': end,
            'inst': code,
            'archive': 'data'}
    try:
        r = requests.get(url=DSE_URL+DSE_DEA_URL, params=data)
        if r.status_code != 200:
            r = requests.get(url=DSE_ALT_URL+DSE_DEA_URL, params=data)
    except Exception as e:
            print(e)

    #soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.content, 'html5lib')

    quotes = []  # a list to store quotes

    table = soup.find('table', attrs={
                      'class': 'table table-bordered background-white shares-table fixedHeader'})
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        quotes.append({'date': cols[1].text.strip().replace(",", ""),
                       'symbol': cols[2].text.strip().replace(",", ""),  # Need this for rest
                       'ltp': cols[3].text.strip().replace(",", ""),
                       'high': cols[4].text.strip().replace(",", ""),
                       'low': cols[5].text.strip().replace(",", ""),
                       'open': cols[6].text.strip().replace(",", ""),
                       'close': cols[7].text.strip().replace(",", ""),
                       'ycp': cols[8].text.strip().replace(",", ""),
                       'trade': cols[9].text.strip().replace(",", ""),
                       'value': cols[10].text.strip().replace(",", ""),
                       'volume': cols[11].text.strip().replace(",", "")
                       })
    df = pd.DataFrame(quotes)
    if 'date' in df.columns:
        df = df.set_index('date')
        df = df.sort_index(ascending=False)
    else:
        print('No data found')
    return df



################################################

def get_basic_hist_data(start=None, end=None, code='All Instrument', index=None, retry_count=1, pause=0.001):
    """
        get historical stock price.
        :param start: str, Start date e.g.: '2020-03-01'
        :param end: str, End date e.g.: '2020-03-02'
        :param code: str, Instrument symbol e.g.: 'ACI'
        :param retry_count : int, e.g.: 3
        :param pause : int, e.g.: 0
        :return: dataframe
    """
    # data to be sent to post request
    data = {'startDate': start,
            'endDate': end,
            'inst': code,
            'archive': 'data'}

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            r = requests.get(url=DSE_URL+DSE_DEA_URL, params=data)
            if r.status_code != 200:
                r = requests.get(url=DSE_ALT_URL+DSE_DEA_URL, params=data)
        except Exception as e:
            print(e)
        else:
            #soup = BeautifulSoup(r.text, 'html.parser')
            soup = BeautifulSoup(r.content, 'html5lib')

            # columns: date, open, high, close, low, volume
            quotes = []  # a list to store quotes

            table = soup.find('table', attrs={
                              'class': 'table table-bordered background-white shares-table fixedHeader'})

            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                quotes.append({'date': cols[1].text.strip().replace(",", ""),
                               'symbol': cols[2].text.strip().replace(",", ""), # Added this
                               'open': float(cols[6].text.strip().replace(",", "")),
                               'high': float(cols[4].text.strip().replace(",", "")),
                               'low': float(cols[5].text.strip().replace(",", "")),
                               'close': float(cols[7].text.strip().replace(",", "")),
                               'volume': int(cols[11].text.strip().replace(",", ""))
                               })
            df = pd.DataFrame(quotes)
            if 'date' in df.columns:
                if (index == 'date'):
                    df = df.set_index('date')
                    df = df.sort_index(ascending=True)
                df = df.sort_index(ascending=True)
            else:
                print('No data found')
            return df

################################################

        
def get_close_price_data(start=None, end=None, code='All Instrument'):
    """
        get stock close price.
        :param start: str, Start date e.g.: '2020-03-01'
        :param end: str, End date e.g.: '2020-03-02'
        :param code: str, Instrument symbol e.g.: 'ACI'
        :return: dataframe
    """
    # data to be sent to post request
    data = {'startDate': start,
            'endDate': end,
            'inst': code,
            'archive': 'data'}
    try:
        r = requests.get(url=DSE_URL+DSE_CLOSE_PRICE_URL, params=data)
        if r.status_code != 200:
            r = requests.get(url=DSE_ALT_URL+DSE_CLOSE_PRICE_URL, params=data)
    except Exception as e:
        print(e)
    else:
        soup = BeautifulSoup(r.content, 'html5lib')

        # columns: date, open, high, close, low, volume
        quotes = []  # a list to store quotes

        table = soup.find(
            'table', attrs={'class': 'table table-bordered background-white'})

        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            quotes.append({'date': cols[1].text.strip().replace(",", ""),
                        'symbol': cols[2].text.strip().replace(",", ""),
                        'close': cols[3].text.strip().replace(",", ""),
                        'ycp': cols[4].text.strip().replace(",", "")
                        })
        df = pd.DataFrame(quotes)
        if 'date' in df.columns:
            df = df.set_index('date')
            df = df.sort_index(ascending=False)
        else:
            print('No data found')
        return df


################################################

def get_last_trade_price_data():
    df = pd.read_fwf('https://dsebd.org/datafile/quotes.txt', sep='\t', skiprows=4)
    return df



################################################

def get_cse_current_trade_data(symbol=None):
    """
        get last stock price.
        :param symbol: str, Instrument symbol e.g.: 'ACI' or 'aci'
        :return: dataframe
    """
    try:
        r = requests.get(CSE_URL+CSE_LSP_URL)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = []  # a list to store quotes
    table = soup.find('table', attrs={'id': 'dataTable'})
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        quotes.append({'symbol': cols[1].text.strip().replace(",", ""),
                       'ltp': cols[2].text.strip().replace(",", ""),
                       'open': cols[3].text.strip().replace(",", ""),
                       'high': cols[4].text.strip().replace(",", ""),
                       'low': cols[5].text.strip().replace(",", ""),
                       'ycp': cols[6].text.strip().replace(",", ""),
                       'trade': cols[7].text.strip().replace(",", ""),
                       'value': cols[8].text.strip().replace(",", ""),
                       'volume': cols[9].text.strip().replace(",", "")
                       })
    df = pd.DataFrame(quotes)
    if symbol:
        df = df.loc[df.symbol == symbol.upper()]
        return df
    else:
        return df
    
 
################################################


def get_agm_news():
    """
        get stock agm declarations.
        :return: dataframe
    """
    try:
        r = requests.get(DSE_URL+DSE_AGM_URL)
    except Exception as e:
        print(e)
    #soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.content, 'html5lib')
    news=[] # a list to store quotes 

    table = soup.find('table') 

    for row in table.find_all('tr')[4:-6]:
        cols = row.find_all('td')
        news.append({'company': cols[0].text.strip(), 
                    'yearEnd': cols[1].text.strip(),
                    'dividend': cols[2].text.strip(),
                    'agmData': cols[3].text.strip(),
                    'recordDate': cols[4].text.strip(),
                    'vanue': cols[5].text.strip(),
                    'time': cols[6].text.strip()
                        })
    df = pd.DataFrame(news)
    return df

################################################

def get_all_news(code=None):
    """
        get dse news.
        :param start: str, Start date e.g.: '2020-03-01'
        :param end: str, End date e.g.: '2020-03-02'
        :param code: str, Instrument symbol e.g.: 'ACI'
        :return: dataframe
    """
    # data to be sent to post request
    data = {'inst': code,
            'criteria': 3,
            'archive': 'news'}
    try:
        r = requests.post(url = DSE_URL+DSE_NEWS_URL, params=data) 
    except Exception as e:
        print(e)

    #soup = BeautifulSoup(r.text, 'html.parser')
    soup = BeautifulSoup(r.content, 'html5lib')

    # columns: Trading Code, News, Post Date
    news=[] # a list to store quotes 


    table = soup.find('table', attrs={'class' : 'table-news'})

    for row in table.find_all('tr'):
        heads = row.find_all('th')
        cols = row.find_all('td')
        if cols:
            if heads[0].text.strip() == "News Title:":
                news.append({"News Title": cols[0].text.strip()})
            elif heads[0].text.strip() == "News:":
                news.append({"News": cols[0].text.strip()})
            elif heads[0].text.strip() == "Post Date:":
                news.append({"Post Date": cols[0].text.strip()})
    df = pd.DataFrame(news)
    return df

################################################

def get_market_inf():
    """
        get stock market information.
        :return: dataframe
    """
    r = requests.get(DSE_URL+DSE_MARKET_INF_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = []  # a list to store quotes

    table = soup.find('table', attrs={'class': 'table table-bordered background-white text-center', '_id': 'data-table'})

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        quotes.append({'Date': cols[0].text.strip().replace(",", ""),
                       
                       'Total Trade': cols[1].text.strip().replace(",", ""),
                       'Total Volume': cols[2].text.strip().replace(",", ""),
                       'Total Value (mn)': cols[3].text.strip().replace(",", ""),
                       'Total Market Cap. (mn)': cols[4].text.strip().replace(",", ""),
                       'DSEX Index': cols[5].text.strip().replace(",", ""),
                       'DSES Index': cols[6].text.strip().replace(",", ""),
                       'DS30 Index': cols[7].text.strip().replace(",", ""),
                       'DGEN Index': cols[8].text.strip().replace(",", "")
        })
    df = pd.DataFrame(quotes)
    return df

################################################

def get_latest_pe():
    """
        get last stock P/E.
        :return: dataframe
    """
    r = requests.get(DSE_URL+DSE_LPE_URL_2)
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = []  # a list to store quotes
    table = soup.find('table')
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        quotes.append((cols[1].text.strip().replace(",", ""),
                       cols[2].text.strip().replace(",", ""),
                       cols[3].text.strip().replace(",", ""),
                       cols[4].text.strip().replace(",", ""),
                       cols[5].text.strip().replace(",", ""),
                       cols[6].text.strip().replace(",", ""),
                       cols[7].text.strip().replace(",", ""),
                       cols[8].text.strip().replace(",", ""),
                       cols[9].text.strip().replace(",", "")
                       ))
    df = pd.DataFrame(quotes)
    return df

################################################


def get_market_inf_more_data(start=None, end=None, index=None, retry_count=3, pause=0.001):
    """
        get historical stock price.
        :param start: str, Start date e.g.: '2020-03-01'
        :param end: str, End date e.g.: '2020-03-02'
        :param retry_count : int, e.g.: 3
        :param pause : int, e.g.: 0
        :return: dataframe
    """
    # data to be sent to post request
    data = {'startDate': start,
            'endDate': end,
            'searchRecentMarket': 'Search Recent Market'}

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            r = requests.post(
                url=DSE_URL+DSE_MARKET_INF_MORE_URL, data=data)
        except Exception as e:
            print(e)
        else:
            #soup = BeautifulSoup(r.text, 'html.parser')
            soup = BeautifulSoup(r.content, 'html5lib')

            quotes = []  # a list to store quotes

            table = soup.find('table', attrs={
                              'class': 'table table-bordered background-white text-center'})

            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                quotes.append({'Date': cols[0].text.strip().replace(",", ""),
                               'Total Trade': int(cols[1].text.strip().replace(",", "")),
                               'Total Volume': int(cols[2].text.strip().replace(",", "")),
                               'Total Value in Taka(mn)': float(cols[3].text.strip().replace(",", "")),
                               'Total Market Cap. in Taka(mn)': float(cols[4].text.strip().replace(",", "")),
                               'DSEX Index': float(cols[5].text.strip().replace(",", "")),
                               'DSES Index': float(cols[6].text.strip().replace(",", "")),
                               'DS30 Index': float(cols[7].text.strip().replace(",", "")),
                               'DGEN Index': float(cols[8].text.strip().replace("-", "0"))
                               })
            df = pd.DataFrame(quotes)
            if 'date' in df.columns:
                if (index == 'date'):
                    df = df.set_index('date')
                    df = df.sort_index(ascending=True)
                df = df.sort_index(ascending=True)
            else:
                print('No data found')
            return df

################################################


def get_market_depth_data(index=None, retry_count=3, pause=0.001):
    """
        get market depth data.
        :param index: str, End date e.g.: 'aci'
        :param retry_count : int, e.g.: 3
        :param pause : int, e.g.: 0
        :return: dataframe
    """
    # data to be sent to post request
    data = {'inst': index}

    for _ in range(retry_count):
        time.sleep(pause)
        try:
            r = requests.post(
                url=DSE_URL+DSE_MARKET_DEPTH_URL, params=data)
            if r.status_code != 200:
                r = requests.post(url=DSE_ALT_URL +
                                  DSE_MARKET_DEPTH_URL, params=data)
        except Exception as e:
            print(e)
        else:
            #soup = BeautifulSoup(r.text, 'html.parser')
            soup = BeautifulSoup(r.content, 'html5lib')

            # columns: date, open, high, close, low, volume
            quotes = []  # a list to store quotes

            table = soup.find('table', attrs={
                              'class': 'table table-stripped'})

            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                quotes.append({'date': cols[0].text.strip().replace(",", ""),
                               'Total Trade': int(cols[1].text.strip().replace(",", "")),
                               'Total Volume': int(cols[2].text.strip().replace(",", "")),
                               'Total Value in Taka(mn)': float(cols[3].text.strip().replace(",", "")),
                               'Total Market Cap. in Taka(mn)': float(cols[4].text.strip().replace(",", "")),
                               'DSEX Index': float(cols[5].text.strip().replace(",", "")),
                               'DSES Index': float(cols[6].text.strip().replace(",", "")),
                               'DS30 Index': float(cols[7].text.strip().replace(",", "")),
                               'DGEN Index': float(cols[8].text.strip().replace("-", "0"))
                               })
            df = pd.DataFrame(quotes)
            if 'date' in df.columns:
                if (index == 'date'):
                    df = df.set_index('date')
                    df = df.sort_index(ascending=True)
                df = df.sort_index(ascending=True)
            else:
                print('No data found')
            return df
        
################################################
        
debug = False
def get_co_data(co_name):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents here...
        # ...
    ]
    
    
    
    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)
    
    # Create a session object
    session = requests.Session()
    
    # Set the user agent as a header for the session
    session.headers.update({'User-Agent': random_user_agent,
                            'Accept': 'text/plain'})
    
    url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'
    
    # Make a request using the session
    response = session.get(url)
    
    
    
    # soup = BeautifulSoup(response.text)
    html_content = response.content
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    all_tr = soup.findAll('div', class_='table-responsive inner-scroll')[0].findAll('tr')
    
    tmp_c = 0
    
    for j in all_tr[1:]:   
        curr_tr_data = j.findAll('td')
        for i in range(len(curr_tr_data)):
            if i == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                serial=curr_tr_data[i].text
                pass
            if i % 10 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    volume = 0
                else: 
                    volume = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 9 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    value_of_trades = 0
                else: 
                    value_of_trades = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 8 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    number_of_trades = 0
                else: 
                    number_of_trades = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 7 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    percentage_change = 0
                else: 
                    percentage_change = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 6 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    yesterday_close_price = 0
                else: 
                    yesterday_close_price = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 5 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    close_price = 0
                else:
                    close_price = float(curr_tr_data[i].text.replace(',', '')) 
                pass
            elif i % 4 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    last_low = 0
                else:
                    last_low = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 3 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    last_high = 0
                else:
                    last_high = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 2 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    last_trading_price = 0
                else:
                    last_trading_price = float(curr_tr_data[i].text.replace(',', ''))
                pass
            elif i % 1 == 0:
                if debug==True:
                    print(str(i) , " : ", curr_tr_data[i])
                if curr_tr_data[i].text == '--':
                    trading_code = 'None'
                else:
                    trading_code = re.sub(r'[^a-zA-Z0-9]', '', curr_tr_data[i].text)
                pass
                
        curr_co_data = {
                        'serial':serial,
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
            # continue
        tmp_c=tmp_c+1
        if trading_code == co_name:
            if debug==True:
                print('Breaking')
            return curr_co_data
            break        

            
################################################

def get_losers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents here...
        # ...
    ]
    
    

    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)

    # Create a session object
    session = requests.Session()

    # Set the user agent as a header for the session
    session.headers.update({'User-Agent': random_user_agent,
                                'Accept': 'text/plain'})

    # url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'

    url = 'https://dsebd.org/top_ten_loser.php'

    # Make a request using the session
    response = session.get(url)



    # soup = BeautifulSoup(response.text)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    co_list = []

    for table in soup.findAll('div', class_='table-responsive'):
        table_rows = table.findAll('tr')
        for curr_row in table_rows:
            try:
                co_text = curr_row.findAll('td')[1].text.strip()
                if len(co_text) < 23 and len(co_text) > 2:
                    co_list.append(co_text)
            except:
                pass

    co_list = set(co_list)
    
    return co_list


################################################

def get_gainers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents here...
        # ...
    ]
    
    

    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)

    # Create a session object
    session = requests.Session()

    # Set the user agent as a header for the session
    session.headers.update({'User-Agent': random_user_agent,
                                'Accept': 'text/plain'})

    # url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'

    url = 'https://dsebd.org/top_ten_gainer.php'

    # Make a request using the session
    response = session.get(url)



    # soup = BeautifulSoup(response.text)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    co_list = []

    for table in soup.findAll('div', class_='table-responsive'):
        table_rows = table.findAll('tr')
        for curr_row in table_rows:
            try:
                co_text = curr_row.findAll('td')[1].text.strip()
                if len(co_text) < 23 and len(co_text) > 2:
                    co_list.append(co_text)
            except:
                pass

    co_list = set(co_list)
    
    return co_list

################################################

def get_top_shares():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents here...
        # ...
    ]
    
    

    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)

    # Create a session object
    session = requests.Session()

    # Set the user agent as a header for the session
    session.headers.update({'User-Agent': random_user_agent,
                                'Accept': 'text/plain'})

    # url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'

    url = 'https://dsebd.org/top_20_share.php'

    # Make a request using the session
    response = session.get(url)



    # soup = BeautifulSoup(response.text)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    co_list = []

    for table in soup.findAll('div', class_='table-responsive'):
        table_rows = table.findAll('tr')
        for curr_row in table_rows:
            try:
                co_text = curr_row.findAll('td')[1].text.strip()
                if len(co_text) < 23 and len(co_text) > 2:
                    co_list.append(co_text)
            except:
                pass

    co_list = set(co_list)
    
    return co_list


################################################

def get_investing_url(co_name):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents here...
        # ...
    ]
    
    

    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)

    # Create a session object
    session = requests.Session()

    # Set the user agent as a header for the session
    session.headers.update({'User-Agent': random_user_agent,
                                    'Accept': 'text/plain'})

    # url = 'https://www.dsebd.org/latest_share_price_scroll_l.php'

    url = 'https://www.google.com/search?client=firefox-b-lm&q=investing.com+' + co_name

    # Make a request using the session
    response = session.get(url)
    
    # soup = BeautifulSoup(response.text)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    links = soup.findAll("a", href=True)

    c = 0
    for link in links:
        if c==10:
            return link['href']
        
################################################

import time

def get_co_tech_investing(url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')

    user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            # Add more user agents here...
            # ...
        ]

    # Randomly select a user agent
    random_user_agent = random.choice(user_agents)

    options.add_argument(f'user-agent={random_user_agent}')


    # Set a user agent string to mimic a real browser
    options.set_preference("general.useragent.override", random_user_agent)
    # Disable browser automation detection features (this may change over time)
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)

    # Disable permissions prompt for notifications
    options.set_preference("permissions.default.desktop-notification", 1)

    # Disable the "navigator.webdriver" property
    options.set_preference("webdriver.firefox.profile", "default")

    # Set a custom window size to mimic a real browser
    options.add_argument("--window-size=1920,1080")

    d = webdriver.Firefox(options=options)
    
    
    start_time = time.time()
    d.get(url)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for getting investing.com data: {execution_time} seconds")

    

    soup = BeautifulSoup(d.page_source, 'html.parser')

    d.close()
    
    prev_close = data[0].text
    open_ = data[1].text
    day_range_start = data[2].text
    day_range_end = data[3].text
    week_range_52_start = data[4].text
    week_range_52_end = data[5].text
    vol = data[6].text
    avg_vol = data[7].text
    year_chng = data[8].text
    outstanding_shares = data[9].text
    market_cap = data[10].text
    revenue = data[11].text
    pe_ratio = data[12].text
    eps = data[13].text
    dividend_yield = data[14].text
    dividend_yield_percentage = data[15].text
    beta = data[16].text
    # next_earning_date = data[17].text
    
    return {
            'prev_close' : data[0].text,
            'open_' : data[1].text,
            'day_range_start' : data[2].text,
            'day_range_end' : data[3].text,
            'week_range_52_start' : data[4].text,
            'week_range_52_end' : data[5].text,
            'vol' : data[6].text,
            'avg_vol' : data[7].text,
            'year_chng' : data[8].text,
            'outstanding_shares' : data[9].text,
            'market_cap' : data[10].text,
            'revenue' : data[11].text,
            'pe_ratio' : data[12].text,
            'eps' : data[13].text,
            'dividend_yield' : data[14].text,
            'dividend_yield_percentage' : data[15].text,
            'beta' : data[16].text,
           }




################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################

################################################


