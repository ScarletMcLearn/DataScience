from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.layouts import row
from random import randint
from functools import partial
from datetime import datetime, timedelta

# Create a data source for the lines
source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# Create a figure
p = figure(width=2150, height=950,  title='Updating Lines')

# Create four line renderers
renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # Add hover tools for each line renderer
# hover_tool1 = HoverTool(renderers=[renderer1], tooltips=[('X', '@x'), ('Y', '@y1')])
# hover_tool2 = HoverTool(renderers=[renderer2], tooltips=[('X', '@x'), ('Y', '@y2')])
# hover_tool3 = HoverTool(renderers=[renderer3], tooltips=[('X', '@x'), ('Y', '@y3')])
# hover_tool4 = HoverTool(renderers=[renderer4], tooltips=[('X', '@x'), ('Y', '@y4')])

# Add hover tools for each line renderer
hover_tool1 = HoverTool(renderers=[renderer1], tooltips=[('X', '@x'), ('Y', f'{datetime.now():%H:%M:%S}')], formatters={'@x': 'datetime'})
hover_tool2 = HoverTool(renderers=[renderer2], tooltips=[('X', '@x'), ('Y', f'{datetime.now():%H:%M:%S}')], formatters={'@x': 'datetime'})
hover_tool3 = HoverTool(renderers=[renderer3], tooltips=[('X', '@x'), ('Y', f'{datetime.now():%H:%M:%S}')], formatters={'@x': 'datetime'})
hover_tool4 = HoverTool(renderers=[renderer4], tooltips=[('X', '@x'), ('Y', f'{datetime.now():%H:%M:%S}')], formatters={'@x': 'datetime'})


# Add the hover tools to the plot
p.add_tools(hover_tool1, hover_tool2, hover_tool3, hover_tool4)

# Update the lines with random data
def update_lines():
    new_data = dict(
        x=source.data['x'] + [source.data['x'][-1] + 1] if source.data['x'] else [0],
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

# Create a callback to update the lines every 2 seconds
callback = partial(update_lines)

# Add the lines to the document
curdoc().add_root(row(p))

# Initial update
update_lines()

# Periodically update the lines every 2 seconds
callback_id = curdoc().add_periodic_callback(callback, 2000)

# Stop the stream after 1 minute
stop_time = datetime.now() + timedelta(minutes=1)

def check_stop_time():
    if datetime.now() >= stop_time:
        curdoc().remove_periodic_callback(callback_id)

# Add a periodic callback to check the stop time
curdoc().add_periodic_callback(check_stop_time, 1000)  # Check every second
