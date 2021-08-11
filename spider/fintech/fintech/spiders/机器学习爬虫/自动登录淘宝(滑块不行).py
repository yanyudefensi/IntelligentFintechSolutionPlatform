#encoding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import UnexpectedAlertPresentException

import time,unittest, re
driver = webdriver.Chrome()

driver.get("https://login.taobao.com")


driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a').click()

driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[3]/form/div[2]/span').click()

driver.find_element_by_id('TPL_username_1').send_keys('onion66591813')


driver.find_element_by_id("TPL_password_1").click()

driver.find_element_by_id("TPL_password_1").send_keys('13579xyz125678')

driver.find_element_by_id("J_SubmitStatic").click()

driver.find_element_by_id("TPL_password_1").click()

driver.find_element_by_id("TPL_password_1").send_keys('13579xyz125678')

time.sleep(1)

dragger = driver.find_element_by_id('nc_1_n1z')

action = ActionChains(driver)

for index in range(500):

    try:

        action.drag_and_drop_by_offset(dragger, 500, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作

    except UnexpectedAlertPresentException:

        break

    time.sleep(11)  # 等待停顿时间

driver.find_element_by_id('J_SubmitStatic').click()  # 重新摁登录摁扭
# driver = webdriver.Firefox(executable_path="D:\\geckodriver")
#打开百度首页
# driver.get("http://www.taobao.com")
# driver.find_element_by_id('q').clear()  # 清除文本框中内容
# driver.find_element_by_id('q').send_keys("帽子")  # 在搜索框中输入“selenium”
# driver.find_element_by_class_name('search-button').click()  # 点击搜索按钮
#
# time.sleep(5)
#
# driver.find_element_by_id('J_Itemlist_Pic_578418267652').click()  # 点击搜索按钮
#
# driver.find_element_by_id('J_LinkBuy').click()  # 点击搜索按钮
# driver.find_element_by_id('a220o.1000855.0.i3.29bc489d0Kxu7v').click()  # 点击搜索按钮
# driver.find_element_by_id('a220o.1000855.0.i4.29bc489d0Kxu7v').click()  # 点击搜索按钮

# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys("豆瓣")
# driver.find_element_by_id('kw').submit()  # 同样可以通过submit进行提交搜索操作，相当于回车
#
# time.sleep(5)
#
# url_1 = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').get_attribute('href')  # 获取元素属性，这里得到a标签中的href链接
#
# driver.get(url_1)  # 进入刚刚获取的链接地址
# eles = driver.find_elements_by_class_name( 'pl')  # 定位class_name为“pl”的元素列表
#
# for i in eles:
#     print(i.text, i.tag_name)  # 输出所有“pl”文本内容及类型

time.sleep(5)

driver.quit()