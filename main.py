#coding:utf-8
from File_To_Py import File_Insert_To_PyDicLi
from Py_To_DB import Mysql_DB
import Data_Dict


'''

sjsjg=File_Insert_To_PyDicLi('SJSJG0817.DBF',Data_Dict.relation_dict_sjsjg)
pydic_sjsjg=sjsjg.file_to_dict(file_type="DBF")
sisjg_mysql=Mysql_DB(pydic_sjsjg,'t_sjsjg1')
sisjg_mysql.pydicli_insert_to_mysql()




sjsmx=File_Insert_To_PyDicLi('SJSMX',Data_Dict.sjsmx_li,relation_li=True)
pydic_sjsmx=sjsmx.file_to_dict(file_type="DBF2",multifile_mode=True)
print pydic_sjsmx
jsmx_mysql=Mysql_DB(pydic_sjsmx,'t_sjsmx')
jsmx_mysql.pydicli_insert_to_mysql()

'''

jsmx=File_Insert_To_PyDicLi('jsmx',Data_Dict.jsmx_li,relation_li=True)
pydic_jsmx=jsmx.file_to_dict(file_type="DBF2",del_key='FJSM',multifile_mode=True)
#print pydic_jsmx
jsmx_mysql=Mysql_DB(pydic_jsmx,'t_jsmx')
jsmx_mysql.pydicli_insert_to_mysql()

