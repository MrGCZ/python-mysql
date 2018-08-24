#coding:utf-8
import xlrd
import xlwt
import datetime
from dbfread import DBF
from pandas import DataFrame
import pymysql
import Data_Dict
from dbfpy import dbf
import os




class File_Insert_To_PyDicLi(object):

    def __init__(self,filelist,file_db_relation,relation_li=False):
        self.filelist=filelist
        if relation_li==False:
            self.file_db_relation = file_db_relation
        else:
            self.file_db_relation=self.litodic(file_db_relation)

    def __str__(self):
        show_name= 'From file %s in relation with %s' % (self.filelist,self.file_db_relation)
        return show_name

    @staticmethod
    def litodic(list):
        dict = {}
        for li in list:
            dict[li] = li
        return dict

#convert file to python dict-list data structure
    def file_to_dict(self,clear_null=0, clear_num_key='trade_date', file_type='Excel',del_key='',multifile_mode=False):

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

        if file_type == 'Excel' and multifile_mode==False:
            filename=self.filelist[0]
            print "Reading the file %s,waiting..." % filename
            data = xlrd.open_workbook(filename)
            table = data.sheet_by_index(0)
            for key in self.file_db_relation.keys():
                data_dict[key] = table.col_values(find_the_column(table, self.file_db_relation[key]))[1:]
                #[1:] cause first row is always title.
            if clear_null == 1:
                dict_null_clear(data_dict, clear_num_key)
        elif file_type == "DBF" and multifile_mode==False:
            filename=self.filelist[0]
            print "Reading the file %s,waiting..." % filename
            dbffile = DBF(filename)
            frame = DataFrame(iter(dbffile))
            for k in self.file_db_relation.keys():
                data_dict[k] = list(frame[self.file_db_relation[k]])
        elif file_type=="DBF2" and multifile_mode==True:  #It's available when multifile_mode=True
            for file in self.filelist:
                print "Reading the file %s,waiting..." %file
                dbffile = dbf.Dbf(file, readOnly=True)
                for fn in self.file_db_relation.keys():
                    li = []
                    for i in range(0, len(dbffile)):
                        li.append(str(dbffile[i][self.file_db_relation[fn]]).strip())
                    data_dict[fn]=data_dict.setdefault(fn,[])+li
        else:
            raise Exception, 'Invalid file type!'
        if not del_key=='':
            #print data_dict
            del data_dict[del_key]
        return data_dict



if __name__ == '__main__':
    A=File_Insert_To_PyDicLi('jsmx02_jsq69.817',Data_Dict.jsmx_li,relation_li=True)
    print A
    print A.file_to_dict(file_type="DBF2")


