#coding=utf-8
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from b2_util.chaojiying import Chaojiying_Client

driver = webdriver.Chrome()
# driver = webdriver.Ie()
# driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains('注册'))
print(EC.title_is('注册'))
print(driver.title)
email_element = driver.find_element_by_id('register_email')

#获取验证码图片的过程
driver.save_screenshot('./imooc.png')
code_element = driver.find_element_by_id('getcode_num')
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open('./imooc.png')
img = im.crop((left,top,right,height))
img.save('./imooc1.png')

# 使用超级鹰代理识别验证码图片
cjy = Chaojiying_Client('liang5564', 'abc1508099549w', 904904)
image = open('imooc1.png', 'rb').read()
result = cjy.PostPic(image, 1902)['pic_str']
print(result)

user_email = ''.join(random.sample('0123456789abcdefg',8)) + "qq.com"
# print(user_email)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'controls')))
print(email_element.get_attribute('placeholder'))
email_element.send_keys(user_email)
print(email_element.get_attribute('value'))
user_name_element_node = driver.find_elements_by_class_name('controls')[1]
user_element = user_name_element_node.find_element_by_class_name('form-control')
user_element.get_attribute('')
user_element.send_keys('qedffsd')
driver.find_element_by_name('password').send_keys('111111')
driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys(result)

time.sleep(5)
driver.close()