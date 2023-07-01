###################################################################
#
#
# ############### Import necessary libraries
#
#
###################################################################
import requests
from bs4 import BeautifulSoup
from bokeh.plotting import figure, curdoc, show
from bokeh.models.formatters import DatetimeTickFormatter
from functools import partial
from bokeh.layouts import column
from bokeh.io import curdoc
from random import randint
from colorama import Fore, Style
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random
from bokeh.models import DatetimeTickFormatter, ColumnDataSource, ContinuousColorMapper, WheelZoomTool, HoverTool, LinearColorMapper, Legend, LegendItem, SingleIntervalTicker, DatetimeTicker
from datetime import datetime
# from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
from bokeh.palettes import Turbo256
# from bokeh.palettes import Category10, Category20, Category20b, Category20c
from bokeh.plotting import figure, show
from tqdm import tqdm
import pandas as pd
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime, timedelta
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pickle 








def generate_shared_data():
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


    # Create a Retry object with desired parameters
    retry_strategy = Retry(
        total=3,  # Maximum number of retries
        backoff_factor=1,  # Exponential backoff factor
        status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry on
    )

    https_adapter = HTTPAdapter(max_retries=retry_strategy, )

    session.mount('https://', https_adapter)
    
    # Make a request using the session
    response = session.get(url, timeout=60)
    
    
    
    # soup = BeautifulSoup(response.text)
    html_content = response.content

    fname = 'temp ' + datetime.now().date().isoformat()  + ' shared_data.pickle'

    with open(fname, 'wb') as file:
        pickle.dump(html_content, file)
        file.close()


def read_shared_data():
    fname = 'temp ' + datetime.now().date().isoformat()  + ' shared_data.pickle'
    with open(fname, 'rb') as file:
        html_content = pickle.load(file)
        file.close()
    return html_content

###################################################################
#
#
# ########## Get Company Data
#
#
####################################################################
# New version
debug = False



# Added this - LRU Cache
from functools import lru_cache
@lru_cache(maxsize=10)
def get_all_data():
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


    # Create a Retry object with desired parameters
    retry_strategy = Retry(
        total=3,  # Maximum number of retries
        backoff_factor=1,  # Exponential backoff factor
        status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry on
    )

    https_adapter = HTTPAdapter(max_retries=retry_strategy, )

    session.mount('https://', https_adapter)
    
    # Make a request using the session
    response = session.get(url, timeout=60)
    
    
    
    # soup = BeautifulSoup(response.text)
    html_content = response.content
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    all_tr = soup.findAll('div', class_='table-responsive inner-scroll')[0].findAll('tr')
    return all_tr
    
    
def get_co_data(co_name, all_tr):
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

        
        val_1 = trading_code + '_Serial'
        val_2 = trading_code + '_Company_Name'
        val_3 = trading_code + '_LTP'
        val_4 = trading_code + '_LH'
        val_5 = trading_code + '_LL'
        val_6 = trading_code + '_CP'
        val_7 = trading_code + '_YCP'
        val_8 = trading_code + '_PC'
        val_9 = trading_code + '_NoT'
        val_10 = trading_code + '_VoT'
        val_11 = trading_code + '_Vol'
        val_12 = trading_code + '_Size'

        sz = 30 + float(value_of_trades/100) 
        # vot = value_of_trades 
        # if vot == 0:
        #     vot = 1
        # sz = 30 + (1.0 / float(vot))

        
        

        curr_co_data = {
                        val_1:[serial],
                        val_2:[trading_code],
                        val_3:[last_trading_price],
                        val_4:[last_high],
                        val_5:[last_low],
                        val_6:[close_price],
                        val_7:[yesterday_close_price],
                        val_8:[percentage_change],
                        val_9:[number_of_trades],
                        val_10:[value_of_trades],
                        val_11:[volume],  
                        val_12:[sz],
                        }
            # continue
        tmp_c=tmp_c+1
        if trading_code == co_name:
            if debug==True:
                print('Breaking')
            return curr_co_data
            break


# Commenting for testing - Will need to uncomment during SHOW TIME
# curr_co_data = get_co_data(co_name='AAMRATECH')

# print(curr_co_data)



######################################################################################
#
#
# Utilities to draw graphs
#
#
#######################################################################################
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


def generate_datetime_objects(no_of_obj, no_already_avail):
    x_values = []
    current_datetime = datetime.now()

    for i in range(no_already_avail, no_already_avail + no_of_obj):
        start_datetime = current_datetime.replace(hour=i + 1, minute=0, second=0, microsecond=0)
        end_datetime = current_datetime.replace(hour=i + 2, minute=0, second=0, microsecond=0)
        new_datetime = start_datetime + timedelta(seconds=random.randint(0, int((end_datetime - start_datetime).total_seconds())))

        x_values.append(new_datetime)

    return x_values

