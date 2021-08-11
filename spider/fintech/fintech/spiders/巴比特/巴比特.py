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
total=['','?cat_id=6168','?cat_id=6167','?cat_id=1647','?cat_id=572','?cat_id=242'
       ,'?cat_id=6','?cat_id=2963','?cat_id=1799','?cat_id=898']
pattern = re.compile('/article*')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
for numb,name in enumerate(total):
    with open('D://巴比特'+str(numb)+'.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow('type','url','title','abstract','content','vender')
        driver.get('https://www.8btc.com/news'+name)
        for i in range(4):
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
            time.sleep(2)
        for i in range(10):
            print ('第'+str(numb+1)+'部分:'+'获取url:'+'%.2f'%(i/4000)+'%')
            try:
                driver.find_element_by_xpath('// *[ @ id = "news"] / div[2] / a').click()
            except:
                pass
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
        req=driver.page_source
        htm = etree.HTML(req)
        print (name)
        href=[]
        for i in htm.xpath('//a'):
            if re.match(pattern, i.get('href')):
                if i.get('href') in href:
                    continue
                href.append(i.get('href'))
        print (href)
        try :
            leng=len(href)
            count=0
            # print('try')
            for k in href:
                print('第'+str(numb+1)+'部分:'+'爬取数据'+'%.2f' % (count/leng*100)+'%')
                count+=1
                req = request.Request('https://www.8btc.com' + k, headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all(['h2', 'p'])
                # print(bsObj.find(['title']).text)
                content=''
                for j in bs:
                    content = f'{content}{j.text}'
                content.replace("\n", "").replace("\r", "")
            # print(content)
                csv_writer.writerow((2,i, bsObj.find(['title']).text,content[:40],
                                     content, ''))
        except:
            pass




