# ################ 1
# from datetime import datetime
# from random import randint
# from bokeh.layouts import column
# from bokeh.models import ColumnDataSource, DataRange1d
# from bokeh.plotting import curdoc, figure
# from bokeh.models.tools import WheelZoomTool

# # Create the figure
# p = figure(width=800, height=400, tools='xpan', active_drag='xpan')

# # Create the data source
# source = ColumnDataSource(data=dict(time=[], value=[]))

# # Set the range for the x-axis to show the last 10 seconds
# x_range = DataRange1d(follow='end', follow_interval=1000, range_padding=0)
# p.x_range = x_range

# # Configure the y-axis
# p.y_range = DataRange1d(start=0, end=100)

# # Add a line to the graph
# line = p.line(x='time', y='value', source=source)

# # Add the WheelZoomTool to enable zooming with the mouse wheel
# p.add_tools(WheelZoomTool())

# # Function to update the graph data
# def update():
#     new_data = dict(
#         time=[datetime.now()],
#         value=[randint(0, 100)]
#     )
#     source.stream(new_data, rollover=100)

# # Update the graph every 1 second
# curdoc().add_periodic_callback(update, 1000)

# # Show the graph
# curdoc().add_root(column(p))

# #############################

# ######### 2
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import WheelZoomTool
from datetime import datetime
from random import randint
from functools import partial

# Create a figure
p = figure(x_axis_type='datetime', y_range=(0, 100), width=800, height=400, tools='pan,reset')

# Create a ColumnDataSource to hold the data
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create a line glyph
line = p.line(x='x', y='y', source=source)

# Set up the streaming callback
def update():
    new_data = dict(
        x=[datetime.now()],
        y=[randint(0, 100)]
    )
    source.stream(new_data, 100)

# Add the WheelZoomTool to enable zooming
p.add_tools(WheelZoomTool())

# Configure the document
curdoc().add_root(column(p))

# Add the periodic callback to update the data
curdoc().add_periodic_callback(update, 1000)