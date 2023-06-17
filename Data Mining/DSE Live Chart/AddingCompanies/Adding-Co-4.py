from DSEStreamerUtilities.Utilities import *
from DSEStreamerUtilities.ColDataSource import *

# If import/run from parent directory
# from AddingCompanies.DSEStreamerUtilities.Utilities import *


p = figure(x_axis_type='datetime', 
           y_range=(-100, 100),
           # x_range = (0, 100),
           width=2150, height=950, 
           # tools='pan,reset'
           title="Dhaka Stock Exchange Live Change",
           # sizing_mode='stretch_both',
          )


p.title.align = "center"
# Set x-axis and y-axis labels
p.xaxis.axis_label = "Date-Time"
p.yaxis.axis_label = "Percentage Change (%)"

p.xaxis.ticker = DatetimeTicker()

# Customize the time axis
p.xaxis.formatter = DatetimeTickFormatter(
                                          days ="%dth %B - %I:%M:%S %p",
                                          months ="%dth %B - %I:%M:%S %p",
                                          hours="%dth %B - %I:%M:%S %p",
                                          minutes="%dth %B - %I:%M:%S %p",
                                          seconds="%dth %B - %I:%M:%S %p",
                                         )

curdoc().theme = 'dark_minimal'







# Get the script start time
start_time = datetime.now()

# p.xaxis.ticker = SingleIntervalTicker(interval=3*1000)  # Interval in milliseconds


# # Create a custom ticker with 3-second intervals
# ticker = SingleIntervalTicker(interval=3000)  # 3000 milliseconds = 3 seconds
# p.xaxis[0].ticker = ticker



# # Define the global variables for the streaming data
# x_values = []
# y_1_values = []
# y_2_values = []

# AAMRANET_values = []
# AAMRATECH_values = []
# ABBANK_values = []


# Create a ColumnDataSource to store the data
# Commenting out this - although its working - to create new implementation
# source = ColumnDataSource(data=dict(x=x_values, y1=y_1_values, 
#                                     y2=y_2_values,
#                                     AAMRANET=AAMRANET_values,
#                                     AAMRATECH=AAMRATECH_values,
#                                     ABBANK=ABBANK_values,
#                                    ))


# New implementation
# source = ColumnDataSource(data=dict(x=x_values, 
                                    
#                                     y1=y_1_values, 
#                                     y2=y_2_values,  

#                                     AAMRANET_LTP=[],
#                                     AAMRANET_LH=[],
#                                     AAMRANET_LL=[],
#                                     AAMRANET_CP=[],
#                                     AAMRANET_YCP=[],
#                                     AAMRANET_PC=[],
#                                     AAMRANET_NoT=[],
#                                     AAMRANET_VoT=[],
#                                     AAMRANET_Vol=[],


#                                     UNITED_POWER_GENERATION_LTP=[],
#                                     UNITED_POWER_GENERATION_LH=[],
#                                     UNITED_POWER_GENERATION_LL=[],
#                                     UNITED_POWER_GENERATION_CP=[],
#                                     UNITED_POWER_GENERATION_YCP=[],
#                                     UNITED_POWER_GENERATION_PC=[],
#                                     UNITED_POWER_GENERATION_NoT=[],
#                                     UNITED_POWER_GENERATION_VoT=[],
#                                     UNITED_POWER_GENERATION_Vol=[],
                                    
#                                     SALVO_CHEMICAL_LTP=[],
#                                     SALVO_CHEMICAL_LH=[],
#                                     SALVO_CHEMICAL_LL=[],
#                                     SALVO_CHEMICAL_CP=[],
#                                     SALVO_CHEMICAL_YCP=[],
#                                     SALVO_CHEMICAL_PC=[],
#                                     SALVO_CHEMICAL_NoT=[],
#                                     SALVO_CHEMICAL_VoT=[],
#                                     SALVO_CHEMICAL_Vol=[],


#                                     RAHIMA_FOOD_CORP_LTP=[],
#                                     RAHIMA_FOOD_CORP_LH=[],
#                                     RAHIMA_FOOD_CORP_LL=[],
#                                     RAHIMA_FOOD_CORP_CP=[],
#                                     RAHIMA_FOOD_CORP_YCP=[],
#                                     RAHIMA_FOOD_CORP_PC=[],
#                                     RAHIMA_FOOD_CORP_NoT=[],
#                                     RAHIMA_FOOD_CORP_VoT=[],
#                                     RAHIMA_FOOD_CORP_Vol=[],


                                    
#                                     AAMRATECH=AAMRATECH_values,
#                                     ABBANK=ABBANK_values,
#                                    ))




