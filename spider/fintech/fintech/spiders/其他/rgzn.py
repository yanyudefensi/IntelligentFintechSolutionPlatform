# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class RgznSpider(scrapy.Spider):
    name = 'rgzn'
    allowed_domains = ['ailab.cn']
    start_urls = ['http://ailab.cn/']
    count=0

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        for i in range(2,1113):
            yield Request('http://www.ailab.cn/?page='+str(i),
                          self.parse)

    def parse(self, response):
        print('人工智能实验室人工智能：' + '%.2f' % ((self.count) / 1112 * 100) + "%")
        self.count += 1
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'list_jc'})
        for j in bs:
            for k in j.find_all('li'):
                yield Request(k.find('a').get('href'),self.parse_2,
                              meta={'url':k.find('a').get('href')})

    def parse_2(self,response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all('p')
        content = ''
        for i in bs:
            content = f'{content}{i.text}'
        title = bsObj.find_all('h3')[0].text
        content = content.replace("\n", "").replace("\r", "")
        print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "")
        item['abstract'] = content[:40]
        item['content'] = content
        item['vender'] = ''
        return item