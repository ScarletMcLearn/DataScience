from bokeh.models import HoverTool

# x_tooltip_label = 'Date time'
# x_tooltip_data = '@x{%dth %B - %I:%M:%S %p}'
# tooltip_title = 'Company Data'

def draw_hovertool(renderer_1, renderer_2, company):
    pc = '@' + company + '_PC'
    ltp = '@' + company + '_LTP'
    lh = '@' + company + '_LH'
    ll = '@' + company + '_LL'
    cp = '@' + company + '_CP'
    ycp = '@' + company + '_YCP'
    nott = '@' + company + '_NoT'
    vot = '@' + company + '_VoT'
    vol = '@' + company + '_Vol'
    return HoverTool(
                        renderers=[renderer_1, renderer_2], 
                tooltips=[
                    ('Company Data', ''), 
                    ('Company Name', company), 
                    ('Date time', '@x{%dth %B - %I:%M:%S %p}'), 
                    ('Percentage Change', pc),
                    ('Last Trading Price', ltp),
                    ('Last High', lh),
                    ('Last Low', ll),
                    ('Closing Price', cp),
                    ("Yesterday's Closing Price", ycp),
                    ('Number of Trades', nott),
                    ('Values of Trades', vot),
                    ('Volume of Trades', vol),
                        ], 
                    formatters={'@x': 'datetime'}
                    )

hover_tool_1 = HoverTool(renderers=[ia1, ib1], tooltips=[(tooltip_title, ''), (x_tooltip_label, x_tooltip_data), (y_tooltip_label, '@y1')], formatters={'@x': 'datetime'})



# Add the HoverTool to the figure
# p.add_tools(hover_tool_1)

# hover_tool_2 = HoverTool(
#                         renderers=[ia2, ib2], 
#                 tooltips=[
#                     (tooltip_title, ''), 
#                     ('Company Name', 'AAMRANET'), 
#                     (x_tooltip_label, x_tooltip_data), 
#                     ('Percentage Change', '@AAMRANET_PC'),
#                     ('Last Trading Price', '@AAMRANET_LTP'),
#                     ('Last High', '@AAMRANET_LH'),
#                     ('Last Low', '@AAMRANET_LL'),
#                     ('Closing Price', '@AAMRANET_CP'),
#                     ("Yesterday's Closing Price", '@AAMRANET_YCP'),
#                     ('Number of Trades', '@AAMRANET_NoT'),
#                     ('Values of Trades', '@AAMRANET_VoT'),
#                     ('Volume of Trades', '@AAMRANET_Vol'),
#                         ], 
#                     formatters={'@x': 'datetime'}
#                     )

hover_tool_2 = draw_hovertool(ia2, ib2, 'AAMRANET')
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

