#coding=utf-8
import configparser

class ReadIni():
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            self.file_name = '../a1_config/LocalElement.ini'
        else:
            self.file_name = file_name
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(self.file_name)

    # 加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == '__main__':
    ri = ReadIni()
    print(ri.get_value('user_email'))
    print(ri.get_value('user_name'))