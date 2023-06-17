from Utils.Utilities import *
from Utils.ColDataSource import *

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




company_lst = ['AAMRANET', 
              #  'UNITED_POWER_GENERATION', 'SALVO_CHEMICAL',
              'RAHIMA_FOOD_CORP',
              ]

company_symbol_lst = ['s',
                     
                     'c'
                     ]

source = company_col_gen(company_lst)

from Utils.Glyphs import generate_gly_dictionary
# # l1, ia1, ib1, l2, ia2, ib2, l5, ia5, ib5, l6, ia6, ib6, l7, ia7, ib7, l3, ia3, ib3, l4, ia4, ib4 = glyph_renderer(source, figure=p)
# l1, ia1, ib1 = glyph_renderer(source, figure=p)




curr_gly = generate_gly_dictionary(source, p, company_lst, company_symbol_lst)

legend_items = []
for key in curr_gly.keys():
    if key.startswith('l'):
        legend_items.append(curr_gly[key])

legend = Legend(items=legend_items
                # [
                    #    #  curr_gly['l0'], 
                    #    # curr_gly['l1'], 
                    #    # # l2, l3, l4, l5, l6, l7, 
                    #     # legend_items
                    # curr_gly['l1'], curr_gly['l0'],
                      # ]
                , 
                location="top_left", 
                orientation="vertical",
               click_policy="hide"
               )

# x_tooltip_label = 'Date time'
# x_tooltip_data = '@x{%dth %B - %I:%M:%S %p}'
y_tooltip_label = 'Percentage change'
# tooltip_title = 'Company Data'




from Utils.HovTools2 import *
# hover_tool_1 = draw_hovertools(curr_gly['ia0'], curr_gly['ib0'])
# p.add_tools(hover_tool_1)

for i in range(len(company_lst)):
    val_1 = 'ia' + str(i)
    val_2 = 'ib' + str(i)
    p.add_tools(draw_hovertools(curr_gly[val_1], curr_gly[val_2]))

         
                                





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
                # y1=[10],
                # y2=[20],
                # AAMRATECH= [40],
                # ABBANK= [30],  



                AAMRANET_LTP=[100],
                AAMRANET_LH=[99],
                AAMRANET_LL=[98],
                AAMRANET_CP=[97],
                AAMRANET_YCP=[96],
                AAMRANET_PC=[95],
                AAMRANET_NoT=[94],
                AAMRANET_VoT=[93],
                AAMRANET_Vol=[92],


                # UNITED_POWER_GENERATION_LTP=[100],
                # UNITED_POWER_GENERATION_LH=[99],
                # UNITED_POWER_GENERATION_LL=[98],
                # UNITED_POWER_GENERATION_CP=[97],
                # UNITED_POWER_GENERATION_YCP=[96],
                # UNITED_POWER_GENERATION_PC=[34],
                # UNITED_POWER_GENERATION_NoT=[94],
                # UNITED_POWER_GENERATION_VoT=[93],
                # UNITED_POWER_GENERATION_Vol=[92],


                # SALVO_CHEMICAL_LTP=[100],
                # SALVO_CHEMICAL_LH=[99],
                # SALVO_CHEMICAL_LL=[98],
                # SALVO_CHEMICAL_CP=[97],
                # SALVO_CHEMICAL_YCP=[96],
                # SALVO_CHEMICAL_PC=[10],
                # SALVO_CHEMICAL_NoT=[94],
                # SALVO_CHEMICAL_VoT=[93],
                # SALVO_CHEMICAL_Vol=[92],



                RAHIMA_FOOD_CORP_LTP=[100],
                RAHIMA_FOOD_CORP_LH=[99],
                RAHIMA_FOOD_CORP_LL=[98],
                RAHIMA_FOOD_CORP_CP=[97],
                RAHIMA_FOOD_CORP_YCP=[96],
                RAHIMA_FOOD_CORP_PC=[1],
                RAHIMA_FOOD_CORP_NoT=[94],
                RAHIMA_FOOD_CORP_VoT=[93],
                RAHIMA_FOOD_CORP_Vol=[92],
                    
              
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

