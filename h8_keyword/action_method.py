#coding=utf-8
import time

from selenium import webdriver
from c3_base.find_element import FindElement

class ActionMethod():
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Ie()

    #浏览器最大化
    def browser_maximize(self):
        self.driver.maximize_window()

    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #获取title
    def get_title(self):
        return self.driver.title

    #定位元素
    def get_element(self,key):
        return FindElement(self.driver).get_element(key)

    #输入元素
    def element_send_keys(self,value,key):
        self.get_element(key).send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_element(key).click()

    #等待
    def sleep_time(self):
        time.sleep(3)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()
