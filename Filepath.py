#coding:utf-8
import os
from dbfread import DBF
from dbfpy import dbf

class FilePath(object):
    def __init__(self,inputdate='20180817'):
        self.inputdate=inputdate
        self.file_short_name_li=['JSMX','sjsjg','sjsmx','sjsfx','zqbd']   #支持的文件类型
        self.tradepath=os.getcwd()+ "\\Data_File\\" + inputdate+ u"\\交易所数据\\"
        self.result_file_dic={}

    def find_the_file_path(self):
        tradefiledir=os.listdir(self.tradepath)
        for file_short_name in self.file_short_name_li:
            result_file_li = []
            for file in tradefiledir:
                if file.lower().startswith(file_short_name.lower()):
                    result_file_li.append(self.tradepath+file)
            self.result_file_dic[file_short_name.lower()]=result_file_li

class FilePath_Fundinfo(FilePath):
    def __init__(self):
        FilePath.__init__(self)
        self.file_short_name_li=['t_gdxw','tfundinfo']
        self.tradepath=os.getcwd()+ "\\Fundinfo\\"
        self.result_file_dic={}




if __name__ == '__main__':

    fi=FilePath()
    fi.find_the_file_path()
    print fi.result_file_dic
    '''
    fi=FilePath_Fundinfo()
    fi.find_the_file_path()
    print fi.result_file_dic
    '''
