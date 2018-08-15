#coding:utf-8
import xlrd
import xlwt
import datetime

def find_the_column(table, col_name,found_col_num="NA"):
    for i in range(table.ncols):
        if table.cell(0, i).value.encode('utf-8') == col_name:
            found_col_num = i
            break
    if found_col_num=="NA":
        raise Exception,"Invalid Column Name!"
    return found_col_num

def dict_null_clear(dict,key):
    for i in range(len(dict[key])):
        if dict[key][i]=="":
            for k in dict.keys():
                del dict[k][i]

#old method, specifically
def interpret_trade_o32(filename=u'综合信息查询_成交回报810.xls',data_dict = {},clear_null=1,clear_num_key='trade_date'):

    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    trade_date = table.col_values(find_the_column(table, '发生日期'))
    fund_id = table.col_values(find_the_column(table, '账户编号'))
    fund_name = table.col_values(find_the_column(table, '账户名称'))
    sec_id = table.col_values(find_the_column(table, '证券代码'))
    sec_name = table.col_values(find_the_column(table, '证券名称'))
    trade_direct = table.col_values(find_the_column(table, '委托方向'))
    trade_volume = table.col_values(find_the_column(table, '成交数量'))
    trade_amount = table.col_values(find_the_column(table, '发生金额(全价)'))

    for i in range(len(trade_date)):
        data_dict['trade_date'] = trade_date
        data_dict['fund_id'] = fund_id
        data_dict['fund_name'] = fund_name
        data_dict['sec_id'] = sec_id
        data_dict['sec_name'] = sec_name
        data_dict['trade_direct'] = trade_direct
        data_dict['trade_volume'] = trade_volume
        data_dict['trade_amount'] = trade_amount

    if clear_null==1:
        dict_null_clear(data_dict, clear_num_key)

    return data_dict


#excel to mysql 字段匹配关系

relation_dict={'trade_date':'发生日期','fund_id':'账户编号','fund_name':'账户名称','sec_id':'证券代码','sec_name':'证券名称',
               'trade_direct':'委托方向','trade_volume':'成交数量','trade_amount':'发生金额(全价)'}

###################################################
#generally convert excel data to python dict(new method,generally)

def excel_to_dict(relation_dict,filename=u'综合信息查询_成交回报815.xls',data_dict = {},clear_null=1,clear_num_key='trade_date'):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    for key in relation_dict.keys():
        data_dict[key]=table.col_values(find_the_column(table, relation_dict[key]))
    if clear_null==1:
        dict_null_clear(data_dict, clear_num_key)
    return data_dict


if __name__ == '__main__':
    data=excel_to_dict(relation_dict)
    print data



