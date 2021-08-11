# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote

class A360RgznSpider(scrapy.Spider):
    name = '360_rgzn'
    allowed_domains = ['btime.com']
    start_urls = ['http://btime.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for i in range(1, 10000):
            # data = {'num': 20,'page': j,}
            data = {'callback': 'jQuery111308057955846985947_1554126227237',
                    'q': '人工智能',
                    'type': 'all',
                    'channel': 'search',
                    'device_id': '157455e242a6ead88df1a79c351e813a',
                    'refresh': 6,
                    'req_count': i,
                    'refresh_type': 2,
                    'pid': 3}
            ajax = s.get('https://pc.api.btime.com/btimeweb/getSearchData?',
                         params=data, headers=headers)
            total = json.loads(ajax.text[ajax.text.find('{'):-1])
            for j in total['data']:
                yield Request(j['open_url'],self.parse,
                                  meta={'url':j['open_url']})
            print('360人工智能：' + '%.2f' % ((i-1) /10000  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(['p'])
        #         print(bsObj.find(['title']).text)
        content = ''
        for i in bs:
            if i.text != '' and i.text not in content:
                content = f'{content}{i.text}'
        title=bsObj.find(['h1']).text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title
        item['abstract'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item