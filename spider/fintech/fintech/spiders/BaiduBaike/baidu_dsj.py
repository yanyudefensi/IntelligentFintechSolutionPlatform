# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class BaiduDsjSpider(scrapy.Spider):
    name = 'baidu_dsj'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/' + quote('大数据', 'utf-8')]

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # html_data = htm.xpath('//*[@class="para"]/a')
        bs = bsObj.find_all(attrs={'class': 'para'})
        for j in bs:
            for k in j.find_all('a'):
                if (k.text != '\xa0' and k.text != None):
                    yield Request('https://baike.baidu.com/item/' + quote(k.text, 'utf-8'),
                                  self.parse_2, meta={'url': 'https://baike.baidu.com/item/' + quote(k.text, 'utf-8'),
                                                      'key': k.text})

    def parse_2(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # html_data = htm.xpath('//*[@class="para"]/a')
        bs = bsObj.find_all(attrs={'class': 'para'})
        for j in bs:
            for k in j.find_all('a'):
                if (k.text != '\xa0' and k.text != None):
                    yield Request('https://baike.baidu.com/item/' + quote(k.text, 'utf-8'),
                                  self.parse_3, meta={'url': 'https://baike.baidu.com/item/' + quote(k.text, 'utf-8'),
                                                      'key': k.text})
        yield Request(response.meta['url'],
                      self.parse_3, meta={'url': response.meta['url'], 'key': response.meta['key']})

    def parse_3(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(name='div', attrs={'class': 'para'})
        content = ""
        for i in bs:
            content = f'{content}{i.text}'
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = response.meta['key']
        item['abstract'] = content[:40].replace('\n', '').replace("\r", "").replace(" ", "")
        item['content'] = content.replace('\n', '').replace("\r", "").replace(" ", "").replace('\xa0', '')
        item['vender'] = ''
        return item
