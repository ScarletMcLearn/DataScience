from bokeh.models import ColumnDataSource





def company_columns_generator(company):
    sr = company + '_Serial'
    ltp = company + '_LTP'
    lh = company + '_LH'
    ll = company + '_LL'
    cp = company + '_CP'
    ycp = company + '_YCP'
    pc = company + '_PC'
    NoT = company + '_NoT'
    vot = company + '_VoT'
    vol = company + '_Vol'
    cn = company + '_Company_Name'
    return {
            sr : [],
            ltp : [],
            lh : [],
            ll : [],
            cp : [],
            ycp : [],
            pc : [],
            NoT : [],
            vot : [],
            vol : [],
            cn : [],
           }



def company_col_gen(company_lst):
    data = {'x':[]}
    data.update(company_columns_generator(company_lst[0]))
    
    for i in range(1, len(company_lst)):
        data.update(company_columns_generator(company_lst[i]))

    source = ColumnDataSource(data=data)

    return source

