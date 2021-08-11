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
# bsObj = BeautifulSoup(htm.read(), "html.parser")
# bs = bsObj.find_all(attrs={'class': 'nav_ul clear'})
# for j in bs:
#     for k in j.find_all('li'):
#         web[k.find('a').text]=(k.find('a').get('href'))

# {'首页': 'http://www.ailab.cn/', '人工智能动态': 'http://ai.ailab.cn/', '大数据': 'http://bigdata.ailab.cn/', '智能机器人': 'http://robot.ailab.cn/', '无人机': 'http://uav.ailab.cn/', '云计算': 'http://cloud.ailab.cn/', '机器学习': 'http://ml.ailab.cn/', '物联网': 'http://iot.ailab.cn/', '展会动态': 'http://www.ailab.cn/zhanhui.php'}
# print(web)
web['无人机']='http://uav.ailab.cn/'
for key in web:
    with open('D:/'+key+'.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('title', 'abstract', 'type', 'content'))
        req = request.Request(web[key], headers=headers)
        htm = urlopen(req)
        bsObj = BeautifulSoup(htm.read(), "html.parser")
        bs = bsObj.find_all(attrs={'class': 'pg'})
        # num=0
        for j in bs:
            for k in j.find_all('a'):
                num=k.get('title')
            # print(num)
        num = re.sub("\D", "",num)
        for i in range(2,int(num)):
            try:
                print((key + '%.2f' % ((i-1)/int(num)*100)) + "%")
                req = request.Request('http://www.ailab.cn/?page='+str(i), headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all(attrs={'class': 'list_jc'})
                for j in bs:
                    for k in j.find_all('li'):
                        req = request.Request(k.find('a').get('href'), headers=headers)
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
