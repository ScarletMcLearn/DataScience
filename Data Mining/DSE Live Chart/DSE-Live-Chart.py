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


#find_header
for i in soup.findAll('th', attrs={"width": "12%"}):
    print(i.text)
    
for i in range(len(soup.findAll('th', attrs={"width": "12%"}))):
     print(str(i), ' : ', soup.findAll('th', attrs={"width": "12%"})[i])
 
#0  :  <th width="12%">TRADING CODE</th>
#1  :  <th width="12%">LTP*</th>
#2  :  <th width="12%">HIGH</th>
#3  :  <th width="12%">LOW</th>
#4  :  <th width="12%">CLOSEP*</th>
#5  :  <th width="12%">YCP*</th>
#6  :  <th width="12%">CHANGE</th>
#7  :  <th width="12%">TRADE</th>
#8  :  <th width="12%">VALUE (mn)</th>
#9  :  <th width="12%">VOLUME</th>


#0  :  393
#1  :  ZEALBANGLA							
#2  :  122.1
#3  :  125
#4  :  121.5
#5  :  122.1
#6  :  122.1
#7  :  0
#8  :  42
#9  :  0.45
#10  :  3,676


    
soup.findAll('tr')

soup.findAll('tr')[394].findAll('td')

for i in range(len(soup.findAll('tr')[394].findAll('td'))):
     print(str(i), ' : ', soup.findAll('tr')[394].findAll('td')[i].text)


for j in range(len(soup.findAll('tr'))):
    for i in range(len(soup.findAll('tr')[j].findAll('td'))):
         if i%1==0:
            trading_code = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%2==0:
         last_trading_price = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%3==0:
         last_high = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%4==0:
         last_low = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%5==0:
         close_price = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%6==0:
         yesterday_close_price = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%7==0:
         percentage_change = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%8==0:
         number_of_trades = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%9==0:
         value_of_trades = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%10==0:
         volume = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         time.sleep(60)
     



I am getting live structured data of 393 rows, each row containing the following columns:
'TRADING CODE',	'LTP*',	'HIGH',	'LOW',	'CLOSEP*',	'YCP*',	'CHANGE',	'TRADE	VALUE (mn)',	'VOLUME'.

I am getting the data by live scraping a site using BeautifulSoup and Requests. 

I can print out the live data using the following code:

for i in range(len(soup.findAll('tr')[394].findAll('td'))):
     print(str(i), ' : ', soup.findAll('tr')[394].findAll('td')[i].text)

# Note :
# len(soup.findAll('tr')) == 393 (this signifies the number of rows / data points)
for j in range(len(soup.findAll('tr'))):
    for i in range(len(soup.findAll('tr')[j].findAll('td'))):
         if i%1==0:
            trading_code = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%2==0:
         last_trading_price = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%3==0:
         last_high = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%4==0:
         last_low = soup.findAll('tr')[j].findAll('td')[i].text
         elif i%5==0:
         close_price = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%6==0:
         yesterday_close_price = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%7==0:
         percentage_change = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%8==0:
         number_of_trades = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%9==0:
         value_of_trades = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         elif i%10==0:
         volume = soup.findAll('tr')[j].findAll('td')[i].text
         print(str(i), ' : ', soup.findAll('tr')[j].findAll('td')[i].text)
         time.sleep(60)

I want to make an interactive Python live time series streaming plot. 
I want to display the percentage_change of each of the 393 data points on a large plot chat. 
I need the data points on the chart to animate to the left and add new points after a particular time duration specified - for example, I want it to sleep for 60 seconds before getting the latest data for the 393 points and animating the previous 393 points to the left and creating the new ones after them.
The plot should be interactive, have tool tips, legends, zooming functionality, drag to scroll functionality, left and right moving functionality. 
The plot should also look visually appealing.

I want you to suggest me the best Python library which I can use to make this plot which will make it easy and efficient to display this with least code. It also has to be customizable and look beautiful. 


#########

Create an interactive Python live time series streaming plot using the Plotly library. The plot should display the percentage_change of each of the 393 data points in a visually appealing manner. The plot should animate the previous 393 points to the left and add new points after a specified time duration (e.g., 60 seconds). The plot should include tooltips, legends, zooming functionality, drag-to-scroll functionality, and left and right moving functionality. Ensure that the plot is visually customizable and aesthetically pleasing. The percentage_change value will fluctuate between 0 and 100%. The x-axis will be time based and each unit on the x-axis will be the time period set before getting new data. Consider using a color scheme or marker style to highlight positive and negative percentage changes. Add tooltips to display additional information about each data point, such as the trading code and other relevant details. Include legends to provide context for the plotted data. Implement zooming functionality to allow users to focus on specific periods of interest. Add drag-to-scroll functionality for easy navigation through the time series.
Consider using animation to smoothly transition and update the plot when new data points are added.


#####

