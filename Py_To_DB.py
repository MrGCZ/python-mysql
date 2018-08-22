#coding:utf-8
import xlrd
import xlwt
import datetime
from dbfread import DBF
from pandas import DataFrame
import pymysql
import Data_Dict


class Mysql_DB(object):

    def __init__(self,insert_from_data,insert_to_dbtable):
        self.insert_from_data=insert_from_data
        self.insert_to_dbtable=insert_to_dbtable
        print 'Start inserting to Database... '

    def connect_wxremit_db(self,host='localhost',port=3306,user='root',password='1026',database='test1'):
        return pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               database=database
                               )

    def query(self,sql_str="select * from test_fund"):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        cur.execute(sql_str)
        rows = cur.fetchall()
        cur.close()
        con.close()
        return rows

    def pydicli_insert_to_mysql(self,insert_length_column='', start_row=0):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        #If not defined,choose random key from insert_from_data
        if insert_length_column=='':
            insert_length_column=self.insert_from_data.keys()[0]
        for i in range(start_row, len(self.insert_from_data[insert_length_column])):
            sql_str = str("insert into " + self.insert_to_dbtable + "(" + ",".join(self.insert_from_data.keys()) + ") values(" +
                          "'%s'," * (len(self.insert_from_data.keys()) - 1) + "'%s')")
            re_str = ','.join(["self.insert_from_data['%s'][i]" % k for k in self.insert_from_data.keys()])
            ex_sql_str = sql_str % eval(re_str)
            # print re_str
            # print ex_sql_str
            try:
                cur.execute(ex_sql_str)
            except:
                con.rollback()
                raise
        con.commit()
        cur.close()
        con.close()


if __name__ == '__main__':
    pass