# from DSEStreamerUtilities.Shapes import *
p, l1, ia1, ib1 = draw_shape_line(x_col_name='x', y_col_name='y1', source=source, figure=p, label='Testy time', shape='c')




p, l2, ia2, ib2 = draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=p, label='AAMRANET', shape='s')

p, l5, ia5, ib5 = draw_shape_line(x_col_name='x', y_col_name='UNITED_POWER_GENERATION_PC', source=source, figure=p, label='UNITED_POWER_GENERATION', shape='s')

p, l6, ia6, ib6 = draw_shape_line(x_col_name='x', y_col_name='SALVO_CHEMICAL_PC', source=source, figure=p, label='SALVO_CHEMICAL', shape='s')

p, l7, ia7, ib7 = draw_shape_line(x_col_name='x', y_col_name='RAHIMA_FOOD_CORP_PC', source=source, figure=p, label='RAHIMA_FOOD_CORP', shape='s')






p, l3, ia3, ib3 = draw_shape_line(x_col_name='x', y_col_name='AAMRATECH', source=source, figure=p, label='AAMRATECH', shape='t')

p, l4, ia4, ib4 = draw_shape_line(x_col_name='x', y_col_name='ABBANK', source=source, figure=p, label='ABBANK', shape='h')




legend = Legend(items=[l1, l2, l3, l4, l5, l6, l7, ], 
                location="top_left", 
                orientation="vertical",
               click_policy="hide"
               )

x_tooltip_label = 'Date time'
x_tooltip_data = '@x{%dth %B - %I:%M:%S %p}'
y_tooltip_label = 'Percentage change'
tooltip_title = 'Company Data'




# # This is working
# # Create a HoverTool and configure it
hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})



# Add the HoverTool to the figure
# p.add_tools(hover_tool_1)

hover_tool_2 = HoverTool(
                        renderers=[ia2, ib2], 
                tooltips=[
                    (tooltip_title, ''), 
                    ('Company Name', 'AAMRANET'), 
                    (x_tooltip_label, x_tooltip_data), 
                    ('Percentage Change', '@AAMRANET_PC'),
                    ('Last Trading Price', '@AAMRANET_LTP'),
                    ('Last High', '@AAMRANET_LH'),
                    ('Last Low', '@AAMRANET_LL'),
                    ('Closing Price', '@AAMRANET_CP'),
                    ("Yesterday's Closing Price", '@AAMRANET_YCP'),
                    ('Number of Trades', '@AAMRANET_NoT'),
                    ('Values of Trades', '@AAMRANET_VoT'),
                    ('Volume of Trades', '@AAMRANET_Vol'),
                        ], 
                    formatters={'@x': 'datetime'}
                    )
# p.add_tools(hover_tool_2)

                                   
                                





