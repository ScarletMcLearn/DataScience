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

# # Create a data source for the lines
# source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))



##############
# Updating from here for 400 lines

no_of_companies = 400
# Create data source for all lines
source_data = {'x': []}
for i in range(1, no_of_companies+1):
    source_data[f'y{i}'] = []

source = ColumnDataSource(data=source_data)

# Initialize lines
lines = []
for i in range(1, no_of_companies+1):
    line = plot.line(x='x', y=f'y{i}', source=source)
    lines.append(line)