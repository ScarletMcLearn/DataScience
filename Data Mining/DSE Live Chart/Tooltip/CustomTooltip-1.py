from bokeh.plotting import figure, show
from bokeh.models import HoverTool

# Create some example data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 7, 6]
labels = ['A', 'B', 'C', 'D', 'E']

# Create a figure
p = figure(width=1000, height=1000)

# Plot the data points
scatter = p.scatter(x, y, size=10)

# Define the tooltip
tooltips = [
    ("Label", "@labels"),  # Use the '@' syntax to refer to a column in the data source
    ("X", "@x"),
    ("Y", "@y"),
]

# Add the HoverTool with the defined tooltips to the figure
hover_tool = HoverTool(tooltips=tooltips, renderers=[scatter])
p.add_tools(hover_tool)

# Show the figure
show(p)