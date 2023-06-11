from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models import DataRange1d
from random import randint
from datetime import datetime, timedelta

# Create a ColumnDataSource to stream data
source = ColumnDataSource(data=dict(time=[], y=[]))

# Set up the figure
plot = figure(x_axis_type='datetime', y_range=(0, 100), width=800, height=400)
line = plot.line('time', 'y', source=source, line_width=2)

# Function to generate new data and update the graph
def update_data():
    new_data = generate_new_data()
    source.stream(new_data, 10)  # Keep the latest 10 points
    # Update the x-axis range to show the latest 10 points
    plot.x_range.start = max(source.data['time']) - timedelta(seconds=10)
    plot.x_range.end = max(source.data['time'])

# Function to generate new data
def generate_new_data():
    return dict(
        time=[datetime.now()],
        y=[randint(0, 100)]
    )

# Add the figure to the current document
curdoc().add_root(plot)

# Update the graph every 1 second
curdoc().add_periodic_callback(update_data, 1000)

# Generate initial data
initial_data = generate_new_data()
source.data = initial_data
# Set up the x-axis range to show the latest 10 points
plot.x_range = DataRange1d(start=max(initial_data['time']) - timedelta(seconds=10), end=max(initial_data['time']))
