#coding=utf-8
from b2_util.read_ini import ReadIni

class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0].lower()
        value = data.split('>')[1]
        # print(by,value)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            else:
                return self.driver.find_element_by_css(value)
        except:
            return None