hover_tool_3 = HoverTool(renderers=[ia3, ib3], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRATECH')], formatters={'@x': 'datetime'})
# p.add_tools(hover_tool_3)

hover_tool_4 = HoverTool(renderers=[ia4, ib4], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@ABBANK')], formatters={'@x': 'datetime'})







hover_tool_5 = HoverTool(
                        renderers=[ia5, ib5], 
                tooltips=[
                    (tooltip_title, ''), 
                    ('Company Name', 'UNITED_POWER_GENERATION'), 
                    (x_tooltip_label, x_tooltip_data), 
                    ('Percentage Change', '@UNITED_POWER_GENERATION_PC'),
                    ('Last Trading Price', '@UNITED_POWER_GENERATION_LTP'),
                    ('Last High', '@UNITED_POWER_GENERATION_LH'),
                    ('Last Low', '@UNITED_POWER_GENERATION_LL'),
                    ('Closing Price', '@UNITED_POWER_GENERATION_CP'),
                    ("Yesterday's Closing Price", '@UNITED_POWER_GENERATION_YCP'),
                    ('Number of Trades', '@UNITED_POWER_GENERATION_NoT'),
                    ('Values of Trades', '@UNITED_POWER_GENERATION_VoT'),
                    ('Volume of Trades', '@UNITED_POWER_GENERATION_Vol'),
                        ], 
                    formatters={'@x': 'datetime'}
                    )






hover_tool_6 = HoverTool(
                        renderers=[ia6, ib6], 
                tooltips=[
                    (tooltip_title, ''), 
                    ('Company Name', 'SALVO_CHEMICAL'), 
                    (x_tooltip_label, x_tooltip_data), 
                    ('Percentage Change', '@SALVO_CHEMICAL_PC'),
                    ('Last Trading Price', '@SALVO_CHEMICAL_LTP'),
                    ('Last High', '@SALVO_CHEMICAL_LH'),
                    ('Last Low', '@SALVO_CHEMICAL_LL'),
                    ('Closing Price', '@SALVO_CHEMICAL_CP'),
                    ("Yesterday's Closing Price", '@SALVO_CHEMICAL_YCP'),
                    ('Number of Trades', '@SALVO_CHEMICAL_NoT'),
                    ('Values of Trades', '@SALVO_CHEMICAL_VoT'),
                    ('Volume of Trades', '@SALVO_CHEMICAL_Vol'),
                        ], 
                    formatters={'@x': 'datetime'}
                    )





hover_tool_7 = HoverTool(
                        renderers=[ia7, ib7], 
                tooltips=[
                    (tooltip_title, ''), 
                    ('Company Name', 'RAHIMA_FOOD_CORP'), 
                    (x_tooltip_label, x_tooltip_data), 
                    ('Percentage Change', '@RAHIMA_FOOD_CORP_PC'),
                    ('Last Trading Price', '@RAHIMA_FOOD_CORP_LTP'),
                    ('Last High', '@RAHIMA_FOOD_CORP_LH'),
                    ('Last Low', '@RAHIMA_FOOD_CORP_LL'),
                    ('Closing Price', '@RAHIMA_FOOD_CORP_CP'),
                    ("Yesterday's Closing Price", '@RAHIMA_FOOD_CORP_YCP'),
                    ('Number of Trades', '@RAHIMA_FOOD_CORP_NoT'),
                    ('Values of Trades', '@RAHIMA_FOOD_CORP_VoT'),
                    ('Volume of Trades', '@RAHIMA_FOOD_CORP_Vol'),
                        ], 
                    formatters={'@x': 'datetime'}
                    )


p.add_tools(
    hover_tool_1,
    hover_tool_2, hover_tool_3, hover_tool_4, hover_tool_5, hover_tool_6, hover_tool_7)





# Perfection Here
#######################################################################################




# Experimenting here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############################
#
#
# Experimenting here

# Create a HoverTool and configure it
# Increase font size using CSS styles
# hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # Increase font size using CSS styles
# hover_tool_1.tooltips = [(tooltip_title, ''),
#                         (x_tooltip_label, x_tooltip_data),
#                         (y_tooltip_label, '@y1')]


# # Create a HoverTool and configure it
# # hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # # Increase font size using CSS styles
# # hover_tool_1.tooltips = [(tooltip_title, ''),
# #                         (x_tooltip_label, x_tooltip_data),
# #                         (y_tooltip_label, '@y1')]

# # Add the HoverTool to the figure
# p.add_tools(hover_tool_1)



# TOOLTIPS = """
#     <div style="display: flex; justify-content: center;">
#         <div>
#             <span style="font-size: 17px; font-weight: bold;">@desc</span>
#         </div>
#         </div>
# """

# # Create a HoverTool and configure it
# hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(TOOLTIPS, ''), (tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})

# # Add the HoverTool to the figure
# # p.add_tools(hover_tool_1)

# hover_tool_2 = HoverTool(renderers=[ia2, ib2], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRANET')], formatters={'@x': 'datetime'})
# # p.add_tools(hover_tool_2)


# hover_tool_3 = HoverTool(renderers=[ia3, ib3], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@AAMRATECH')], formatters={'@x': 'datetime'})
# # p.add_tools(hover_tool_3)

# hover_tool_4 = HoverTool(renderers=[ia4, ib4], tooltips=[(x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@ABBANK')], formatters={'@x': 'datetime'})



# p.add_tools(hover_tool_1, hover_tool_2, hover_tool_3, hover_tool_4)





# # p, i2 = draw_shape(x_col_name='x', y_col_name='y1', source=source, figure=p, shape='c', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# # p, i3 = draw_shape(x_col_name='x', y_col_name='y1', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=8, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='10 10', )

# # legend_item = LegendItem(label="Circle Line", renderers=[i2, i3])

# p, i4 = draw_shape(x_col_name='x', y_col_name='y2', source=source, figure=p, shape='t', size=30, fill_color=mapper, border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# p, i5 = draw_shape(x_col_name='x', y_col_name='y2', source=source, figure=p, shape='l', size=30, fill_color='blue', border_color='white', border_width=3, alpha=0.3, line_smoothing=0.9, line_join='round', line_cap='round', line_alpha=0.6, line_dash='4 4', )

# legend_item = LegendItem(label="Circle Line", renderers=[i4, i5])








######################################
#
#
# Working from here again
#
#



# Add the legend to the figure
p.add_layout(legend, 'left')

# Increase the size of the legend symbols
legend.label_text_font_size = "14pt"
legend.label_width = 50  # Adjust the width of the legend labels
legend.glyph_width = 50  # Adjust the width of the legend symbols
legend.spacing = 10  # Adjust the spacing between legend items
legend.propagate_hover = True


def update_data():
                # AAMRANET= get_co_data(co_name='AAMRANET')['percentage_change']
                # time.sleep(random.randint(5, 10))
                # AAMRATECH= get_co_data(co_name='AAMRATECH')['percentage_change']
                # time.sleep(random.randint(5, 10))
                # ABBANK= get_co_data(co_name='ABBANK')['percentage_change']
                # time.sleep(random.randint(5, 10))
    
                new_data = dict(
                x=[datetime.now()],
                # x = source.data['x'][-1] + timedelta(seconds=4),
                y1=[10],
                y2=[20],
                # AAMRANET= [50],
                AAMRATECH= [40],
                ABBANK= [30],  



                AAMRANET_LTP=[100],
                AAMRANET_LH=[99],
                AAMRANET_LL=[98],
                AAMRANET_CP=[97],
                AAMRANET_YCP=[96],
                AAMRANET_PC=[95],
                AAMRANET_NoT=[94],
                AAMRANET_VoT=[93],
                AAMRANET_Vol=[92],


                UNITED_POWER_GENERATION_LTP=[100],
                UNITED_POWER_GENERATION_LH=[99],
                UNITED_POWER_GENERATION_LL=[98],
                UNITED_POWER_GENERATION_CP=[97],
                UNITED_POWER_GENERATION_YCP=[96],
                UNITED_POWER_GENERATION_PC=[34],
                UNITED_POWER_GENERATION_NoT=[94],
                UNITED_POWER_GENERATION_VoT=[93],
                UNITED_POWER_GENERATION_Vol=[92],


                SALVO_CHEMICAL_LTP=[100],
                SALVO_CHEMICAL_LH=[99],
                SALVO_CHEMICAL_LL=[98],
                SALVO_CHEMICAL_CP=[97],
                SALVO_CHEMICAL_YCP=[96],
                SALVO_CHEMICAL_PC=[10],
                SALVO_CHEMICAL_NoT=[94],
                SALVO_CHEMICAL_VoT=[93],
                SALVO_CHEMICAL_Vol=[92],



                RAHIMA_FOOD_CORP_LTP=[100],
                RAHIMA_FOOD_CORP_LH=[99],
                RAHIMA_FOOD_CORP_LL=[98],
                RAHIMA_FOOD_CORP_CP=[97],
                RAHIMA_FOOD_CORP_YCP=[96],
                RAHIMA_FOOD_CORP_PC=[1],
                RAHIMA_FOOD_CORP_NoT=[94],
                RAHIMA_FOOD_CORP_VoT=[93],
                RAHIMA_FOOD_CORP_Vol=[92],
                    
                # AAMRANET= [AAMRANET],
                # AAMRATECH= [AAMRATECH],
                # ABBANK= [ABBANK],     
                                )
                source.stream(new_data, 
                              # 100
                              1000
                             )

# Configure the document
curdoc().add_root(column(p))

update_data()

# Add the periodic callback to update the data
curdoc().add_periodic_callback(update_data, 3000)  # 180000   # 3000


# Perfection

