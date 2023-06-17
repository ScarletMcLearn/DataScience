from Utils.Utilities import updated_draw_shape_line


def glyph_renderer(source, figure):
    l1, ia1, ib1 = updated_draw_shape_line(x_col_name='x', y_col_name='y1', source=source, figure=figure, label='Testy time', shape='c')
    
    
    
    
    l2, ia2, ib2 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=figure, label='AAMRANET', shape='s')
    
    l5, ia5, ib5 = updated_draw_shape_line(x_col_name='x', y_col_name='UNITED_POWER_GENERATION_PC', source=source, figure=figure, label='UNITED_POWER_GENERATION', shape='s')
    
    l6, ia6, ib6 = updated_draw_shape_line(x_col_name='x', y_col_name='SALVO_CHEMICAL_PC', source=source, figure=figure, label='SALVO_CHEMICAL', shape='s')
    
    l7, ia7, ib7 = updated_draw_shape_line(x_col_name='x', y_col_name='RAHIMA_FOOD_CORP_PC', source=source, figure=figure, label='RAHIMA_FOOD_CORP', shape='s')

    l3, ia3, ib3 = updated_draw_shape_line(x_col_name='x', y_col_name='AAMRATECH', source=source, figure=figure, label='AAMRATECH', shape='t')

    l4, ia4, ib4 = updated_draw_shape_line(x_col_name='x', y_col_name='ABBANK', source=source, figure=figure, label='ABBANK', shape='h')


    return l1, ia1, ib1, l2, ia2, ib2, l5, ia5, ib5, l6, ia6, ib6, l7, ia7, ib7, l3, ia3, ib3, l4, ia4, ib4
