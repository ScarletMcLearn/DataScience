# # # # # # # from bokeh.io import curdoc
# # # # # # # from bokeh.models import ColumnDataSource
# # # # # # # from bokeh.plotting import figure
# # # # # # # from bokeh.layouts import row
# # # # # # # from random import randint
# # # # # # # from functools import partial
# # # # # # # from bokeh.models import Button

# # # # # # # # Create a figure
# # # # # # # p = figure(width=800, height=400, title='Updating Lines')

# # # # # # # # Create four line renderers
# # # # # # # renderer1 = p.line('x', 'y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # # # # # # renderer2 = p.line('x', 'y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # # # # # # renderer3 = p.line('x', 'y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # # # # # # renderer4 = p.line('x', 'y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # # # # # # Create a data source for the lines
# # # # # # # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # # # # # # Update the lines with random data
# # # # # # # def update_lines():
# # # # # # #     new_data = dict(
# # # # # # #         x=[1, 2, 3, 4],  # x-values remain constant
# # # # # # #         y1=[randint(0, 10) for _ in range(4)],
# # # # # # #         y2=[randint(0, 10) for _ in range(4)],
# # # # # # #         y3=[randint(0, 10) for _ in range(4)],
# # # # # # #         y4=[randint(0, 10) for _ in range(4)]
# # # # # # #     )
# # # # # # #     source.data = new_data

# # # # # # # # Create a callback to update the lines every 5 seconds
# # # # # # # callback = partial(update_lines)

# # # # # # # # Create a button to start updating
# # # # # # # button = Button(label='Start Updating', button_type='success')
# # # # # # # button.on_click(callback)

# # # # # # # # Add the lines and button to the document
# # # # # # # curdoc().add_root(row(p, button))

# # # # # # # # Initial update
# # # # # # # update_lines()



# # # # # # from bokeh.io import curdoc
# # # # # # from bokeh.models import ColumnDataSource
# # # # # # from bokeh.plotting import figure
# # # # # # from bokeh.layouts import row
# # # # # # from random import randint
# # # # # # from functools import partial
# # # # # # from bokeh.models import Button

# # # # # # # Create a data source for the lines
# # # # # # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # # # # # Create a figure
# # # # # # p = figure(width=800, height=400, title='Updating Lines')

# # # # # # # Create four line renderers
# # # # # # renderer1 = p.line('x', 'y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # # # # # renderer2 = p.line('x', 'y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # # # # # renderer3 = p.line('x', 'y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # # # # # renderer4 = p.line('x', 'y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # # # # # Update the lines with random data
# # # # # # def update_lines():
# # # # # #     new_data = dict(
# # # # # #         x=[1, 2, 3, 4],  # x-values remain constant
# # # # # #         y1=[randint(0, 10) for _ in range(4)],
# # # # # #         y2=[randint(0, 10) for _ in range(4)],
# # # # # #         y3=[randint(0, 10) for _ in range(4)],
# # # # # #         y4=[randint(0, 10) for _ in range(4)]
# # # # # #     )
# # # # # #     source.data = new_data

# # # # # # # Create a callback to update the lines every 5 seconds
# # # # # # callback = partial(update_lines)

# # # # # # # Create a button to start updating
# # # # # # button = Button(label='Start Updating', button_type='success')
# # # # # # button.on_click(callback)

# # # # # # # Add the lines and button to the document
# # # # # # curdoc().add_root(row(p, button))

# # # # # # # Initial update
# # # # # # update_lines()



# # # # # from bokeh.io import curdoc
# # # # # from bokeh.models import ColumnDataSource
# # # # # from bokeh.plotting import figure
# # # # # from bokeh.layouts import row
# # # # # from random import randint
# # # # # from functools import partial

# # # # # # Create a data source for the lines
# # # # # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # # # # Create a figure
# # # # # p = figure(width=800, height=400, title='Updating Lines')

# # # # # # Create four line renderers
# # # # # renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # # # # renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # # # # renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # # # # renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # # # # Update the lines with random data
# # # # # def update_lines():
# # # # #     new_data = dict(
# # # # #         x=[1, 2, 3, 4],  # x-values remain constant
# # # # #         y1=[randint(0, 10) for _ in range(4)],
# # # # #         y2=[randint(0, 10) for _ in range(4)],
# # # # #         y3=[randint(0, 10) for _ in range(4)],
# # # # #         y4=[randint(0, 10) for _ in range(4)]
# # # # #     )
# # # # #     source.stream(new_data, rollover=4)

# # # # # # Create a callback to update the lines every 2 seconds
# # # # # callback = partial(update_lines)

# # # # # # Add the lines to the document
# # # # # curdoc().add_root(row(p))

# # # # # # Periodically update the lines every 2 seconds
# # # # # curdoc().add_periodic_callback(callback, 2000)


