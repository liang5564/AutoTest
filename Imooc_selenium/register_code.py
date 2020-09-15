#coding=utf-8
import random
import time
from PIL import Image
from selenium import webdriver
from b2_util.chaojiying import Chaojiying_Client

driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)

# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_random_user():
    user_info = ''.join(random.sample('0123456789abcdefgh',8))
    return user_info

# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

# 解析图片获取验证码
def code_online(file_name):
    cjy = Chaojiying_Client('liang5564', 'abc1508099549w', 904904)
    image = open(file_name, 'rb').read()
    text = cjy.PostPic(image, 1902)['pic_str']
    print(text)
    return text

# 运行主程序
def run_main():
    file_name = './imooc.png'
    user_name = get_random_user()
    user_email = user_name + "@163.com"
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name)
    get_element('register_password').send_keys('111111')
    get_code_image(file_name)
    text = code_online(file_name)
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()

    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    run_main()