Create an interactive Python live time series streaming plot using the Plotly library. The plot should display the percentage_change over time using a line plot, where positive changes are shown in one color and negative changes in another color. Customize the color scheme or marker style to ensure clear differentiation between positive and negative changes. Incorporate a time-based x-axis to accurately represent the time series data. Add tooltips that display the relevant details for each data point, including the trading code, last_trading_price, last_high, last_low, close_price, yesterday_close_price, percentage_change, number_of_trades, value_of_trades, and volume. Implement a scrollable legend that shows the colors associated with the 393 data points per time point, mapped by trading_code values. Provide zooming functionality to allow users to focus on specific periods of interest. Enable drag-to-scroll functionality for easy navigation through the time series. Utilize animation to create smooth transitions and updates when new data points are added.

########

import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.callbacks import Points, InputDeviceState

# Create an empty figure with subplots
fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)

# Create empty arrays to store the data
x_data = []
y_data = []
colors = []

# Create the initial plot with empty data
line_plot = go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color='gray'), name='Percentage Change')
fig.append_trace(line_plot, row=1, col=1)

scatter_plot = go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color='gray'), name='Trading Code')
fig.append_trace(scatter_plot, row=2, col=1)

# Create the layout
fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',
        range=[0, 10],  # Initial x-axis range
        showgrid=True,
    ),
    yaxis=dict(
        title='Percentage Change',
        showgrid=True,
    ),
    xaxis2=dict(
        title='Time',
        showgrid=True,
    ),
    yaxis2=dict(
        title='Trading Code',
        showgrid=True,
        range=[0, 393],  # Fixed y-axis range for trading code
        dtick=50,  # Tick interval
    ),
    hovermode='x unified',  # Show hover information for both subplots
)

# Create a custom color scale for positive and negative changes
color_scale = [[0, 'red'], [1, 'green']]  # Change the colors as desired

# Create a Points callback to update the plot with new data
def update_plot(trace, points, selector):
    global x_data, y_data, colors

    # Get the new data from the real-time source
    new_x = points.xs[0]['x']
    new_y = points.xs[0]['y']
    new_color = 'red' if new_y < 0 else 'green'

    # Append the new data to the arrays
    x_data.append(new_x)
    y_data.append(new_y)
    colors.append(new_color)

    # Update the line plot trace
    fig.data[0].x = x_data
    fig.data[0].y = y_data
    fig.data[0].line.color = colors

    # Update the scatter plot trace
    fig.data[1].x = x_data
    fig.data[1].y = [393] * len(x_data)  # Fixed y-axis value for trading code
    fig.data[1].marker.color = colors

# Create a Points object with the callback function
callback_points = Points(fig.data[0])
callback_points.on_add(update_plot)

# Create InputDeviceState to enable drag-to-scroll functionality
ids = [callback_points.id]
input_state = InputDeviceState(ids)

# Create the animation frames for smooth transitions and updates
animation_frames = [dict(data=fig.data)]

fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',
        range=[0, 10],  # Initial x-axis range
        showgrid=True,
    ),
    yaxis=dict(
        title='Percentage Change',
        showgrid=True,
    ),
    xaxis2=dict(
        title='Time',
        showgrid=True,
    ),
    yaxis2=dict(
        title='Trading Code',
        showgrid=True,
        range=[0, 393],  # Fixed y-axis range for trading code
        dtick=50,  # Tick interval
    ),
    hovermode='x unified',  # Show hover information for both subplots
    updatemenus=[
        dict(
            type='buttons',
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[None, {'frame': {'duration': 100, 'redraw': False}, 'fromcurrent': True, 'transition': {'duration': 0}}],
                ),
                dict(
                    label='Pause',
                    method='animate',
                    args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}],
                ),
                dict(
                    label='Reset',
                    method='animate',
                    args=[None, {'frame': {'duration': 0, 'redraw': True}, 'transition': {'duration': 0}}],
                ),
            ],
            direction='left',
            pad={'r': 10, 't': 10},
            showactive=False,
            x=0,
            xanchor='right',
            y=1.15,
            yanchor='top'
        ),
    ],
    sliders=[
        dict(
            active=0,
            currentvalue={'prefix': 'Zoom Level: '},
            pad={'t': 50},
            steps=[],
        ),
    ],
)

# Update the steps for the slider based on the number of data points
num_data_points = 100  # Replace with the actual number of data points
for i in range(num_data_points):
    frame = dict(
        args=[[i], {'frame': {'duration': 300, 'redraw': False}, 'mode': 'immediate'}],
        label=str(i),
        method='animate',
    )
    fig.layout.sliders[0].steps.append(frame)


# Create tooltips using custom hovertemplate for the line plot
fig.data[0].hovertemplate = (
    '<b>Trading Code:</b> %{customdata[0]}<br>' +
    '<b>Last Trading Price:</b> %{customdata[1]:.2f}<br>' +
    '<b>Last High:</b> %{customdata[2]:.2f}<br>' +
    '<b>Last Low:</b> %{customdata[3]:.2f}<br>' +
    '<b>Close Price:</b> %{customdata[4]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{customdata[5]:.2f}<br>' +
    '<b>Percentage Change:</b> %{customdata[6]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{customdata[7]}<br>' +
    '<b>Value of Trades:</b> %{customdata[8]:.2f}<br>' +
    '<b>Volume:</b> %{customdata[9]}'
)

