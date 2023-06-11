###################################################################
#
#
# ########## Get Company Data
#
#
####################################################################
import random
import requests
from bs4 import BeautifulSoup
import re

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
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random
from bokeh.plotting import figure, show, curdoc
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
import random
from bokeh.models import ContinuousColorMapper
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
from bokeh.palettes import Turbo256
from bokeh.palettes import Category10, Category20, Category20b, Category20c
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
from bokeh.models import LinearColorMapper
from tqdm import tqdm
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from bokeh.models import Legend, LegendItem

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
    # if cmap_cond==True:
    #     mapper = linear_cmap(field_name="y", palette=Turbo256, 
    #                  low=100, high=0)
    #     color = mapper
        # border_color = mapper
        # fill_color = mapper
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
    return figure, item

# Perfection Here
#######################################################################################




# Experimenting here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import requests
from bs4 import BeautifulSoup
import random
import time

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource
from bokeh.models.formatters import DatetimeTickFormatter
from functools import partial
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import WheelZoomTool
from datetime import datetime
from random import randint
from functools import partial




# Define the global variables for the streaming data
x_values = []
y_1_values = []
# y_2_values = []

# Create a ColumnDataSource to store the data
source = ColumnDataSource(data=dict(x=x_values, y1=y_1_values, 
                                    # y2=y_2_values)
                                   ))

# Create the figure
# p = figure(
#     title="Dhaka Stock Exchange Live Change",
#     x_axis_type="datetime",
#     sizing_mode="scale_both",
#     max_width=900,
#     max_height=300,
#     width=900,
#     height=900
# )
p = figure(x_axis_type='datetime', 
           y_range=(0, 100),
           width=2150, height=950, 
           # tools='pan,reset'
           title="Dhaka Stock Exchange Live Change",
           # sizing_mode='stretch_both',
          )


p.title.align = "center"
# Set x-axis and y-axis labels
p.xaxis.axis_label = "Date-Time"
p.yaxis.axis_label = "Percentage Change (%)"

p.xaxis.formatter = DatetimeTickFormatter(hours="%H:%M")

curdoc().theme = 'dark_minimal'

# # Draw shapes function
# def draw_shape(figure, source, x_col_name, y_col_name, shape, size, fill_color, border_color, border_width, alpha, line_dash, line_alpha, line_cap, line_join, line_smoothing):
#     if shape == 'circle' or shape == 'c':
#         item = figure.circle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
#     elif shape == 'line' or shape == 'l':
#         item = figure.line(x=x_col_name, y=y_col_name, source=source, line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=line_alpha, line_cap=line_cap, line_join=line_join)
#     return figure, item

# Function to periodically update the data

# Add a line renderer
line = p.line(x='x', y='y1', source=source)

def update_data():
        # value_1 = random.randint(0, 10)
        # # value_2 = random.random()
        # new_data = dict(
        #     x=source.data['x'] + [source.data['x'][-1] + 1] if source.data['x'] else [0],
        #     y1=source.data['y1'] + [value_1],
        # )

        # # Update the data
        # source.data = new_data

        # # Update the x-range of the plot to show the latest points
        # if len(source.data['x']) >= 10:
        #     p.x_range.start = source.data['x'][-10]
        # p.x_range.end = source.data['x'][-1]
    
        # # Update the y-range of the plot
        # p.y_range.start = min(source.data['y1']) - 1
        # p.y_range.end = max(source.data['y1']) + 1

        # # y_2_values.append(value_2)
        # source.data = dict(x=x_values, y1=y_1_values, 
        #                    # y2=y_2_values
        #                   )

        # # Pause for a while before updating again
        # time.sleep(1)
        new_data = dict(
        x=[datetime.now()],
        y1=[randint(0, 100)]
    )
        source.stream(new_data, 
                      # 100
                      1000
                     )

# Configure the document
curdoc().add_root(column(p))

# Add the periodic callback to update the data
curdoc().add_periodic_callback(update_data, 1000)


# Perfection

# callback = partial(update_data)

# update_data()

# # Update the lines with random data
# def update_data():
#     new_data = dict(
#         x=source.data['x'] + [source.data['x'][-1] + 1] if source.data['x'] else [0],
#         y1=source.data['y1'] + [randint(0, 10)],
#         y2=source.data['y2'] + [randint(0, 10)],
#         y3=source.data['y3'] + [randint(0, 10)],
#         y4=source.data['y4'] + [randint(0, 10)]
#     )
#     source.data = new_data

#     # Update the x-range of the plot to show the latest points
#     if len(source.data['x']) >= 10:
#         p.x_range.start = source.data['x'][-10]
#     p.x_range.end = source.data['x'][-1]

#     # Update the y-range of the plot
#     p.y_range.start = min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1
#     p.y_range.end = max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1


# Start updating the data in a separate thread
# curdoc().add_root(p)
# curdoc().add_periodic_callback(callback, 1000)  # Update every second
# curdoc().title = "Streaming Plot"

# curdoc()