# # # # from bokeh.io import curdoc
# # # # from bokeh.models import ColumnDataSource
# # # # from bokeh.plotting import figure
# # # # from bokeh.layouts import row
# # # # from random import randint
# # # # from functools import partial
# # # # from bokeh.models import CDSView, IndexFilter

# # # # # Create a data source for the lines
# # # # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # # # Create a figure
# # # # p = figure(width=800, height=400, title='Updating Lines')

# # # # # Create four line renderers
# # # # renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # # # renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # # # renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # # # renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # # # Update the lines with random data
# # # # def update_lines():
# # # #     new_data = dict(
# # # #         x=source.data['x'] + [source.data['x'][-1] + 1],  # Append a new x value
# # # #         y1=source.data['y1'] + [randint(0, 10)],
# # # #         y2=source.data['y2'] + [randint(0, 10)],
# # # #         y3=source.data['y3'] + [randint(0, 10)],
# # # #         y4=source.data['y4'] + [randint(0, 10)]
# # # #     )
# # # #     source.data = new_data

# # # #     # Update the x-range of the plot to show the latest points
# # # #     start_index = max(0, len(source.data['x']) - 10)  # Show the last 10 points
# # # #     end_index = len(source.data['x'])
# # # #     view = CDSView(source=source, filters=[IndexFilter(indices=list(range(start_index, end_index)))])
# # # #     p.x_range.update(start=source.data['x'][start_index], end=source.data['x'][end_index-1])
# # # #     p.y_range.update(start=min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1,
# # # #                      end=max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1)
# # # #     renderer1.view = view
# # # #     renderer2.view = view
# # # #     renderer3.view = view
# # # #     renderer4.view = view

# # # # # Create a callback to update the lines every 2 seconds
# # # # callback = partial(update_lines)

# # # # # Add the lines to the document
# # # # curdoc().add_root(row(p))

# # # # # Periodically update the lines every 2 seconds
# # # # curdoc().add_periodic_callback(callback, 2000)


# # # from bokeh.io import curdoc
# # # from bokeh.models import ColumnDataSource, CDSView, IndexFilter
# # # from bokeh.plotting import figure
# # # from bokeh.layouts import row
# # # from random import randint
# # # from functools import partial
# # # from bokeh.models import Button

# # # # Create a data source for the lines
# # # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # # Create a figure
# # # p = figure(width=800, height=400, title='Updating Lines')

# # # # Create four line renderers
# # # renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # # renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # # renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # # renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # # Update the lines with random data
# # # def update_lines():
# # #     new_data = dict(
# # #         x=source.data['x'] + [source.data['x'][-1] + 1],  # Append a new x value
# # #         y1=source.data['y1'] + [randint(0, 10)],
# # #         y2=source.data['y2'] + [randint(0, 10)],
# # #         y3=source.data['y3'] + [randint(0, 10)],
# # #         y4=source.data['y4'] + [randint(0, 10)]
# # #     )
# # #     source.data = new_data

# # #     # Update the x-range of the plot to show the latest points
# # #     start_index = max(0, len(source.data['x']) - 10)  # Show the last 10 points
# # #     end_index = len(source.data['x'])
# # #     view = CDSView(source=source, filters=[IndexFilter(indices=list(range(start_index, end_index)))])
# # #     renderer1.view = view
# # #     renderer2.view = view
# # #     renderer3.view = view
# # #     renderer4.view = view

# # #     # Update the x-range and y-range of the plot
# # #     p.x_range.update(start=min(source.data['x']), end=max(source.data['x']))
# # #     p.y_range.update(start=min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1,
# # #                      end=max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1)

# # # # Create a callback to update the lines every 2 seconds
# # # callback = partial(update_lines)

# # # # Add the lines to the document
# # # curdoc().add_root(row(p))

# # # # Periodically update the lines every 2 seconds
# # # curdoc().add_periodic_callback(callback, 2000)



# # from bokeh.io import curdoc
# # from bokeh.models import ColumnDataSource, CDSView, IndexFilter
# # from bokeh.plotting import figure
# # from bokeh.layouts import row
# # from random import randint
# # from functools import partial
# # from bokeh.models import Button

# # # Create a data source for the lines
# # source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # # Create a figure
# # p = figure(width=800, height=400, title='Updating Lines')

# # # Create four line renderers
# # renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# # renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# # renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# # renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # # Update the lines with random data
# # def update_lines():
# #     new_data = dict(
# #         x=source.data['x'] + [source.data['x'][-1] + 1],  # Append a new x value
# #         y1=source.data['y1'] + [randint(0, 10)],
# #         y2=source.data['y2'] + [randint(0, 10)],
# #         y3=source.data['y3'] + [randint(0, 10)],
# #         y4=source.data['y4'] + [randint(0, 10)]
# #     )
# #     source.data = new_data

