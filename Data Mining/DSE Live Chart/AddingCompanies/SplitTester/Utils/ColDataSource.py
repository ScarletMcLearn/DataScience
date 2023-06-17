from bokeh.models import ColumnDataSource


# Define the global variables for the streaming data
x_values = []
y_1_values = []
y_2_values = []

AAMRANET_values = []
AAMRATECH_values = []
ABBANK_values = []


source = ColumnDataSource(data=dict(x=x_values, 
                                    
                                    y1=y_1_values, 
                                    y2=y_2_values,  

                                    AAMRANET_LTP=[],
                                    AAMRANET_LH=[],
                                    AAMRANET_LL=[],
                                    AAMRANET_CP=[],
                                    AAMRANET_YCP=[],
                                    AAMRANET_PC=[],
                                    AAMRANET_NoT=[],
                                    AAMRANET_VoT=[],
                                    AAMRANET_Vol=[],


                                    UNITED_POWER_GENERATION_LTP=[],
                                    UNITED_POWER_GENERATION_LH=[],
                                    UNITED_POWER_GENERATION_LL=[],
                                    UNITED_POWER_GENERATION_CP=[],
                                    UNITED_POWER_GENERATION_YCP=[],
                                    UNITED_POWER_GENERATION_PC=[],
                                    UNITED_POWER_GENERATION_NoT=[],
                                    UNITED_POWER_GENERATION_VoT=[],
                                    UNITED_POWER_GENERATION_Vol=[],
                                    
                                    SALVO_CHEMICAL_LTP=[],
                                    SALVO_CHEMICAL_LH=[],
                                    SALVO_CHEMICAL_LL=[],
                                    SALVO_CHEMICAL_CP=[],
                                    SALVO_CHEMICAL_YCP=[],
                                    SALVO_CHEMICAL_PC=[],
                                    SALVO_CHEMICAL_NoT=[],
                                    SALVO_CHEMICAL_VoT=[],
                                    SALVO_CHEMICAL_Vol=[],


                                    RAHIMA_FOOD_CORP_LTP=[],
                                    RAHIMA_FOOD_CORP_LH=[],
                                    RAHIMA_FOOD_CORP_LL=[],
                                    RAHIMA_FOOD_CORP_CP=[],
                                    RAHIMA_FOOD_CORP_YCP=[],
                                    RAHIMA_FOOD_CORP_PC=[],
                                    RAHIMA_FOOD_CORP_NoT=[],
                                    RAHIMA_FOOD_CORP_VoT=[],
                                    RAHIMA_FOOD_CORP_Vol=[],


                                    
                                    AAMRATECH=AAMRATECH_values,
                                    ABBANK=ABBANK_values,
                                   ))

