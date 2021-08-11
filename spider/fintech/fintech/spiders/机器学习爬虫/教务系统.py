#encoding = utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import UnexpectedAlertPresentException

import time,unittest, re
#通过executable_path参数指定Firefox驱动文件所在位置
driver = webdriver.Chrome()

driver.get("http://xsjw2018.scuteo.com/jwglxt/xtgl/login_slogin.html;jsessionid=934F8431B3D6420BC8D4831159EDA888")

#进入账户密码模式
pwd=driver.find_element_by_id('yhm')
pwd.clear()
pwd.send_keys('201630719526')

pwd=driver.find_element_by_id('mm')
pwd.clear()
pwd.send_keys('13579xyz125678!')

driver.find_element_by_id('dl').click()
sel = driver.find_element_by_name('学生课表查询')
print("success")
time.sleep(5)

# driver.quit()