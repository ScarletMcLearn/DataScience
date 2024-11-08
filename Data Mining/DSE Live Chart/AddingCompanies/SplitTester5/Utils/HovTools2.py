from bokeh.models import HoverTool



# def draw_hovertool(renderer_1, renderer_2, company):
#     pc = '@' + company + '_PC'
#     ltp = '@' + company + '_LTP'
#     lh = '@' + company + '_LH'
#     ll = '@' + company + '_LL'
#     cp = '@' + company + '_CP'
#     ycp = '@' + company + '_YCP'
#     nott = '@' + company + '_NoT'
#     vot = '@' + company + '_VoT'
#     vol = '@' + company + '_Vol'
#     return HoverTool(
#                         renderers=[renderer_1, renderer_2], 
#                 tooltips=[
#                     ('Company Data', ''), 
#                     ('Company Name', company), 
#                     ('Date time', '@x{%dth %B - %I:%M:%S %p}'), 
#                     ('Percentage Change', pc),
#                     ('Last Trading Price', ltp),
#                     ('Last High', lh),
#                     ('Last Low', ll),
#                     ('Closing Price', cp),
#                     ("Yesterday's Closing Price", ycp),
#                     ('Number of Trades', nott),
#                     ('Values of Trades', vot),
#                     ('Volume of Trades', vol),
#                         ], 
#                     formatters={'@x': 'datetime'}
#                     )







    
def draw_hovertools(renderer_1, renderer_2):
    return draw_hovertool(renderer_1, renderer_2, 'AAMRANET')
# p.add_tools(hover_tool_2)











# def draw_hovertool(renderer_1, renderer_2, company):
#     pc = '@' + company + '_PC'
#     ltp = '@' + company + '_LTP'
#     lh = '@' + company + '_LH'
#     ll = '@' + company + '_LL'
#     cp = '@' + company + '_CP'
#     ycp = '@' + company + '_YCP'
#     nott = '@' + company + '_NoT'
#     vot = '@' + company + '_VoT'
#     vol = '@' + company + '_Vol'
#     return HoverTool(
#         renderers=[renderer_1, renderer_2],
#         tooltips="""
#     <div>
#         <div>
#             <span style="font-weight: bold; font-size:20px">Company Data</span>
#         </div>
#         <div>
#             <span>Company Name: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Date time: </span>
#             <span>@x</span>
#         </div>
#         <div>
#             <span>Percentage Change: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Last Trading Price: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Last High: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Last Low: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Closing Price: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Yesterday's Closing Price: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Number of Trades: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Values of Trades: </span>
#             <span>{}</span>
#         </div>
#         <div>
#             <span>Volume of Trades: </span>
#             <span>{}</span>
#         </div>
#     </div>
# """.format(company, pc, ltp, lh, ll, cp, ycp, nott, vot, vol),
#         formatters={
#             'x'      : 'datetime',
#         }
#     )

# {{%d}}th {{%B}} - {{%I:%M:%S %p}}





           






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
        tooltips="""
    <div>
        <div>
            <span style="font-weight: bold; font-size:20px">Company Data</span>
        </div>
        <div>
            <span>Company Name: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Date time: </span>
            <span>@x</span>
            <span>@x{{%dth %B - %I:%M:%S %p}}</span>
        </div>
        <div>
            <span>Percentage Change: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Last Trading Price: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Last High: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Last Low: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Closing Price: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Yesterday's Closing Price: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Number of Trades: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Values of Trades: </span>
            <span>{}</span>
        </div>
        <div>
            <span>Volume of Trades: </span>
            <span>{}</span>
        </div>
    </div>
""".format(company, pc, ltp, lh, ll, cp, ycp, nott, vot, vol),
        formatters={
            'x'      : 'printf',
            
        }
    )

