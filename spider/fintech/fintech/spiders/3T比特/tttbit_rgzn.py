# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class TttbitRgznSpider(scrapy.Spider):
    name = 'tttbit_rgzn'
    allowed_domains = ['tttbit.com']
    start_urls = ['http://tttbit.com/']

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        num=1081
        for i in range(1,num+1):
            yield Request('http://tttbit.com/category/rengongzhineng/page/'+str(i),
                          self.parse)
            print('TTTBIT_人工智能：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all('article')
        # print (bs[0].a.get('href'))
        # yield Request(bs[0].a.get('href'),self.parse_2,
        #                       meta={'url':bs[0].a.get('href')})
        for j in bs:
            yield Request(j.a.get('href'),self.parse_2,
                              meta={'url':j.a.get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class': 'entry-content mh-clearfix'})
        content = bs.text
        # for i in bs.find_all('p'):
        #     content = f'{content}{i.text}'
        title = bsObj.find('h1').text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        item['abstract'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item