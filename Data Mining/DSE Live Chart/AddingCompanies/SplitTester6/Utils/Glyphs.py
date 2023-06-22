from Utils.Utilities import updated_draw_shape_line
from matplotlib.pyplot import get_cmap
import numpy as np


def glyph_renderer(source, figure):
    # l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='y1', source=source, figure=figure, label='Testy time', shape='c')
    
    
    
    
    l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=figure, label='AAMRANET', shape='s')
    
    # l5, ia5, ib5 = updated_draw_shape_line(x_col_name='x', y_col_name='UNITED_POWER_GENERATION_PC', source=source, figure=figure, label='UNITED_POWER_GENERATION', shape='s')
    
    # l6, ia6, ib6 = updated_draw_shape_line(x_col_name='x', y_col_name='SALVO_CHEMICAL_PC', source=source, figure=figure, label='SALVO_CHEMICAL', shape='s')
    
    # l7, ia7, ib7 = updated_draw_shape_line(x_col_name='x', y_col_name='RAHIMA_FOOD_CORP_PC', source=source, figure=figure, label='RAHIMA_FOOD_CORP', shape='s')

    # l3, ia3, ib3 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRATECH', source=source, figure=figure, label='AAMRATECH', shape='t')

    # l4, ia4, ib4 = updated_draw_shape_line(x_col_name='x', y_col_name='ABBANK', source=source, figure=figure, label='ABBANK', shape='h')


    return l1, ia1, ib1
    # l1, ia1, ib1, 
    # l2, ia2, ib2, 
    # l5, ia5, ib5, l6, ia6, ib6, l7, ia7, ib7, l3, ia3, ib3, l4, ia4, ib4



def glyph_dict_generator(source, figure, company_lst):

    
    l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=figure, label='AAMRANET', shape='s')


    return l1, ia1, ib1



# def generate_gly_dictionary(company_list):
#     dictionary = {}
#     counter = len(company_list)
#     for i in range(0, counter):
#         key_l = f"l{i}"
#         key_ia = f"ia{i}"
#         key_ib = f"ib{i}"
#         pc = company_list[i] + '_PC'
#         label = company_list[i]
#         dictionary[key_l], dictionary[key_ia], dictionary[key_ib] = updated_draw_shape_line(x_col_name='x', y_col_name=pc, source=source, figure=p, label=label, shape='s')
#     return dictionary




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
        dictionary[key_l], dictionary[key_ia], dictionary[key_ib] = updated_draw_shape_line(x_col_name='x', y_col_name=pc, source=source, figure=figure, label=label, shape=shape, company_lst=company_list, line_no=line_no, color=color[i])
    return dictionary
