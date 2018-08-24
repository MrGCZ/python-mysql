#coding:utf-8
from File_To_Py import File_Insert_To_PyDicLi
from Py_To_DB import Mysql_DB
from Filepath import FilePath
import Data_Dict


trade_file_path=FilePath()
trade_file_path.find_the_file_path()
file_path_dict=trade_file_path.result_file_dic

'''
#jsmx to DB
jsmx=File_Insert_To_PyDicLi(file_path_dict['jsmx'],Data_Dict.jsmx_li,relation_li=True)
pydic_jsmx=jsmx.file_to_dict(file_type="DBF2",del_key='FJSM',multifile_mode=True)
jsmx_mysql=Mysql_DB(pydic_jsmx,'t_jsmx')
jsmx_mysql.pydicli_insert_to_mysql()

#sjsmx to DB
sjsmx=File_Insert_To_PyDicLi(file_path_dict['sjsmx'],Data_Dict.sjsmx_li,relation_li=True)
pydic_sjsmx=sjsmx.file_to_dict(file_type="DBF2",multifile_mode=True)
jsmx_mysql=Mysql_DB(pydic_sjsmx,'t_sjsmx')
jsmx_mysql.pydicli_insert_to_mysql()


#sjsjg to DB
sjsjg=File_Insert_To_PyDicLi(file_path_dict['sjsjg'],Data_Dict.relation_dict_sjsjg)
pydic_sjsjg=sjsjg.file_to_dict(file_type="DBF")
sisjg_mysql=Mysql_DB(pydic_sjsjg,'t_sjsjg1')
sisjg_mysql.pydicli_insert_to_mysql()

#sjsfx to DB
sjsfx=File_Insert_To_PyDicLi(file_path_dict['sjsfx'],Data_Dict.sjsfx_li,relation_li=True)
pydic_sjsfx=sjsfx.file_to_dict(file_type='DBF')
print pydic_sjsfx
sjsfx_mysql=Mysql_DB(pydic_sjsfx,'t_sjsfx')
sjsfx_mysql.pydicli_insert_to_mysql()

'''

#zqbd to DB
sjsfx=File_Insert_To_PyDicLi(file_path_dict['zqbd'],Data_Dict.zqbd_li,relation_li=True)
pydic_zqbd=sjsfx.file_to_dict(file_type='DBF2',multifile_mode=True)
print pydic_zqbd
zqbd_mysql=Mysql_DB(pydic_zqbd,'t_zqbd')
zqbd_mysql.pydicli_insert_to_mysql()



