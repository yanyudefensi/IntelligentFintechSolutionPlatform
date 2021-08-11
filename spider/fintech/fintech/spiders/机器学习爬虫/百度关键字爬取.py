#encoding = utf-8
from selenium import webdriver
driver = webdriver.Chrome()
class baidu(object):
    def baidubaike(s, file):
        driver.get("https://baike.baidu.com/item/"+s)
        content = driver.find_elements_by_class_name('para')
        with open('D:/'+file+'.txt', 'w', encoding='utf-8') as txt:
            for i in content:
                cont = i.text
                txt.write(cont)
                print(cont)
            txt.close()