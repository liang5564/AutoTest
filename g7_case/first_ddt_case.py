#coding=utf-8
import ddt
import unittest
import sys
import os
import time
sys.path.append(r'C:\Users\Administrator\Desktop\AutoTest')
from HTMLTestRunner import HTMLTestRunner
from f6_business.register_business import RegisterBusiness
from selenium import webdriver
from b2_util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = '../image/code.png'


    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
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

    """
    # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    @ddt.data(
        ('123', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'),
        ('@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'),
        ('12569793@qq.com', 'Mushishi01', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址')
    )
    @ddt.unpack
    def test_register01_case(self,email,username,password,code,assertCode,assertText):
        print(email)
        email_error = self.register_b.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,'测试失败')
    """

    #以读取excel的方式实现参数化
    @ddt.data(*data)
    def test_register02_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.register_b.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,'测试失败')

if __name__ == '__main__':
    # unittest.main()
    report_time = time.strftime('%Y%m%d%H%M%S')
    report_path = '../report/' + report_time + '.html'
    with open(report_path,'wb') as fp:
        suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='自动化测试报告',
            description='运行环境：Windows7，Chrome浏览器'
        )
        runner.run(suite)
