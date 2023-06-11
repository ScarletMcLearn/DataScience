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
from bokeh.models import DatetimeTickFormatter, ColumnDataSource, ContinuousColorMapper, WheelZoomTool, HoverTool, LinearColorMapper, Legend, LegendItem, SingleIntervalTicker, DatetimeTicker, HoverTool
from datetime import datetime
import random
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




###################################################################
#
#
# ########## Get Company Data
#
#
####################################################################
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
        # Final line
    # figure.line(x=x_col_name, y=y_col_name, source=source, #size=size, 
    #            # fill_color=fill_color, 
    #             line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=alpha,  line_cap=line_cap, line_join=line_join, 
               # line_smoothing=line_smoothing
              # )
    return figure, item


def draw_shape_line(x_col_name, y_col_name, source, figure, label, shape):
    p, i2 = draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape=shape, size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.55, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

    p, i3 = draw_shape(x_col_name=x_col_name, y_col_name=y_col_name, source=source, figure=figure, shape='l', size=30, fill_color='blue', border_color='white', border_width=6, alpha=0.5, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='10 10', )
    
    legend_item = LegendItem(label=label, renderers=[i2, i3])

    # legend = Legend(items=[legend_item], location="top_left", orientation="vertical")

    # # Add the legend to the figure
    # p.add_layout(legend)

    return p, legend_item, i2, i3



p = figure(x_axis_type='datetime', 
           y_range=(-100, 100),
           # x_range = (0, 100),
           width=2150, height=950, 
           # tools='pan,reset'
           title="Dhaka Stock Exchange Live Change",
           # sizing_mode='stretch_both',
          )


p.title.align = "center"
# Set x-axis and y-axis labels
p.xaxis.axis_label = "Date-Time"
p.yaxis.axis_label = "Percentage Change (%)"

p.xaxis.ticker = DatetimeTicker()

# Customize the time axis
p.xaxis.formatter = DatetimeTickFormatter(
                                          days ="%dth %B - %I:%M:%S %p",
                                          months ="%dth %B - %I:%M:%S %p",
                                          hours="%dth %B - %I:%M:%S %p",
                                          minutes="%dth %B - %I:%M:%S %p",
                                          seconds="%dth %B - %I:%M:%S %p",
                                         )

curdoc().theme = 'dark_minimal'




mapper = linear_cmap(field_name="y1", palette=Turbo256, 
                     low=100, high=0)


# Get the script start time
start_time = datetime.now()

# p.xaxis.ticker = SingleIntervalTicker(interval=3*1000)  # Interval in milliseconds


# # Create a custom ticker with 3-second intervals
# ticker = SingleIntervalTicker(interval=3000)  # 3000 milliseconds = 3 seconds
# p.xaxis[0].ticker = ticker

# Define the global variables for the streaming data
x_values = []
y_1_values = []
y_2_values = []

AAMRANET_values = []
AAMRATECH_values = []
ABBANK_values = []


# Create a ColumnDataSource to store the data
source = ColumnDataSource(data=dict(x=x_values, y1=y_1_values, 
                                    y2=y_2_values,
                                    AAMRANET=AAMRANET_values,
                                    AAMRATECH=AAMRATECH_values,
                                    ABBANK=ABBANK_values,
                                   ))



p, l1, ia1, ib1 = draw_shape_line(x_col_name='x', y_col_name='y1', source=source, figure=p, label='Testy time', shape='c')

p, l2, ia2, ib2 = draw_shape_line(x_col_name='x', y_col_name='AAMRANET', source=source, figure=p, label='AAMRANET', shape='s')

p, l3, ia3, ib3 = draw_shape_line(x_col_name='x', y_col_name='AAMRATECH', source=source, figure=p, label='AAMRATECH', shape='t')

p, l4, ia4, ib4 = draw_shape_line(x_col_name='x', y_col_name='ABBANK', source=source, figure=p, label='ABBANK', shape='h')



x_tooltip_label = 'Date time'
x_tooltip_data = '@x{%dth %B - %I:%M:%S %p}'
y_tooltip_label = 'Percentage change'
tooltip_title = 'Company Data'




# # This is working
# # Create a HoverTool and configure it
hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})



# Add the HoverTool to the figure
# p.add_tools(hover_tool_1)

