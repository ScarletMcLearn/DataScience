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
mapper = linear_cmap(field_name="y_1_values", palette=Turbo256, 
                     low=100, high=0)

p = figure(
    title="Dhaka Stock Exchange Live Change",
    x_axis_type="datetime",
    sizing_mode="scale_both",
    max_width=900,
    max_height=300,
    width=900,
    height=900
)

p.title.align = "center"
# Set x-axis and y-axis labels
p.xaxis.axis_label = "Date-Time"
p.yaxis.axis_label = "Percentage Change (%)"

p.xaxis.formatter = DatetimeTickFormatter(hours="%H:%M")

curdoc().theme = 'dark_minimal'

global source
no_of_obj = 6
x_values = []
no_already_avail = len(x_values)
x_values += generate_datetime_objects(no_of_obj, no_already_avail)

y_1_values = generate_random_floats(len(x_values))
y_2_values = generate_random_floats(len(x_values))
y_3_values = generate_random_floats(len(x_values))
y_4_values = generate_random_floats(len(x_values))

# print(len(x_values))
# print(len(y_1_values))
# print(len(y_2_values))
source = ColumnDataSource(data=dict(x_values=x_values, y_1_values=y_1_values, y_2_values=y_2_values, y_3_values=y_3_values, y_4_values=y_4_values))


p, i2 = draw_shape(x_col_name='x_values', y_col_name='y_1_values', source=source, figure=p, shape='c', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

p, i3 = draw_shape(x_col_name='x_values', y_col_name='y_1_values', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

p, i4 = draw_shape(x_col_name='x_values', y_col_name='y_2_values', source=source, figure=p, shape='c', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

p, i5 = draw_shape(x_col_name='x_values', y_col_name='y_2_values', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )


p, i6 = draw_shape(x_col_name='x_values', y_col_name='y_3_values', source=source, figure=p, shape='c', size=30, fill_color='pink', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

p, i7 = draw_shape(x_col_name='x_values', y_col_name='y_3_values', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

i2_i3 = LegendItem(label="Circle Line 1", renderers=[i2, i3])
i4_i5 = LegendItem(label="Circle Line 2", renderers=[i4, i5])
i6_i7 = LegendItem(label="Circle Line 3", renderers=[i6, i7])

legend_item = []
legend_item.append(i2_i3)
legend_item.append(i4_i5)
legend_item.append(i6_i7)


legend = Legend(items=legend_item, location="top_left", orientation="vertical")

# Add the legend to the figure
p.add_layout(legend)

# Show the plot
show(p)

from bokeh.io import curdoc

# Define a callback function for updating the plot
# def update():
    # # Generate new random data for each column in the ColumnDataSource
    # new_x_value = generate_datetime_objects(1, len(source.data['x_values']))[0]
    # new_y_1_value = generate_random_floats(1)[0]
    # new_y_2_value = generate_random_floats(1)[0]
    # new_y_3_value = generate_random_floats(1)[0]
    # new_y_4_value = generate_random_floats(1)[0]
    
    # # Append the new data to the existing data in the ColumnDataSource
    # source.data['x_values'].append(new_x_value)
    # source.data['y_1_values'].append(new_y_1_value)
    # source.data['y_2_values'].append(new_y_2_value)
    # source.data['y_3_values'].append(new_y_3_value)
    # source.data['y_4_values'].append(new_y_4_value)
    
    # # Trigger the update of the plot
    # curdoc().add_next_tick_callback(lambda: source.change.emit())

# # Create a ColumnDataSource to store the data
# source = ColumnDataSource(data=dict(x_values=[], y_1_values=[], y_2_values=[], y_3_values=[], y_4_values=[]))

# def update():
#     # Generate new random data
#     new_x = generate_datetime_objects(1, len(source.data['x_values']))
#     new_y_1 = generate_random_floats(1)
#     new_y_2 = generate_random_floats(1)
#     new_y_3 = generate_random_floats(1)
#     new_y_4 = generate_random_floats(1)
    
#     # Append the new data to the existing column data
#     source.data['x_values'].extend(new_x)
#     source.data['y_1_values'].extend(new_y_1)
#     source.data['y_2_values'].extend(new_y_2)
#     source.data['y_3_values'].extend(new_y_3)
#     source.data['y_4_values'].extend(new_y_4)
    
#     # Trigger the update by explicitly notifying the ColumnDataSource of the change
#     source.data = source.data.copy()

# # Update the plot every 5 seconds using the update() function
# callback = CustomJS(code="setInterval(function(){IPython.notebook.kernel.execute('update()')}, 5000);")
# show(p)
    

# # Schedule the callback function to run every 5 seconds
# # curdoc().add_periodic_callback(update, 5000)

import time
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource

# Create a figure and add line glyphs
p = figure(title="Live Chart", x_axis_type="datetime")
p.line(x='x_values', y='y_1_values', line_color="red", line_width=2, source=source)
p.line(x='x_values', y='y_2_values', line_color="green", line_width=2, source=source)
p.line(x='x_values', y='y_3_values', line_color="blue", line_width=2, source=source)
p.line(x='x_values', y='y_4_values', line_color="orange", line_width=2, source=source)

# Create a ColumnDataSource to store the data
source = ColumnDataSource(data=dict(x_values=[], y_1_values=[], y_2_values=[], y_3_values=[], y_4_values=[]))

def update():
    # Generate new random data
    new_x = generate_datetime_objects(1, len(source.data['x_values']))
    new_y_1 = generate_random_floats(1)
    new_y_2 = generate_random_floats(1)
    new_y_3 = generate_random_floats(1)
    new_y_4 = generate_random_floats(1)
    
    # Append the new data to the existing column data
    source.data['x_values'].extend(new_x)
    source.data['y_1_values'].extend(new_y_1)
    source.data['y_2_values'].extend(new_y_2)
    source.data['y_3_values'].extend(new_y_3)
    source.data['y_4_values'].extend(new_y_4)
    
    # Trigger the update by explicitly notifying the ColumnDataSource of the change
    source.data = source.data.copy()

# Update the plot every 5 seconds
callback_id = None

def start_update():
    global callback_id
    if callback_id is None:
        callback_id = curdoc().add_periodic_callback(update, 5000)

def stop_update():
    global callback_id
    if callback_id:
        curdoc().remove_periodic_callback(callback_id)
        callback_id = None

# Start the periodic updates
start_update()

# Show the plot
show(p)

# Keep the script running to continue receiving updates
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        # Stop the updates if interrupted
        stop_update()
        break
