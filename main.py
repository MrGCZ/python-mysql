#coding:utf-8
from File_To_Py import File_Insert_To_PyDicLi
from Py_To_DB import Mysql_DB
from Filepath import FilePath
import Data_Dict

'''

tgdxw=File_Insert_To_PyDicLi('t_gdxw.xls',Data_Dict.tgdxw_li,relation_li=True)
pydic_tgdxw=tgdxw.file_to_dict()
print pydic_tgdxw
tgdxw_mysql=Mysql_DB(pydic_tgdxw,'t_gdxw')
tgdxw_mysql.pydicli_insert_to_mysql()

tfundinfo=File_Insert_To_PyDicLi('tfundinfo.xls',Data_Dict.tfundinfo_li,relation_li=True)
pydic_tfundinfo=tfundinfo.file_to_dict()
print pydic_tfundinfo
tfundinfo_mysql=Mysql_DB(pydic_tfundinfo,'tfundinfo')
tfundinfo_mysql.pydicli_insert_to_mysql()

'''

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

'''
#sjsjg to DB
sjsjg=File_Insert_To_PyDicLi(file_path_dict['sjsjg'],Data_Dict.relation_dict_sjsjg)
pydic_sjsjg=sjsjg.file_to_dict(file_type="DBF")
sisjg_mysql=Mysql_DB(pydic_sjsjg,'t_sjsjg1')
sisjg_mysql.pydicli_insert_to_mysql()

