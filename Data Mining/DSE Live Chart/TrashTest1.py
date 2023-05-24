from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, LegendItem
from bokeh.plotting import figure
from bokeh.layouts import row


# Variables for saving/loading data
save_to_disk = False
load_from_disk = False


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


def create_legend_item(label, glyph_renderers):
    return LegendItem(label=label, renderers=glyph_renderers)


# Chunk size for loading data from CSV
CHUNK_SIZE = 1000

# Create a data source for the lines
data_dict = {'x': []}
line_count = 400
for i in range(1, line_count+1):
    data_dict[f'y{i}'] = []

source = ColumnDataSource(data=data_dict)

# Create a toggle button
x_range_toggle = Toggle(label='Update X-Range', active=True)

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

    # Update the x-range of the plot if enabled
    if x_range_toggle.active:
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

# Callback function for the toggle button
def toggle_callback(attr, old, new):
    if new == True:
        # Enable updating the x-range
        if len(source.data['x']) >= 10:
            p.x_range.start = source.data['x'][-10]
        p.x_range.end = source.data['x'][-1]
    else:
        # Disable updating the x-range
        p.x_range.start = p.x_range.start
        p.x_range.end = p.x_range.end

# Add callback to the toggle button
x_range_toggle.on_click(toggle_callback)

# Create a callback to update the lines every 2 seconds
callback = partial(update_lines)

# Load the initial data from CSV
source.data, start_x = load_data_from_csv()

# Add the lines and toggle button to the document
curdoc().add_root(row(p))
curdoc().add_root(x_range_toggle)

# Periodically update the lines every 2 seconds
curdoc().add_periodic_callback(callback, 2000)
