from File_To_Py import File_Insert_To_PyDicLi
from Py_To_DB import Mysql_DB
import Data_Dict

'''
sjsjg=File_Insert_To_PyDicLi('SJSJG0815.DBF',Data_Dict.relation_dict_sjsjg)
pydic_sjsjg=sjsjg.file_to_dict(file_type="DBF")
sisjg_mysql=Mysql_DB(pydic_sjsjg,'t_sjsjg1')
sisjg_mysql.pydicli_insert_to_mysql()


'''

jsmx=File_Insert_To_PyDicLi('jsmx',Data_Dict.relation_dict_sjsjg)
pydic_jsmx=jsmx.file_to_dict(file_type="DBF2",del_key='FJSM',multifile_mode=True)
#print pydic_jsmx
jsmx_mysql=Mysql_DB(pydic_jsmx,'t_jsmx')
jsmx_mysql.pydicli_insert_to_mysql()

