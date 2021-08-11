# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class Yjs2Spider(scrapy.Spider):
    name = 'yjs2'
    allowed_domains = ['searchcloudcomputing.techtarget.com.cn']
    start_urls = ['http://searchcloudcomputing.techtarget.com.cn/']

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        num=407
        for i in range(2,num):
            yield Request('https://searchcloudcomputing.techtarget.com.cn/analyses/page/'+str(i),
                          self.parse)
            print('云计算分析：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'newslist'})
        for j in bs:
            for k in j.find_all('h4'):
                yield Request(k.find('a').get('href'),self.parse_2,
                              meta={'url':k.find('a').get('href')})

    def parse_2(self,response):
        bsObj = BeautifulSoup(response.text, "lxml")
        ma = bsObj.find(attrs={'class': 'maintext'})
        bs = ma.find_all('p')
        content = ''
        for i in bs[:-7]:
            content = f'{content}{i.text}'
        title = bsObj.find('h1').text
        content = content.replace("\n", "").replace("\r", "")
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "")
        item['abstract'] = content[:40]
        item['content'] = content
        item['vender'] = ''
        return item