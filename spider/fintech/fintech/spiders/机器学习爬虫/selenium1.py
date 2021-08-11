#encoding = utf-8
from selenium import webdriver
import time
#通过executable_path参数指定Firefox驱动文件所在位置
driver = webdriver.Firefox()
# driver = webdriver.Firefox(executable_path="D:\\geckodriver")
#打开百度首页
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').clear()  # 清除文本框中内容
driver.find_element_by_id('kw').send_keys("selenium")  # 在搜索框中输入“selenium”
driver.find_element_by_id('su').click()  # 点击搜索按钮

time.sleep(5)

driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys("豆瓣")
driver.find_element_by_id('kw').submit()  # 同样可以通过submit进行提交搜索操作，相当于回车

time.sleep(5)

url_1 = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').get_attribute('href')  # 获取元素属性，这里得到a标签中的href链接

driver.get(url_1)  # 进入刚刚获取的链接地址
eles = driver.find_elements_by_class_name( 'pl')  # 定位class_name为“pl”的元素列表

for i in eles:
    print(i.text, i.tag_name)  # 输出所有“pl”文本内容及类型

time.sleep(5)
