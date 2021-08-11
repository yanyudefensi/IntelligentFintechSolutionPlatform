#encoding = utf-8
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/cat")
content = driver.find_elements_by_tag_name(['ul', 'p','b','a'])#这个只能有一个string参数
#'ul' and 'p' and 'b' and 'a'
for i in content:
    print(i.text)