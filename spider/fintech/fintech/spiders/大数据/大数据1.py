import lxml
from lxml import etree
import time
import re,csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
total=['']
       # 'newsflash','news','opinion','bigdata','ai'
       # ,'soft','translation','report']
with open('D://大数据.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(('title','abstract','type','content'))
    # pattern = re.compile('/article*')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    for name in total:
        driver.get('https://www.afenxi.com/'+name)
        for i in range(2):
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
            time.sleep(2)
        for i in range(2000):
            try:
                driver.find_element_by_link_text('点击查看更多').click()
            except:
                pass
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
        req=driver.page_source
        htm = etree.HTML(req)
        print (name)
        href=[]
        for i in htm.xpath('// *[ @ class = "item-title"]/a'):
                # print(i.get('href'))
                href.append(i.get('href'))
        try:
            count=0
            num=len(href)
            for i in href:
                print(('大数据'+name+'%.2f' % (count/num*100))+"%")
                count+=1
                req = request.Request(i, headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all(['p','section'])
        #         print(bsObj.find(['title']).text)
                content=''
                for i in bs:
                    if i.text !='' and i.text not in content:
                        content = f'{content}{i.text}'
                content.replace("\n", "").replace("\r", "")
                # print(content)
                csv_writer.writerow((bsObj.find(['h1']).text,content[:20],'大数据',content))
        except:
            pass