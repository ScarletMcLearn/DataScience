import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.callbacks import Points, InputDeviceState

# Import necessary modules and libraries

# Create an empty figure with subplots
fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)

# Create empty arrays to store the data
x_data = []
y_data = []
colors = []

# Create the initial plot with empty data
line_plot = go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color='gray'), name='Percentage Change')
fig.append_trace(line_plot, row=1, col=1)

scatter_plot = go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color='gray'), name='Trading Code')
fig.append_trace(scatter_plot, row=2, col=1)

# Create the layout
fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',  # Set x-axis title
        range=[0, 10],  # Initial x-axis range
        showgrid=True,  # Display gridlines on the x-axis
    ),
    yaxis=dict(
        title='Percentage Change',  # Set y-axis title
        showgrid=True,  # Display gridlines on the y-axis
    ),
    xaxis2=dict(
        title='Time',  # Set second x-axis title
        showgrid=True,  # Display gridlines on the second x-axis
    ),
    yaxis2=dict(
        title='Trading Code',  # Set second y-axis title
        showgrid=True,  # Display gridlines on the second y-axis
        range=[0, 393],  # Fixed y-axis range for trading code
        dtick=50,  # Tick interval for y-axis
    ),
    hovermode='x unified',  # Show hover information for both subplots
)


# Create a custom color scale for positive and negative changes
color_scale = [[0, 'red'], [1, 'green']]  # Change the colors as desired

# Create a Points callback to update the plot with new data
def update_plot(trace, points, selector):
    global x_data, y_data, colors

    # Get the new data from the real-time source
    new_x = points.xs[0]['x']
    new_y = points.xs[0]['y']
    new_color = 'red' if new_y < 0 else 'green'

    # Append the new data to the arrays
    x_data.append(new_x)
    y_data.append(new_y)
    colors.append(new_color)

    # Update the line plot trace
    fig.data[0].x = x_data
    fig.data[0].y = y_data
    fig.data[0].line.color = colors

    # Update the scatter plot trace
    fig.data[1].x = x_data
    fig.data[1].y = [393] * len(x_data)  # Fixed y-axis value for trading code
    fig.data[1].marker.color = colors


# Create a Points object with the callback function
callback_points = Points(fig.data[0])
callback_points.on_add(update_plot)

# Create InputDeviceState to enable drag-to-scroll functionality
ids = [callback_points.id]
input_state = InputDeviceState(ids)

# Create the animation frames for smooth transitions and updates
animation_frames = [dict(data=fig.data)]


fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',  # Set x-axis title
        range=[0, 10],  # Initial x-axis range
        showgrid=True,  # Display gridlines on the x-axis
    ),
    yaxis=dict(
        title='Percentage Change',  # Set y-axis title
        showgrid=True,  # Display gridlines on the y-axis
    ),
    xaxis2=dict(
        title='Time',  # Set second x-axis title
        showgrid=True,  # Display gridlines on the second x-axis
    ),
    yaxis2=dict(
        title='Trading Code',  # Set second y-axis title
        showgrid=True,  # Display gridlines on the second y-axis
        range=[0, 393],  # Fixed y-axis range for trading code
        dtick=50,  # Tick interval for y-axis
    ),
    hovermode='x unified',  # Show hover information for both subplots
    updatemenus=[
        dict(
            type='buttons',
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[None, {'frame': {'duration': 100, 'redraw': False}, 'fromcurrent': True, 'transition': {'duration': 0}}],
                ),
                dict(
                    label='Pause',
                    method='animate',
                    args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}],
                ),
                dict(
                    label='Reset',
                    method='animate',
                    args=[None, {'frame': {'duration': 0, 'redraw': True}, 'transition': {'duration': 0}}],
                ),
            ],
            direction='left',
            pad={'r': 10, 't': 10},
            showactive=False,
            x=0,
            xanchor='right',
            y=1.15,
            yanchor='top'
        ),
    ],
    sliders=[
        dict(
            active=0,
            currentvalue={'prefix': 'Zoom Level: '},
            pad={'t': 50},
            steps=[],
        ),
    ],
)


# Update the steps for the slider based on the number of data points
num_data_points = 100  # Replace with the actual number of data points
for i in range(num_data_points):
    frame = dict(
        args=[[i], {'frame': {'duration': 300, 'redraw': False}, 'mode': 'immediate'}],
        label=str(i),
        method='animate',
    )
    fig.layout.sliders[0].steps.append(frame)


# Create tooltips using custom hovertemplate for the line plot
fig.data[0].hovertemplate = (
    '<b>Trading Code:</b> %{customdata[0]}<br>' +
    '<b>Last Trading Price:</b> %{customdata[1]:.2f}<br>' +
    '<b>Last High:</b> %{customdata[2]:.2f}<br>' +
    '<b>Last Low:</b> %{customdata[3]:.2f}<br>' +
    '<b>Close Price:</b> %{customdata[4]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{customdata[5]:.2f}<br>' +
    '<b>Percentage Change:</b> %{customdata[6]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{customdata[7]}<br>' +
    '<b>Value of Trades:</b> %{customdata[8]:.2f}<br>' +
    '<b>Volume:</b> %{customdata[9]}'
)

