from Utils.Utilities import updated_draw_shape_line
from matplotlib.pyplot import get_cmap
import numpy as np


def glyph_renderer(source, figure):
    l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=figure, label='AAMRANET', shape='s')
    return l1, ia1, ib1

    

def glyph_dict_generator(source, figure, company_lst):
    l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=figure, label='AAMRANET', shape='s')
    return l1, ia1, ib1





def get_colors(num_categories: int):
    np.random.seed(42)  # Setting a random seed for consistent results
    colors = []
    while len(colors) < num_categories:
        color = tuple(np.random.uniform(0, 1, 3))
        hex_color = "#{:02x}{:02x}{:02x}".format(*[int(c * 255) for c in color])
        if hex_color not in colors:
            colors.append(hex_color)
    return colors


def generate_gly_dictionary(source, figure, company_list, company_symbol_lst):
    dictionary = {}
    counter = len(company_list)
    color = get_colors(len(company_list))
    for i in range(0, counter):
        key_l = f"l{i}"
        key_ia = f"ia{i}"
        key_ib = f"ib{i}"
        pc = company_list[i] + '_PC'
        label = company_list[i]
        shape = company_symbol_lst[i]
        line_no=i

        sz = company_list[i] + '_Size'

        
        dictionary[key_l], dictionary[key_ia], dictionary[key_ib] = updated_draw_shape_line(x_col_name='x', y_col_name=pc, source=source, figure=figure, label=label, shape=shape, line_no=line_no, color=color[i], size_helper=sz)
    return dictionary
