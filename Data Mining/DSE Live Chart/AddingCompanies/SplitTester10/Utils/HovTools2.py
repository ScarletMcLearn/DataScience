from bokeh.models import HoverTool


    
def draw_hovertools(renderer_1, renderer_2):
    return draw_hovertool(renderer_1, renderer_2, 'AAMRANET')
# p.add_tools(hover_tool_2)



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
    sz = '@' + company + '_Size'
    return HoverTool(
        renderers=[renderer_1, renderer_2],
        tooltips="""
    <div>
        <div>
            <span style="font-weight: bold; font-size:17px; color:#00d2ff;">Company Data</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Company Name: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Date time: </span>
            
            <span style="font-weight: bold; font-size:15px">@x{{%dth %B - %I:%M:%S %p}}</span>
           
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Percentage Change: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Last Trading Price: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Last High: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Last Low: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Closing Price: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Yesterday's Closing Price: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Number of Trades: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Values of Trades: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Volume of Trades: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size:15px; color:#00d2ff;">Size of Glyphs: </span>
            <span style="font-weight: bold; font-size:15px">{}</span>
        </div>
    </div>
""".format(company, pc, ltp, lh, ll, cp, ycp, nott, vot, vol, sz),
        formatters={
            # 'x'      : 'printf',
            '@x'      : 'datetime',
            
        }
    )



