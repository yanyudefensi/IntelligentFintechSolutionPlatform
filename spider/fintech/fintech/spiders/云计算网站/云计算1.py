import lxml
from lxml import html
import requests
import csv,re
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
web={}
web['新闻']='https://searchcloudcomputing.techtarget.com.cn/news/'
for key in web:
    with open('D:/'+key+'.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('title', 'abstract', 'type', 'content'))
        for i in range(2,407):
            try:
                print((key + '%.2f' % ((i-1)/407*100)) + "%")
                req = request.Request('https://searchcloudcomputing.techtarget.com.cn/interviews/page/3/',
                                      headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                print (bsObj.text)
                bs = bsObj.find_all('h4',attrs={'class': 'newslist'})
                print (bs)
                for j in bs:
                    req = request.Request(j.find('a').get('href'), headers=headers)
                    print(j.find('a').get('href'))
                    html = urlopen(req)
                    bsObj = BeautifulSoup(html.read(), "html.parser")
                    bs = bsObj.find_all(name='div',attrs={'class': 'newslist'})
                    content=''
                    for i in bs:
                        content = f'{content}{i.text}'
                    title=bsObj.find_all('h1')
                    content.replace("\n", "").replace("\r", "")
                    # print(content)
                    csv_writer.writerow((j.find('a').get('title').text, content[:20], key, content))
            except:
                pass
    # csv_file.close()
