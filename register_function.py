#coding=utf-8
import sys
import os
sys.path.append(os.getcwd())
print(os.getcwd())
import random
import time
from PIL import Image
from selenium import webdriver
from b2_util.chaojiying import Chaojiying_Client
from c3_base.find_element import FindElement


class RegisterFunction():
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    # 获取driver并且打开url
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        return driver

    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        return find_element.get_element(key)

    # 获取随机数
    def get_random_user(self):
        user_info = ''.join(random.sample('0123456789abcdefgh',8))
        return user_info

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']
        top = code_element.location['y']
        width = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left,top,width,height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        cjy = Chaojiying_Client('liang5564', 'abc1508099549w', 904904)
        image = open(file_name, 'rb').read()
        text = cjy.PostPic(image, 1902)['pic_str']
        print(text)
        time.sleep(2)
        return text

    def main(self):
        file_name = './imooc.png'
        user_name = self.get_random_user()
        user_email = user_name + "@163.com"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name)
        self.send_user_info('password','111111')
        self.send_user_info('code_text','111111')
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功')
        else:
            print(code_error)
            self.driver.save_screenshot('./codeerror.png')

        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(1,4):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()