# #     # Update the x-range of the plot to show the latest points
# #     start_index = max(0, len(source.data['x']) - 10)  # Show the last 10 points
# #     end_index = len(source.data['x'])
# #     view = CDSView(source=source, filters=[IndexFilter(indices=list(range(start_index, end_index)))])
# #     renderer1.view = view
# #     renderer2.view = view
# #     renderer3.view = view
# #     renderer4.view = view

# #     # Update the x-range and y-range of the plot
# #     p.x_range.update(start=min(source.data['x']), end=max(source.data['x']))
# #     p.y_range.update(start=min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1,
# #                      end=max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1)

# # # Create a callback to update the lines every 2 seconds
# # callback = partial(update_lines)

# # # Add the lines to the document
# # curdoc().add_root(row(p))

# # # Initial update
# # update_lines()

# # # Periodically update the lines every 2 seconds
# # curdoc().add_periodic_callback(callback, 2000)




# # Working

# from bokeh.io import curdoc
# from bokeh.models import ColumnDataSource, CDSView, IndexFilter
# from bokeh.plotting import figure
# from bokeh.layouts import row
# from random import randint
# from functools import partial

# # Create a data source for the lines
# source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # Create a figure
# p = figure(width=800, height=400, title='Updating Lines')

# # Create four line renderers
# renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # Update the lines with random data
# def update_lines():
#     if not source.data['x']:  # Check if x data is empty
#         new_x = [0]
#     else:
#         new_x = [source.data['x'][-1] + 1]  # Append a new x value

#     new_data = dict(
#         x=source.data['x'] + new_x,
#         y1=source.data['y1'] + [randint(0, 10)],
#         y2=source.data['y2'] + [randint(0, 10)],
#         y3=source.data['y3'] + [randint(0, 10)],
#         y4=source.data['y4'] + [randint(0, 10)]
#     )
#     source.data = new_data

#     # Update the x-range of the plot to show the latest points
#     start_index = max(0, len(source.data['x']) - 10)  # Show the last 10 points
#     end_index = len(source.data['x'])
#     view = CDSView(source=source, filters=[IndexFilter(indices=list(range(start_index, end_index)))])
#     renderer1.view = view
#     renderer2.view = view
#     renderer3.view = view
#     renderer4.view = view

#     # Update the x-range and y-range of the plot
#     p.x_range.update(start=min(source.data['x']), end=max(source.data['x']))
#     p.y_range.update(start=min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1,
#                      end=max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1)

# # Create a callback to update the lines every 2 seconds
# callback = partial(update_lines)

# # Add the lines to the document
# curdoc().add_root(row(p))

# # Initial update
# update_lines()

# # Periodically update the lines every 2 seconds
# curdoc().add_periodic_callback(callback, 2000)


# Above working 


# from bokeh.io import curdoc
# from bokeh.models import ColumnDataSource
# from bokeh.plotting import figure
# from bokeh.layouts import row
# from random import randint
# from functools import partial

# # Create a data source for the lines
# source = ColumnDataSource(data=dict(x=[], y1=[], y2=[], y3=[], y4=[]))

# # Create a figure
# p = figure(width=800, height=400, title='Updating Lines')

# # Create four line renderers
# renderer1 = p.line(x='x', y='y1', line_width=2, color='blue', legend_label='Line 1', source=source)
# renderer2 = p.line(x='x', y='y2', line_width=2, color='red', legend_label='Line 2', source=source)
# renderer3 = p.line(x='x', y='y3', line_width=2, color='green', legend_label='Line 3', source=source)
# renderer4 = p.line(x='x', y='y4', line_width=2, color='orange', legend_label='Line 4', source=source)

# # Update the lines with random data
# def update_lines():
#     new_data = dict(
#         x=source.data['x'] + [source.data['x'][-1] + 1],
#         y1=source.data['y1'] + [randint(0, 10)],
#         y2=source.data['y2'] + [randint(0, 10)],
#         y3=source.data['y3'] + [randint(0, 10)],
#         y4=source.data['y4'] + [randint(0, 10)]
#     )
#     source.data = new_data

#     # Update the x-range of the plot to show the latest points
#     p.x_range.start = max(0, source.data['x'][-10])  # Show the last 10 points
#     p.x_range.end = source.data['x'][-1]

#     # Update the y-range of the plot
#     p.y_range.start = min(min(source.data['y1']), min(source.data['y2']), min(source.data['y3']), min(source.data['y4'])) - 1
#     p.y_range.end = max(max(source.data['y1']), max(source.data['y2']), max(source.data['y3']), max(source.data['y4'])) + 1

# # Create a callback to update the lines every 2 seconds
# callback = partial(update_lines)

# # Add the lines to the document
# curdoc().add_root(row(p))

# # Initial update
# update_lines()

# # Periodically update the lines every 2 seconds
# curdoc().add_periodic_callback(callback, 2000)




# Working perfectly !!!
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
curdoc().add_periodic_callback(callback, 2000)
# ^Working perfectly !!!