# Create tooltips using custom hovertemplate for the scatter plot
fig.data[1].hovertemplate = (
    '<b>Trading Code:</b> %{customdata}<br>' +
    '<b>Last Trading Price:</b> %{x:.2f}<br>' +
    '<b>Last High:</b> %{y[0]:.2f}<br>' +
    '<b>Last Low:</b> %{y[1]:.2f}<br>' +
    '<b>Close Price:</b> %{y[2]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{y[3]:.2f}<br>' +
    '<b>Percentage Change:</b> %{y[4]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{y[5]}<br>' +
    '<b>Value of Trades:</b> %{y[6]:.2f}<br>' +
    '<b>Volume:</b> %{y[7]}'
)


# Enable drag-to-scroll functionality
fig.show(config={'scrollZoom': True})



# Enable streaming updates
stream = go.Stream(
    token='your_stream_token',  # Replace with your stream token
    maxpoints=393,  # Number of points per update
)



# Open the stream
stream.open()


# Continuously update the plot with new data
while True:
    # Get new data from the real-time source
    trading_code = ...
    last_trading_price = ...
    last_high = ...
    last_low = ...
    close_price = ...
    yesterday_close_price = ...
    percentage_change = ...
    number_of_trades = ...
    value_of_trades = ...
    volume = ...

    # Append the new data to the arrays
    x_data.append(new_x)
    y_data.append(new_y)
    colors.append(new_color)

    # Send the new data to the plotly stream
    stream.write(dict(
        x=new_x,
        y=new_y,
        customdata=[
            trading_code,
            last_trading_price,
            last_high,
            last_low,
            close_price,
            yesterday_close_price,
            percentage_change,
            number_of_trades,
            value_of_trades,
            volume,
        ]
    ))


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# Create empty arrays to store the data
x_data = []
y_data = []
colors = []



# Create the initial plot with empty data
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
line_plot = go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color='gray'), name='Percentage Change')
scatter_plot = go.Scatter(x=x_data, y=y_data, mode='markers', marker=dict(color='gray'), name='Trading Code')


# Create a custom color scale for positive and negative changes
color_scale = [[0, 'red'], [1, 'green']]  # Change the colors as desired


# Add the line plot and scatter plot to the figure
fig.add_trace(line_plot, row=1, col=1)
fig.add_trace(scatter_plot, row=2, col=1)


# Update the layout
fig.update_layout(
    height=600,
    title='Live Time Series Streaming Plot',
    xaxis=dict(
        title='Time',
        showgrid=True,
        range=[datetime.datetime.now() - datetime.timedelta(hours=1), datetime.datetime.now()]  # Initial x-axis range
    ),
    yaxis=dict(
        title='Percentage Change',
        showgrid=True
    ),
    xaxis2=dict(
        title='Time',
        showgrid=True
    ),
    yaxis2=dict(
        title='Trading Code',
        showgrid=True,
        range=[0, 393]  # Fixed y-axis range for trading code
    ),
    hovermode='x unified',  # Show hover information for both subplots
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    plot_bgcolor='white'
)



# Create tooltips using custom hovertemplate for the line plot
line_plot.hovertemplate = (
    '<b>Trading Code:</b> %{customdata[0]}<br>' +
    '<b>Last Trading Price:</b> %{customdata[1]:.2f}<br>' +
    '<b>Last High:</b> %{customdata[2]:.2f}<br>' +
    '<b>Last Low:</b> %{customdata[3]:.2f}<br>' +
    '<b>Close Price:</b> %{customdata[4]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{customdata[5]:.2f}<br>' +
    '<b>Percentage Change:</b> %{customdata[6]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{customdata[7]}<br>' +
    '<b>Value of Trades:</b> %{customdata[8]:.2f}<br>' +
    '<b>Volume:</b> %{customdata[9]}'
)



# Create tooltips using custom hovertemplate for the scatter plot
scatter_plot.hovertemplate = (
    '<b>Trading Code:</b> %{customdata}<br>' +
    '<b>Last Trading Price:</b> %{x:.2f}<br>' +
    '<b>Last High:</b> %{y[0]:.2f}<br>' +
    '<b>Last Low:</b> %{y[1]:.2f}<br>' +
    '<b>Close Price:</b> %{y[2]:.2f}<br>' +
    '<b>Yesterday Close Price:</b> %{y[3]:.2f}<br>' +
    '<b>Percentage Change:</b> %{y[4]:.2f}%<br>' +
    '<b>Number of Trades:</b> %{y[5]}<br>' +
    '<b>Value of Trades:</b> %{y[6]:.2f}<br>' +
    '<b>Volume:</b> %{y[7]}'
)


# Enable drag-to-scroll functionality
fig.update_xaxes(dragmode='pan')


# Enable zooming functionality
fig.update_xaxes(rangeselector=dict(
    buttons=list([
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(count=1, label='1d', step='day', stepmode='backward'),
        dict(count=7, label='1w', step='day', stepmode='backward'),
        dict(count=1, label='1m', step='month', stepmode='backward'),
        dict(count=3, label='3m', step='month', stepmode='backward'),
        dict(count=6, label='6m', step='month', stepmode='backward'),
        dict(count=1, label='1y', step='year', stepmode='backward'),
        dict(step='all')
    ])
))


# Enable animation
fig.update_layout(transition=dict(duration=1000))


# Show the figure
fig.show()




