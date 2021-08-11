# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote

class A360DsjSpider(scrapy.Spider):
    name = '360_dsj'
    allowed_domains = ['btime.com']
    start_urls = ['http://btime.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for i in range(1, 10001):
            # data = {'num': 20,'page': j,}
            # time_local = time.localtime(comment_timestamp)
            # comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            data={'callback': 'jQuery111308729569126802736_1554125601506',
            'q': '大数据',
            'type': 'all',
            'channel': 'search',
            'device_id': '00f0b6ecf6f16d05c318b2a042065e43',
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
            print('360大数据：' + '%.2f' % ((i-1) /10000  * 100) + "%")

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