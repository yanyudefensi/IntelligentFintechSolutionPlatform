# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class BabitSpider(scrapy.Spider):
    name = 'babit'
    allowed_domains = ['8btc.com']
    start_urls = ['http://8btc.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        total = [6168, 6167,1647,572,242,6,2963,1799,898]
        # for k in total:
        for j in range(1, 5000):
            data = {'num': 20,'page': j,'cat_id':6168}
            tom = s.get('https://webapi.8btc.com/bbt_api/news/list?', params=data, headers=headers)
            total = json.loads(tom.text)
            for i in total['data']['list']:
                yield Request('https://www.8btc.com/article/' + str(i['id']),self.parse,
                                  meta={'url':'https://www.8btc.com/article/' + str(i['id'])})
            print('巴比特：'+str(k) + '%.2f' % ((j-1) /5000  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find_all(['h2', 'p'])
        # print(bsObj.find(['title']).text)
        content = ''
        for j in bs:
            content = f'{content}{j.text}'
        title = bsObj.find(['title']).text
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