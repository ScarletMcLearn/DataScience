from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import row
from random import randint
from functools import partial

# Create a data source for the lines
source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# Create a figure
p = figure(width=800, height=400, title='Updating Lines')

# Create four line renderers
renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)


MAX_DATA_POINTS = 100  # Maximum number of data points to store

def update_lines():
    new_data = dict(
        x=source.data['x'][-(MAX_DATA_POINTS-1):] + [source.data['x'][-1] + 1] if source.data['x'] else [0],
        y1=source.data['y1'][-(MAX_DATA_POINTS-1):] + [randint(0, 10)],
        y2=source.data['y2'][-(MAX_DATA_POINTS-1):] + [randint(0, 10)],
        y3=source.data['y3'][-(MAX_DATA_POINTS-1):] + [randint(0, 10)],
        y4=source.data['y4'][-(MAX_DATA_POINTS-1):] + [randint(0, 10)]
    )
    source.data = new_data

    # Update the x-range of the plot to show the latest points
    if len(source.data['x']) >= 10:
        p.x_range.start = source.data['x'][-10]
    p.x_range.end = source.data['x'][-1]

    # Update the y-range of the plot
    p.y_range.start = min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1
    p.y_range.end = max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1


# Create a callback to update the lines every 2 seconds
callback = partial(update_lines)

# Add the lines to the document
curdoc().add_root(row(p))

# Initial update
update_lines()

# Periodically update the lines every 2 seconds
curdoc().add_periodic_callback(callback, 2000)


# Working Perfectly 2