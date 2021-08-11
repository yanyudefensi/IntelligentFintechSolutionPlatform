# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class LsjSpider(scrapy.Spider):
    name = 'lsj'
    allowed_domains = ['7234.cn']
    start_urls = ['http://7234.cn/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for j in range(1, 3301):
            data = {'page': j,}
            ajax = s.get('https://www.7234.cn/more?', params=data, headers=headers)
            total = json.loads(ajax.text)
            bsObj = BeautifulSoup(total['html'], "lxml")
            bs = bsObj.find_all('a')
            text = re.compile(r".*[0-9]$")
            href = []
            for i in bs:
                if text.match(i.get('href')):
                    href.append(i.get('href'))
            for i in set(href):
                yield Request('https://www.7234.cn' +i,self.parse,
                                  meta={'url':'https://www.7234.cn' +i})
            print('链世界：' + '%.2f' % ((j-1) /3301  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class':'a-content'})
        bs=bs.find_all(['p','b'])
        # print(bsObj.find(['title']).text)
        content = ''
        for j in bs:
            content = f'{content}{j.text}'
        title = bsObj.find(['h1']).text
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