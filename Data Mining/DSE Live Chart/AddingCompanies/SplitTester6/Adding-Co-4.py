from Utils.Utilities import *
from Utils.ColDataSource import *

# If import/run from parent directory
# from AddingCompanies.DSEStreamerUtilities.Utilities import *

# from datetime import datetime, timedelta
# from bokeh.models import  Range1d
# start_time = datetime.now()
# start_time -= timedelta(minutes=30)
# end_time = start_time + timedelta(hours=24)

p = figure(x_axis_type='datetime', 
           # y_range=(-100, 100),
           width=2150, height=1400,    # 950 
           title="Dhaka Stock Exchange Live Change",
          )

y_range=(-100, 100)
from bokeh.models import Range1d
p.y_range = Range1d(*y_range)

p.title.align = "center"
# Set x-axis and y-axis labels
p.xaxis.axis_label = "Date-Time"
p.yaxis.axis_label = "Percentage Change (%)"

p.xaxis.ticker = DatetimeTicker() # commented this and added below 



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




# company_lst = ['BEXIMCO', 
#               #  'UNITED_POWER_GENERATION', 'SALVO_CHEMICAL',
#               'EHL',
#                'MARICO',
#               ]

# company_symbol_lst = ['s',
                     
#                      'c',
#                      ]


company_lst = [
                'MARICO',
                'OLYMPIC',
                'BSCCL',
                'SQUARETEXT',
    
                'APEXFOODS',
                'EHL',
                'GSPFINANCE',
                'IPDC',
    
                'MATINSPINN',
                'SALVOCHEM',
                'TRUSTBANK',


    #################################
                'ACMELAB',
                'ACIFORMULA',
                'JAMUNAOIL',
                'HWAWELLTEX',
    
                'DOREENPWR',
                'BSC',
                'INTRACO',
                'FORTUNE',

                'GPHISPAT',
                'RENATA', 
                'ANWARGALV',
                'BDCOM',

                'BERGERPBL',
                'PHARMAID',
                'PARAMOUNT',
                'RAHIMAFOOD',
    # #################################
                'IDLC',
                # 'KAY&QUE',
                'LINDEBD',
                'MJLBD',

                'NPOLYMER',
    # #################################
                'UPGDCL',
                'KPCL',
                'GPHISPAT',
                'BSCCL',

                # 'AMCL(PRAN)',
                'ACI',
                'SQURPHARMA',
                'SPCL',

                'POWERGRID',
                'BATBC',
                'ARAMIT',

                
                
                
    
    
              ]

company_symbol_lst = [                   
                     'd',
                     'd',
                     'd',
                     'd',
    
                     'd',
                     'd',
                     'd',
                     'd',

                     'd',
                     'd',
                     'd',
                     #################
                     'd+',
                     'd+',
                     'd+',
                     'd+',

                     'd+',
                     'd+',
                     'd+',
                     'd+',

                     'd+',
                     'd+',
                     'd+',
                     'd+',

                     'd+',
                     'd+',
                     'd+',
                     'd+',
                     #################
                     't',
                     't',
                     't',
                     't',
    
                     't',
                     #################
                     'c',
                     'c',
                     'c',
                     'c',

                     'c',
                     'c',
                     'c',
                     'c',

                     'c',
                     'c',
                     'c',
                    #################
                     ]

source = company_col_gen(company_lst)

from Utils.Glyphs import generate_gly_dictionary





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
    # p.add_tools(draw_hovertools(curr_gly[val_1], curr_gly[val_2]))
    p.add_tools(draw_hovertool(curr_gly[val_1], curr_gly[val_2], company_lst[i]))

         
                                





# Add the legend to the figure
p.add_layout(legend, 'left')

# Increase the size of the legend symbols
legend.label_text_font_size = "14pt"
legend.label_width = 50  # Adjust the width of the legend labels
legend.glyph_width = 50  # Adjust the width of the legend symbols
legend.spacing = 10  # Adjust the spacing between legend items
legend.propagate_hover = True



from datetime import datetime, timedelta
from bokeh.models import DataRange1d

# Update the x-axis range
current_time = datetime.now()
start_range = current_time - timedelta(minutes=30)
end_range = current_time + timedelta(hours=24)
p.x_range.start = start_range - timedelta(minutes=30)
p.x_range.end = end_range




# p.x_range = DataRange1d()  # commented this to see if range works



def update_data():
                
                all_tr = get_all_data()
                # stream_data = dict(x=[datetime.now()])
                stream_data = dict(x=[datetime.now()])
                for i in range(len(company_lst)):
                    stream_data.update(get_co_data(company_lst[i], all_tr)) 
                    
                new_data = stream_data

                # Added this
                # start_range = start_time - timedelta(minutes=30)
                # end_range = start_time + timedelta(hours=24)
                # p.x_range.start = start_range
                # p.x_range.end = end_range
    
                source.stream(new_data, 
                              # 100
                              1000
                             )
                

# Configure the document
curdoc().add_root(column(p))

update_data()

# Add the periodic callback to update the data
curdoc().add_periodic_callback(update_data, 180000)  # 180000   # 3000


# Perfection

