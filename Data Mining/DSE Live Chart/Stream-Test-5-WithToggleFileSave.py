from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
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
source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# Create a figure
p = figure(width=800, height=400, title='Updating Lines')

# Create four line renderers
renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)


# Function to load data from CSV in chunks
def load_data_from_csv():
    data = {
        'x': [],
        'y1': [],
        'y2': [],
        'y3': [],
        'y4': []
    }

    if load_from_disk and os.path.exists('data.csv'):
        for chunk in pd.read_csv('data.csv', chunksize=CHUNK_SIZE):
            data['x'].extend(chunk['x'].tolist())
            data['y1'].extend(chunk['y1'].tolist())
            data['y2'].extend(chunk['y2'].tolist())
            data['y3'].extend(chunk['y3'].tolist())
            data['y4'].extend(chunk['y4'].tolist())
        start_x = max(data['x']) if data['x'] else 0
    else:
        # Create a new CSV file
        if save_to_disk:
            pd.DataFrame(data).to_csv('data.csv', index=False)
        start_x = 0

    return data, start_x

# Update the lines with random data
def update_lines():
    new_data = dict(
        x=source.data['x'] + [source.data['x'][-1] + 1] if source.data['x'] else [start_x + 1],
        y1=source.data['y1'] + [randint(0, 10)],
        y2=source.data['y2'] + [randint(0, 10)],
        y3=source.data['y3'] + [randint(0, 10)],
        y4=source.data['y4'] + [randint(0, 10)]
    )
    source.data = new_data

    # Update the x-range of the plot to show the latest points
    if len(source.data['x']) >= 10:
        p.x_range.start = source.data['x'][-10]
    p.x_range.end = source.data['x'][-1]

    # Update the y-range of the plot
    p.y_range.start = min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1
    p.y_range.end = max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1

    # Save the updated data to the CSV file
    if save_to_disk:
        pd.DataFrame(source.data).to_csv('data.csv', index=False)

# Create a callback to update the lines every 2 seconds
callback = partial(update_lines)

# Load the initial data from CSV
source.data, start_x = load_data_from_csv()

# Add the lines to the document
curdoc().add_root(row(p))

# Periodically update the lines every 2 seconds
curdoc().add_periodic_callback(callback, 2000)