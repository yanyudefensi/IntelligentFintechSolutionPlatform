import requests
import json,re
import time
import re,csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote
# # request_headers={
# # 'cache-control': 'no-cache',
# # 'content-type': 'application/json; charset=UTF-8',
# # 'date': 'Mon, 01 Apr 2019 08:02:21 GMT',
# # 'expires': 'Thu, 19 Nov 1981 08:52:00 GMT',
# # 'pragma': 'no-cache',
# # 'status': '200',
# # 'strict-transport-security': 'max-age=15768000; preload',
# # 'x-hit': 'web2'
# # }
s  = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# pattern = re.compile('article*')
# for i in range (1,1351):
#     data = {
#         'num': 20,
#         'page':i,
#     }
#     tom=s.get('https://webapi.8btc.com/bbt_api/news/list?',params = data,headers=headers)
#     total=json.loads(tom.text)
#     # print(type(total))
#     for i in total['data']['list']:
#         # print(i['post_name'])
#         # if re.match(pattern, i['id']):
#         print (i['id'])

# json_string = json_string[json_string.find('{'):-2]

# https://pc.api.btime.com/btimeweb/getSearchData?callback=jQuery111304930191092802534_1554110765034&q=%E7%89%A9%E8%81%94%E7%BD%91&type=all&channel=search&device_id=90c251cdd7e1d35c45f5093d61a26808&refresh=6&req_count=6&refresh_type=2&pid=3&from=&page_refresh_id=&_=1554110765041

# for i in range(1, 10001):
    # data = {'num': 20,'page': j,}
# ajax = s.get('http://www.bcfans.com/jishu/rumen/81274.html', headers=headers)
# total = json.loads(ajax.text)
# count =1
# print (total['html'])
req = request.Request('http://www.bcfans.com/jishu/rumen/106168.html', headers=headers)
html = urlopen(req)
bsObj = BeautifulSoup(html.read(), "html.parser")
content=''
bs = bsObj.find_all(attrs={'class': 'top30'})
for i in bs[2].find_all(['p','em'])[:-1]:
    content = f'{content}{i.text}'
title = bsObj.find_all('h1')[1].text
print (title+'\n'+content)
# content = ''
# # for i in bs.find_all(['p','em']):
# #     content = f'{content}{i.text}'

# content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
