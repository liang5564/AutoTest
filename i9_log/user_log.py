#coding=utf-8
import logging
import time
import os
import datetime

class UserLog():
    def __init__(self):
        #实例化日志对象
        self.logger = logging.getLogger()
        #设置日志等级（DEBUG、INFO）
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s    %(filename)s    %(funcName)s    %(levelno)s    %(levelname)s    %(message)s')

        """控制台输出日志"""
        self.consle = logging.StreamHandler()
        self.consle.setLevel(logging.INFO)
        self.consle.setFormatter(formatter)
        self.logger.addHandler(self.consle)

        '''文件输出日志'''
        #生成文件名（方法一）
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        log_name = log_dir + '/' + log_file
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
            #生成文件名（方法二）
            # log_name = time.strftime('%H%m%d%') + '.log'
            # log_path = './logs/' + log_name
            # file_handle = logging.FileHandler(log_path)

        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug('test564')

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.consle.close()
        self.logger.removeHandler(self.consle)
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    logger = UserLog()
    log = logger.get_log()
    log.debug('test')
    logger.close_handle()