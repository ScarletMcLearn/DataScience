from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Toggle
from bokeh.plotting import figure
from bokeh.layouts import row
from random import randint
from functools import partial
import pandas as pd
import os

# Variables for saving/loading data
save_to_disk = False
load_from_disk = False

# Chunk size for loading data from CSV
CHUNK_SIZE = 1000

# Create a data source for the lines
data_dict = {'x': []}
line_count = 400
for i in range(1, line_count+1):
    data_dict[f'y{i}'] = []

source = ColumnDataSource(data=data_dict)

# Create a figure
p = figure(width=800, height=400, title='Updating Lines')

# Create line renderers
renderers = []
line_colors = ['blue', 'red', 'green', 'orange']
for i in range(1, line_count+1):
    renderer = p.line(x='x', y=f'y{i}', line_width=2, color=line_colors[i % len(line_colors)], legend_label=f'Line {i}', source=source)
    renderers.append(renderer)

# Function to load data from CSV in chunks
def load_data_from_csv():
    data = {'x': []}
    for i in range(1, line_count+1):
        data[f'y{i}'] = []

    if load_from_disk and os.path.exists('data.csv'):
        for chunk in pd.read_csv('data.csv', chunksize=CHUNK_SIZE):
            data['x'].extend(chunk['x'].tolist())
            for i in range(1, line_count+1):
                data[f'y{i}'].extend(chunk[f'y{i}'].tolist())
        start_x = max(data['x']) if data['x'] else 0
    else:
        # Create a new CSV file
        if save_to_disk:
            pd.DataFrame(data).to_csv('data.csv', index=False)
        start_x = 0

    return data, start_x

# Update the lines with random data
def update_lines():
    new_data = {'x': source.data['x'] + [source.data['x'][-1] + 1] if source.data['x'] else [start_x + 1]}
    for i in range(1, line_count+1):
        new_data[f'y{i}'] = source.data[f'y{i}'] + [randint(0, 10)]
    source.data = new_data

    # Update the x-range of the plot to show the latest points
    if len(source.data['x']) >= 10:
        p.x_range.start = source.data['x'][-10]
    p.x_range.end = source.data['x'][-1]

    # Update the y-range of the plot
    y_min = min([min(source.data[f'y{i}']) for i in range(1, line_count+1)]) - 1
    y_max = max([max(source.data[f'y{i}']) for i in range(1, line_count+1)]) + 1
    p.y_range.start = y_min
    p.y_range.end = y_max

    # Save the updated data to the CSV file
    if save_to_disk:
        pd.DataFrame(source.data).to_csv('data.csv', index=False)

# Create a callback to update the lines every 2 seconds
callback = partial(update_lines)

# Load the initial data from CSV
source.data, start_x = load_data_from_csv()

# Add the lines to the document
curdoc().add_root(row(p))

# Create a toggle button
toggle_button = Toggle(label="Toggle Update", button_type="success")

# Define the toggle button callback
def toggle_callback(active):
    if active:
        curdoc().add_periodic_callback(callback, 2000)
    else:
        curdoc().remove_periodic_callback(callback)

toggle_button.on_click(toggle_callback)

# Add the toggle button to the document
curdoc().add_root(row(toggle_button))
