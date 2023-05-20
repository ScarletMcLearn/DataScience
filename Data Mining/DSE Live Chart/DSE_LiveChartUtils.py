# from colorama import Fore, Style
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time, random
# from bokeh.plotting import figure, show, curdoc
# from bokeh.models import DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import ContinuousColorMapper
# from bokeh.palettes import Viridis256
# from bokeh.transform import linear_cmap
# from bokeh.palettes import Turbo256
# from bokeh.palettes import Category10, Category20, Category20b, Category20c
# from bokeh.plotting import figure, show, curdoc
# from bokeh.models import DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import ContinuousColorMapper
# from bokeh.palettes import Viridis256
# from bokeh.transform import linear_cmap
# from bokeh.palettes import Turbo256
# from bokeh.palettes import Category10, Category20, Category20b, Category20c
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool
# from datetime import datetime
# import random
# from bokeh.models import ContinuousColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.palettes import Viridis256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool
# from datetime import datetime
# import random
# from bokeh.models import ContinuousColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.palettes import Viridis256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool
# from datetime import datetime
# import random
# from bokeh.models import ContinuousColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.palettes import Viridis256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# from tqdm import tqdm
# import pandas as pd
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from datetime import datetime, timedelta
# import random
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# import random
# from datetime import datetime, timedelta
# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
# from datetime import datetime
# import random
# from bokeh.models import LinearColorMapper
# from bokeh.palettes import Turbo256
# import random
# from datetime import datetime, timedelta
# from bokeh.plotting import figure, show

from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random
from bokeh.plotting import figure, show, curdoc
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
import random
from bokeh.models import ContinuousColorMapper
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
from bokeh.palettes import Turbo256
from bokeh.palettes import Category10, Category20, Category20b, Category20c
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
from bokeh.models import LinearColorMapper
from tqdm import tqdm
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def scroll(d):
    SCROLL_PAUSE_TIME = 0.5 
    # Get scroll height
    last_height = d.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = d.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def tqdm_sleep(sec):
    for i in tqdm(range(sec)):
        time.sleep(1)








def generate_datetime_objects(no_of_obj, no_already_avail):
    x_values = []
    current_datetime = datetime.now()

    for i in range(no_already_avail, no_already_avail + no_of_obj):
        start_datetime = current_datetime.replace(hour=i + 1, minute=0, second=0, microsecond=0)
        end_datetime = current_datetime.replace(hour=i + 2, minute=0, second=0, microsecond=0)
        new_datetime = start_datetime + timedelta(seconds=random.randint(0, int((end_datetime - start_datetime).total_seconds())))

        x_values.append(new_datetime)

    return x_values

def generate_random_floats(n_of_obj):
    return [random.uniform(0, 100) for _ in range(n_of_obj)]





def draw_shape(figure, source, x_col_name, y_col_name, shape, size, fill_color, border_color, border_width, alpha, line_dash, line_alpha, line_cap, line_join, line_smoothing):
    if shape=='circle' or shape=='c':
        figure.circle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square' or shape=='s':
        figure.square(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond' or shape=='d':
        figure.diamond(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='triangle' or shape=='t':
        figure.triangle(x=x_col_name, y=y_col_name, source=source, size=size, fill_color=fill_color, line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='cross' or shape=='+':
        figure.cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='X' or shape=='x':
        figure.x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='asterisk' or shape=='*':
        figure.asterisk(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_cross' or shape=='c+':
        figure.circle_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='circle_x' or shape=='cx':
        figure.circle_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='inverted_triangle' or shape=='it':
        figure.inverted_triangle(x=x_col_name, y=y_col_name, source=source,  size=size, fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_cross' or shape=='s+':
        figure.square_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='square_x' or shape=='sx':
        figure.square_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='plus' or shape=='p':
        figure.plus(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_cross' or shape=='d+':
        figure.diamond_cross(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='diamond_x' or shape=='dx':
        figure.diamond_x(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='hex' or shape=='h':
        figure.hex(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='y':
        figure.y(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='-' or shape=='dash':
        figure.dash(x=x_col_name, y=y_col_name, source=source, size=size,  fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha)
    elif shape=='line' or shape=='l':
        # Line cap / line join : "butt", "round", or "square"
        # miter, round or bevel
        figure.line(x=x_col_name, y=y_col_name, source=source, #size=size, 
               # fill_color=fill_color, 
                line_color=border_color, line_width=border_width, alpha=alpha, line_dash=line_dash, line_alpha=alpha,  line_cap=line_cap, line_join=line_join, 
               # line_smoothing=line_smoothing
              )
   
