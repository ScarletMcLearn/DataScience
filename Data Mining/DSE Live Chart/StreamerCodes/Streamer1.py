from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource
from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import row

import random
from datetime import datetime, timedelta

# Create the ColumnDataSource
source = ColumnDataSource(data=dict(time=[], value=[]))

# Create the figure
p = figure(title="Streaming Graph", width=800, height=400,
           x_axis_type="datetime", y_range=(0, 100))

# Configure axis format
p.xaxis.formatter = DatetimeTickFormatter(seconds=["%M:%S"])

# Add a line to the figure
p.line(x='time', y='value', source=source, line_width=2)

# Define the update function
def update():
    new_data = dict(
        time=[datetime.now()],
        value=[random.randint(0, 100)]
    )
    source.stream(new_data, 10)  # Only keep the latest 10 points

# Add the figure to the current document
curdoc().add_root(row(p))

# Update the graph every 1 second
curdoc().add_periodic_callback(update, 1000)
