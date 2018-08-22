#coding:utf-8
from File_To_Py import File_Insert_To_PyDicLi
from Py_To_DB import Mysql_DB
from Filepath import FilePath_Fundinfo
import Data_Dict

fundinfo_file=FilePath_Fundinfo()
fundinfo_file.find_the_file_path()
fundinfo_file_dic=fundinfo_file.result_file_dic
print fundinfo_file_dic

tgdxw=File_Insert_To_PyDicLi(fundinfo_file_dic['t_gdxw'],Data_Dict.tgdxw_li,relation_li=True)
pydic_tgdxw=tgdxw.file_to_dict()
tgdxw_mysql=Mysql_DB(pydic_tgdxw,'t_gdxw')
tgdxw_mysql.pydicli_insert_to_mysql()

tfundinfo=File_Insert_To_PyDicLi(fundinfo_file_dic['tfundinfo'],Data_Dict.tfundinfo_li,relation_li=True)
pydic_tfundinfo=tfundinfo.file_to_dict()
tfundinfo_mysql=Mysql_DB(pydic_tfundinfo,'tfundinfo')
tfundinfo_mysql.pydicli_insert_to_mysql()