hover_tool_2 = HoverTool(renderers=[ia2, ib2], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRANET')], formatters={'@x': 'datetime'})
# p.add_tools(hover_tool_2)


hover_tool_3 = HoverTool(renderers=[ia3, ib3], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRATECH')], formatters={'@x': 'datetime'})
# p.add_tools(hover_tool_3)

hover_tool_4 = HoverTool(renderers=[ia4, ib4], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@ABBANK')], formatters={'@x': 'datetime'})



p.add_tools(
    hover_tool_1,
    hover_tool_2, hover_tool_3, hover_tool_4)





# Perfection Here
#######################################################################################




# Experimenting here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############################
#
#
# Experimenting here

# Create a HoverTool and configure it
# Increase font size using CSS styles
# hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # Increase font size using CSS styles
# hover_tool_1.tooltips = [(tooltip_title, ''),
#                         (x_tooltip_label, x_tooltip_data),
#                         (y_tooltip_label, '@y1')]


# # Create a HoverTool and configure it
# # hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # # Increase font size using CSS styles
# # hover_tool_1.tooltips = [(tooltip_title, ''),
# #                         (x_tooltip_label, x_tooltip_data),
# #                         (y_tooltip_label, '@y1')]

# # Add the HoverTool to the figure
# p.add_tools(hover_tool_1)



# TOOLTIPS = """
#     <div style="display: flex; justify-content: center;">
#         <div>
#             <span style="font-size: 17px; font-weight: bold;">@desc</span>
#         </div>
#         </div>
# """

# # Create a HoverTool and configure it
# hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(TOOLTIPS, ''), (tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # Add the HoverTool to the figure
# # p.add_tools(hover_tool_1)

# hover_tool_2 = HoverTool(renderers=[ia2, ib2], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRANET')], formatters={'@x': 'datetime'})
# # p.add_tools(hover_tool_2)


# hover_tool_3 = HoverTool(renderers=[ia3, ib3], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRATECH')], formatters={'@x': 'datetime'})
# # p.add_tools(hover_tool_3)

# hover_tool_4 = HoverTool(renderers=[ia4, ib4], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@ABBANK')], formatters={'@x': 'datetime'})



# p.add_tools(hover_tool_1, hover_tool_2, hover_tool_3, hover_tool_4)





# # p, i2 = draw_shape(x_col_name='x', y_col_name='y1', source=source, figure=p, shape='c', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# # p, i3 = draw_shape(x_col_name='x', y_col_name='y1', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=8, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='10 10', )

# # legend_item = LegendItem(label="Circle Line", renderers=[i2, i3])

# p, i4 = draw_shape(x_col_name='x', y_col_name='y2', source=source, figure=p, shape='t', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# p, i5 = draw_shape(x_col_name='x', y_col_name='y2', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# legend_item = LegendItem(label="Circle Line", renderers=[i4, i5])








######################################
#
#
# Working from here again
#
#

legend = Legend(items=[l1, l2, l3, l4], 
                location="top_left", 
                orientation="vertical",
               click_policy="hide"
               )

# Add the legend to the figure
p.add_layout(legend, 'left')

# Increase the size of the legend symbols
legend.label_text_font_size = "14pt"
legend.label_width = 50  # Adjust the width of the legend labels
legend.glyph_width = 50  # Adjust the width of the legend symbols
legend.spacing = 10  # Adjust the spacing between legend items
legend.propagate_hover = True


def update_data():
                # AAMRANET= get_co_data(co_name='AAMRANET')['percentage_change']
                # time.sleep(random.randint(5, 10))
                # AAMRATECH= get_co_data(co_name='AAMRATECH')['percentage_change']
                # time.sleep(random.randint(5, 10))
                # ABBANK= get_co_data(co_name='ABBANK')['percentage_change']
                # time.sleep(random.randint(5, 10))
    
                new_data = dict(
                x=[datetime.now()],
                # x = source.data['x'][-1] + timedelta(seconds=4),
                y1=[10],
                y2=[20],
                AAMRANET= [50],
                AAMRATECH= [40],
                ABBANK= [30],  
                # AAMRANET= [AAMRANET],
                # AAMRATECH= [AAMRATECH],
                # ABBANK= [ABBANK],     
                                )
                source.stream(new_data, 
                              # 100
                              1000
                             )

# Configure the document
curdoc().add_root(column(p))

update_data()

# Add the periodic callback to update the data
curdoc().add_periodic_callback(update_data, 3000)  # 180000   # 3000


# Perfection