def generate_random_floats(n_of_obj):
    return [random.uniform(0, 100) for _ in range(n_of_obj)]

def draw_shape(figure, source, x_col_name, y_col_name, shape, size, fill_color, border_color, border_width, alpha, line_dash, line_alpha, line_cap, line_join, line_smoothing,):
    if shape=='circle' or shape=='c':
        item = figure.circle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square' or shape=='s':
        item = figure.square(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond' or shape=='d':
        item = figure.diamond(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='triangle' or shape=='t':
        item = figure.triangle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='cross' or shape=='+':
        item = figure.cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='X' or shape=='x':
        item = figure.x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='asterisk' or shape=='*':
        item = figure.asterisk(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_cross' or shape=='c+':
        item = figure.circle_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_x' or shape=='cx':
        item = figure.circle_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='inverted_triangle' or shape=='it':
        item = figure.inverted_triangle(x=x_col_name, y=y_col_name, source=source,  size=size, fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_cross' or shape=='s+':
        item = figure.square_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_x' or shape=='sx':
        item = figure.square_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='plus' or shape=='p':
        item = figure.plus(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_cross' or shape=='d+':
        item = figure.diamond_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_x' or shape=='dx':
        item = figure.diamond_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='hex' or shape=='h':
        item = figure.hex(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='y':
        item = figure.y(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='-' or shape=='dash':
        item = figure.dash(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='line' or shape=='l':
        # Line cap / line join : "butt", "round", or "square"
        # miter, round or bevel
        item = figure.line(x=x_col_name, y=y_col_name, source=source, #size=size, 
               # fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=alpha,  line_cap=line_cap, line_join=line_join, 
               # line_smoothing=line_smoothing
              )
    return figure, item


mapper = linear_cmap(field_name="y1", palette=Turbo256, 
                     low=100, high=0)

def draw_shape_line(x_col_name, y_col_name, source, figure, label, shape):
    mapper = linear_cmap(field_name=y_col_name, palette=Turbo256, 
                     low=100, high=0)
    p, i2 = draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape=shape, size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.55, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

    p, i3 = draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape='l', size=30, fill_color='blue', border_color='white', border_width=6, alpha=0.5, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='10 10', )
    
    legend_item = LegendItem(label=label, renderers=[i2, i3])

    return p, legend_item, i2, i3





def updated_draw_shape(figure, source, x_col_name, y_col_name, shape, size, fill_color, border_color, border_width, alpha, line_dash, line_alpha, line_cap, line_join, line_smoothing,):
    if shape=='circle' or shape=='c':
        item = figure.circle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square' or shape=='s':
        item = figure.square(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond' or shape=='d':
        item = figure.diamond(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='triangle' or shape=='t':
        item = figure.triangle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='cross' or shape=='+':
        item = figure.cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='X' or shape=='x':
        item = figure.x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='asterisk' or shape=='*':
        item = figure.asterisk(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_cross' or shape=='c+':
        item = figure.circle_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_x' or shape=='cx':
        item = figure.circle_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='inverted_triangle' or shape=='it':
        item = figure.inverted_triangle(x=x_col_name, y=y_col_name, source=source,  size=size, fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_cross' or shape=='s+':
        item = figure.square_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_x' or shape=='sx':
        item = figure.square_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='plus' or shape=='p':
        item = figure.plus(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_cross' or shape=='d+':
        item = figure.diamond_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_x' or shape=='dx':
        item = figure.diamond_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='hex' or shape=='h':
        item = figure.hex(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='y':
        item = figure.y(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='-' or shape=='dash':
        item = figure.dash(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='line' or shape=='l':
        # Line cap / line join : "butt", "round", or "square"
        # miter, round or bevel
        item = figure.line(x=x_col_name, y=y_col_name, source=source, #size=size, 
               # fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=alpha,  line_cap=line_cap, line_join=line_join, 
               # line_smoothing=line_smoothing
              )
        # Final line
    # figure.line(x=x_col_name, y=y_col_name, source=source, #size=size, 
    #            # fill_color=fill_color, 
    #             line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=alpha,  line_cap=line_cap, line_join=line_join, 
               # line_smoothing=line_smoothing
              # )
    return item






import sys

def updated_draw_shape_line(x_col_name, y_col_name, source, figure, label, shape, line_no, color, size_helper):
    

    size = 30
    i2 = updated_draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape=shape, size=size_helper, fill_color=color, border_color='white', border_width=3, alpha=0.55, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

    i3 = updated_draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape='l', size=size, fill_color='blue', border_color='white', border_width=6, alpha=0.5, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='10 10', )
    
    legend_item = LegendItem(label=label, renderers=[i2, i3])

    return legend_item, i2, i3


