#coding=utf-8
from d4_page.register_page import RegisterPage
from b2_util.get_code import GetCode

class RegisterHandle():
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self,file_name):
        get_code_text = GetCode(self.driver)
        # code = get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(file_name)

    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_username_error_element().text
            elif info == 'password_error':
                text = self.register_p.get_password_error_element().text
            elif info == 'code_text_error':
                text = self.register_p.get_code_error_element().text
            print(text)
        except:
            text == None
        return text

    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_code_element().click()

    #获取注册按钮信息
    def get_register_text(self):
        return self.register_p.get_button_element().text