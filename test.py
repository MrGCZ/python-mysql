#coding:utf-8

'''
################################test for dbf reader###############################################
from dbfpy import dbf
from Data_Dict import relation_dict_sjsjg
db=dbf.Dbf('SJSJG0815.DBF',readOnly=True)
print db


def dbf_convert_column_li(column_name,db):
    li = []
    for field in db:
        dt=field[column_name]
        li.append(dt)
    return li


dict={}
for k in relation_dict_sjsjg.keys():
    dict[k]=dbf_convert_column_li(relation_dict_sjsjg[k],db)

print dict


from dbfread import DBF
from pandas import DataFrame
from Data_Dict import relation_dict_sjsjg


dbf = DBF('SJSJG0815.DBF')
frame = DataFrame(iter(dbf))

dict={}

for k in relation_dict_sjsjg.keys():
    dict[k]=list(frame[relation_dict_sjsjg[k]])

print dict['JGJSZH']
print len(dict['JGJSZH'])


from dbfpy import dbf
from pandas import  DataFrame
from Data_Dict import jsmx_li
dbf=dbf.Dbf('jsmx02_jsq69.817',readOnly=True)
dict={}

for fn in dbf.fieldNames:
    li=[]
    for i in range(0, len(dbf)):
        li.append(dbf[i][fn].strip())
        dict[fn]=li

del dict['FJSM']




import os
filename=os.listdir(os.getcwd())
for fn in filename:
    if fn.startswith('jsmx'):
        print fn
'''

dict={}
print dict.setdefault('asdas',[])+['a','s']
