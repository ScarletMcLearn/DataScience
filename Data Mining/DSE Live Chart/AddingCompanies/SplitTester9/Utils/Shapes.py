from DSEStreamerUtilities.Utilities import draw_shape_line

p, l1, ia1, ib1 = draw_shape_line(x_col_name='x', y_col_name='y1', source=source, figure=p, label='Testy time', shape='c')




p, l2, ia2, ib2 = draw_shape_line(x_col_name='x', y_col_name='AAMRANET_PC', source=source, figure=p, label='AAMRANET', shape='s')

p, l5, ia5, ib5 = draw_shape_line(x_col_name='x', y_col_name='UNITED_POWER_GENERATION_PC', source=source, figure=p, label='UNITED_POWER_GENERATION', shape='s')

p, l6, ia6, ib6 = draw_shape_line(x_col_name='x', y_col_name='SALVO_CHEMICAL_PC', source=source, figure=p, label='SALVO_CHEMICAL', shape='s')

p, l7, ia7, ib7 = draw_shape_line(x_col_name='x', y_col_name='RAHIMA_FOOD_CORP_PC', source=source, figure=p, label='RAHIMA_FOOD_CORP', shape='s')






p, l3, ia3, ib3 = draw_shape_line(x_col_name='x', y_col_name='AAMRATECH', source=source, figure=p, label='AAMRATECH', shape='t')

p, l4, ia4, ib4 = draw_shape_line(x_col_name='x', y_col_name='ABBANK', source=source, figure=p, label='ABBANK', shape='h')
