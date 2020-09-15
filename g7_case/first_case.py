#coding=utf-8
import sys
import os
import time
sys.path.append(r'C:\Users\Administrator\Desktop\AutoTest')
import unittest
from HTMLTestRunner import HTMLTestRunner
from f6_business.register_business import RegisterBusiness
from selenium import webdriver
from i9_log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = UserLog()
        self.logger = self.log.get_log()
        self.file_name = '../image/code.png'

    @classmethod
    def tearDownClass(self):
        self.log.close_handle

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info('this is chrome')
        self.register_b = RegisterBusiness(self.driver)
        print('这是case的前置条件')

    def tearDown(self):
        time.sleep(5)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName + '.png'
                self.driver.save_screenshot('../report/' + case_name)
        self.driver.close()
        print('这是case的后置条件')

    def test_login01_email_error(self):
        email_error = self.register_b.login_email_error('345@qq.com','user111','111111',self.file_name)
        self.assertFalse(email_error,'case执行了')
        # if email_error == True:
        #     print('注册成功了，此条case失败')

    def test_login02_username_error(self):
        username_error = self.register_b.login_name_error('111@qq.com','ss','111111',self.file_name)
        self.assertFalse(username_error)

    def test_login03_password_error(self):
        password_error = self.register_b.login_password_error('111@qq.com','user02','11',self.file_name)
        self.assertFalse(password_error)

    def test_login04_code_error(self):
        code_error = self.register_b.login_code_error('111@qq.com','user03','111111',self.file_name)
        self.assertFalse(code_error)

    def test_login05_success(self):
        success = self.register_b.user_base('111@qq.com','ss','111111',self.file_name)
        self.assertFalse(success)
'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    # unittest.main()
    file_path = r'C:\Users\Administrator\Desktop\AutoTest\report\first_case.html'
    fp = open(file_path,'wb')
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login01_email_error'))
    suite.addTest(FirstCase('test_login02_username_error'))
    runner = HTMLTestRunner(
        stream=fp,
        title='This is my first report!',
        description='这个是我们第一次测试报告',
        verbosity=2
    )
    runner.run(suite)
