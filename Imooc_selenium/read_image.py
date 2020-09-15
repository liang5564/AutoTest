#coding=utf-8
import pytesseract
from PIL import Image
from b2_util.chaojiying import Chaojiying_Client

# 使用pytesseract识别验证码图片
image = Image.open('./简单验证码.png')
text = pytesseract.image_to_string(image)
print(text)

# 使用超级鹰代理识别验证码图片
cjy = Chaojiying_Client('liang5564', 'abc1508099549w', 904904)
image = open('imooc1.png', 'rb').read()
result = cjy.PostPic(image, 1902)['pic_str']
print(result)