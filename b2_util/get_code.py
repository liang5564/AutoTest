#coding=utf-8
import time
from PIL import Image
from selenium import webdriver

from b2_util.chaojiying import Chaojiying_Client

class GetCode():
    def __init__(self,driver):
        self.driver = driver

    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
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

if __name__ == '__main__':
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('http://www.5itest.cn/register')
    gc = GetCode(driver)
    file_name = '../image/imooc.png'
    gc.get_code_image(file_name)
    result = gc.code_online(file_name)
    print(result)