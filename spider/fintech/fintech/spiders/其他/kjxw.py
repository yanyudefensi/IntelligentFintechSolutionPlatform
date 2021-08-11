# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class KjxwSpider(scrapy.Spider):
    name = 'kjxw'
    allowed_domains = ['tech.ailab.cn']
    start_urls = ['http://tech.ailab.cn/']
    count = 0

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        for i in range(2, 184):
            yield Request('http://tech.ailab.cn/?page=' + str(i),
                          self.parse)

    def parse(self, response):
        print('人工智能实验室科技新闻：' + '%.2f' % ((self.count) / 184 * 100) + "%")
        self.count += 1
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'list_jc'})
        for j in bs:
            for k in j.find_all('li'):
                yield Request(k.find('a').get('href'), self.parse_2,
                              meta={'url': k.find('a').get('href')})

    def parse_2(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all('p')
        content = ''
        for i in bs:
            content = f'{content}{i.text}'
        title = bsObj.find_all('h1')[0].text
        # if title=='在线客服':
        #     return 1
        content = content.replace("\n", "").replace("\r", "").replace("\t", "").replace('\xa0','')
        print('标题：' + title + '内容：' + content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace('\xa0','')
        item['abstract'] = content[:40]
        item['content'] = content
        item['vender'] = ''
        return item