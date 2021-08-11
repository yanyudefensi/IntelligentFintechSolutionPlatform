#encoding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import UnexpectedAlertPresentException

import time,unittest, re
#通过executable_path参数指定Firefox驱动文件所在位置
driver = webdriver.Chrome()

driver.get("https://wx.qq.com/")

time.sleep(10)
#进入账户密码模式


driver.find_element_by_class_name('web_wechat_tab_friends web_wechat_tab_friends_hl').click()
driver.find_element_by_class_name('nickname ng-binding').click()
driver.find_element_by_class_name('button').click()
driver.find_element_by_id('editArea').send_keys('tomcat')
time.sleep(5)

driver.quit()