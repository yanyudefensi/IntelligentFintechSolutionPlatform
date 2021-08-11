import lxml
from lxml import etree
import time
import re,csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from urllib.parse import quote
driver = webdriver.Chrome()
total=['人工智能']
with open('D://360'+total[0]+'.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(('title','abstract','type','content'))
    # pattern = re.compile('/article*')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    for name in total:
        driver.get('https://www.btime.com/search?q='+quote(name, 'utf-8'))
        for i in range(3000):
            print(('360' + name + '%.2f' % (i/3000* 100)) + "%")
            for i in range(5):
                driver.execute_script("var q=document.documentElement.scrollTop=100000")
                time.sleep(1)
            try:
                driver.find_element_by_class_name('icon-more-feed').click()
            except:
                pass
        req=driver.page_source
        htm = etree.HTML(req)
        print (name)
        href=[]
        for i in htm.xpath('// *[ @ class = "feed-lp-rt"]'):
                print(i.get('href'))
                href.append(i.get('href'))
        count=0
        num=len(href)
        for i in href:
            try:
                print(('360'+name+'%.2f' % (count/num*100))+"%")
                count+=1
                req = request.Request(i, headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all(['p'])
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