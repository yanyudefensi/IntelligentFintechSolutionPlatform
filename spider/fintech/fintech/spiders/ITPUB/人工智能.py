import lxml
from lxml import html
import requests
import csv,re
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen
from urllib.parse import quote


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = request.Request('http://www.ailab.cn/', headers=headers)
# htm= urlopen(req)
web={}
web['itpub人工智能']='http://www.itpub.net/?cid=36&page='
for key in web:
    with open('D:/'+key+'.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('title', 'abstract', 'type', 'content'))
        for i in range(1,27):
            try:
                print((key + '%.2f' % ((i-1)/30*100)) + "%")
                req = request.Request(web[key]+str(i), headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all('h4')
                for j in bs:
                    req = request.Request(j.find('a').get('href'), headers=headers)
                    html = urlopen(req)
                    bsObj = BeautifulSoup(html.read(), "html.parser")
                    bs = bsObj.find_all('p')
                    content=''
                    for i in bs:
                        content = f'{content}{i.text}'
                    title=bsObj.find_all('h1')
                    content.replace("\n", "").replace("\r", "")
                    # print(content)
                    csv_writer.writerow((bsObj.find('title').text, content[:20], '人工智能', content))
            except:
                pass