# Create tooltips using custom hovertemplate for the scatter plot
fig.data[1].hovertemplate = (
    '<b>Trading Code:</b> %{customdata}<br>' +
    '<b>Last Trading Price:</b> %{x:.2f}<br>' +
    '<b>Last High:</b> %{y[0]:.2f}<br>' +
    '<b>Last Low:</b> %{y[1]:.2f}<br>' +
    '<b>Close Price:</b> %{y[2]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{y[3]:.2f}<br>' +
    '<b>Percentage Change:</b> %{y[4]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{y[5]}<br>' +
    '<b>Value of Trades:</b> %{y[6]:.2f}<br>' +
    '<b>Volume:</b> %{y[7]}'
)

# Enable drag-to-scroll functionality
fig.show(config={'scrollZoom': True})

# Enable streaming updates
stream = go.Stream(
    token='your_stream_token',  # Replace with your stream token
    maxpoints=393,  # Number of points per update
)

# Open the stream
stream.open()

# Continuously update the plot with new data
while True:
    # Get new data from the real-time source
    trading_code = ...
    last_trading_price = ...
    last_high = ...
    last_low = ...
    close_price = ...
    yesterday_close_price = ...
    percentage_change = ...
    number_of_trades = ...
    value_of_trades = ...
    volume = ...

    # Append the new data to the arrays
    x_data.append(new_x)
    y_data.append(new_y)
    colors.append(new_color)

    # Send the new data to the plotly stream
    stream.write(dict(
        x=new_x,
        y=new_y,
        customdata=[
            trading_code,
            last_trading_price,
            last_high,
            last_low,
            close_price,
            yesterday_close_price,
            percentage_change,
            number_of_trades,
            value_of_trades,
            volume,
        ]
    ))


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# Create empty arrays to store the data
x_data = []
y_data = []
colors = []

# Create the initial plot with empty data
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
line_plot = go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color='gray'), name='Percentage Change')
scatter_plot = go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color='gray'), name='Trading Code')

# Create a custom color scale for positive and negative changes
color_scale = [[0, 'red'], [1, 'green']]  # Change the colors as desired

# Add the line plot and scatter plot to the figure
fig.add_trace(line_plot, row=1, col=1)
fig.add_trace(scatter_plot, row=2, col=1)

# Update the layout
fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',
        showgrid=True,
        range=[datetime.datetime.now() - datetime.timedelta(hours=1), datetime.datetime.now()]  # Initial x-axis range
    ),
    yaxis=dict(
        title='Percentage Change',
        showgrid=True
    ),
    xaxis2=dict(
        title='Time',
        showgrid=True
    ),
    yaxis2=dict(
        title='Trading Code',
        showgrid=True,
        range=[0, 393]  # Fixed y-axis range for trading code
    ),
    hovermode='x unified',  # Show hover information for both subplots
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    plot_bgcolor='white'
)

# Create tooltips using custom hovertemplate for the line plot
line_plot.hovertemplate = (
    '<b>Trading Code:</b> %{customdata[0]}<br>' +
    '<b>Last Trading Price:</b> %{customdata[1]:.2f}<br>' +
    '<b>Last High:</b> %{customdata[2]:.2f}<br>' +
    '<b>Last Low:</b> %{customdata[3]:.2f}<br>' +
    '<b>Close Price:</b> %{customdata[4]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{customdata[5]:.2f}<br>' +
    '<b>Percentage Change:</b> %{customdata[6]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{customdata[7]}<br>' +
    '<b>Value of Trades:</b> %{customdata[8]:.2f}<br>' +
    '<b>Volume:</b> %{customdata[9]}'
)

# Create tooltips using custom hovertemplate for the scatter plot
scatter_plot.hovertemplate = (
    '<b>Trading Code:</b> %{customdata}<br>' +
    '<b>Last Trading Price:</b> %{x:.2f}<br>' +
    '<b>Last High:</b> %{y[0]:.2f}<br>' +
    '<b>Last Low:</b> %{y[1]:.2f}<br>' +
    '<b>Close Price:</b> %{y[2]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{y[3]:.2f}<br>' +
    '<b>Percentage Change:</b> %{y[4]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{y[5]}<br>' +
    '<b>Value of Trades:</b> %{y[6]:.2f}<br>' +
    '<b>Volume:</b> %{y[7]}'
)

# Enable drag-to-scroll functionality
fig.update_xaxes(dragmode='pan')

# Enable zooming functionality
fig.update_xaxes(rangeselector=dict(
    buttons=list([
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(count=1, label='1d', step='day', stepmode='backward'),
        dict(count=7, label='1w', step='day', stepmode='backward'),
        dict(count=1, label='1m', step='month', stepmode='backward'),
        dict(count=3, label='3m', step='month', stepmode='backward'),
        dict(count=6, label='6m', step='month', stepmode='backward'),
        dict(count=1, label='1y', step='year', stepmode='backward'),
        dict(step='all')
    ])
))

# Enable animation
fig.update_layout(transition=dict(duration=1000))

# Show the figure
fig.show()



