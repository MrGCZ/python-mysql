#coding:utf-8
import xlrd
import xlwt
import datetime
from dbfread import DBF
from pandas import DataFrame
import pymysql
import Data_Dict



class File_Insert_To_PyDicLi(object):

    def __init__(self,filename,file_db_relation):
        self.filename=filename
        self.file_db_relation=file_db_relation

    def __str__(self):
        show_name= 'From file %s in relation with %s' % (self.filename,self.file_db_relation)
        return show_name

#convert file to python dict-list data structure
    def file_to_dict(self,clear_null=0, clear_num_key='trade_date', file_type='Excel'):

        def find_the_column(table, col_name, found_col_num="NA"):
            for i in range(table.ncols):
                if table.cell(0, i).value.encode('utf-8') == col_name:
                    found_col_num = i
                    break
            if found_col_num == "NA":
                raise Exception, "Invalid Column Name!"
            return found_col_num

        def dict_null_clear(dict, key):
            for i in range(len(dict[key])):
                if dict[key][i] == "":
                    for k in dict.keys():
                        del dict[k][i]

        data_dict = {}
        if file_type == 'Excel':
            data = xlrd.open_workbook(self.filename)
            table = data.sheet_by_index(0)
            for key in self.file_db_relation.keys():
                data_dict[key] = table.col_values(find_the_column(table, self.file_db_relation[key]))[1:]
                #[1:] cause first row is always title.
            if clear_null == 1:
                dict_null_clear(data_dict, clear_num_key)
            return data_dict
        elif file_type == "DBF":
            dbf = DBF(self.filename)
            frame = DataFrame(iter(dbf))
            for k in self.file_db_relation.keys():
                data_dict[k] = list(frame[self.file_db_relation[k]])
            return data_dict
        else:
            raise Exception, 'Invalid file type!'



if __name__ == '__main__':
    A=File_Insert_To_PyDicLi('SJSJG0815.DBF',Data_Dict.relation_dict_sjsjg)
    print A


