#coding:utf-8

from Interpreter import interpret_trade_o32
from Interpreter import file_to_dict
from connect import insert_trade_o32
from connect import pydic_insert_to_mysql
import Data_Dict


#data=excel_to_dict(Data_Dict.relation_dict_o32_trade)
#pydic_insert_to_mysql(data,'test_o32_trade','trade_date')

data=file_to_dict(Data_Dict.relation_dict_sjsjg,filename='SJSJG0815.DBF',file_type="DBF")
pydic_insert_to_mysql(data,'t_sjsjg1','JGJSZH')



