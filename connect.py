import pymysql
from Interpreter import interpret_trade_o32
from Interpreter import file_to_dict
#connect
def connect_wxremit_db():
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='1026',
                           database='test1'
                           )
#search
def query():
    sql_str=("select * from test_fund")
    con = connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

#insert(as an example)
def insert(insertdatas):
    con = connect_wxremit_db()
    cur = con.cursor()
    for data in insertdatas:
        sql_str = ("insert into test_fund(id,name) values('%s','%s')" % (data[0], data[1]))
        try:
            cur.execute(sql_str)
        except:
            con.rollback()
            raise
    con.commit()
    cur.close()
    con.close()

#insert O32 trade data(old method:specifically)
def insert_trade_o32(insertdata):
    con = connect_wxremit_db()
    cur = con.cursor()
    for i in range(1,len(insertdata['trade_date'])):
        sql_str=("insert into test_o32_trade(trade_date,fund_id,fund_name,sec_id,"
                 "sec_name,trade_direct,trade_volume,trade_amount) values('%s','%s','%s','%s',"
                 "'%s','%s','%s','%s')"
                 % (insertdata['trade_date'][i],insertdata['fund_id'][i],insertdata['fund_name'][i],
                    insertdata['sec_id'][i],insertdata['sec_name'][i],insertdata['trade_direct'][i],
                    insertdata['trade_volume'][i],insertdata['trade_amount'][i])
                 )
        try:
            cur.execute(sql_str)
        except:
            con.rollback()
            raise
    con.commit()
    cur.close()
    con.close()

#generally insert python dict to mysql(generally method)
#insert_length_column indicates the length of insert data.

def pydic_insert_to_mysql(insert_data,insert_table,insert_length_column,start_row=0):
    con = connect_wxremit_db()
    cur = con.cursor()
    for i in range(start_row,len(insert_data[insert_length_column])):
        sql_str = str("insert into " + insert_table + "(" + ",".join(insert_data.keys()) + ") values("+
                    "'%s',"*(len(insert_data.keys())-1)+"'%s')")
        re_str=','.join(["insert_data['%s'][i]" % k for k in insert_data.keys()])
        ex_sql_str=sql_str % eval(re_str)
        #print re_str
        #print ex_sql_str
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

