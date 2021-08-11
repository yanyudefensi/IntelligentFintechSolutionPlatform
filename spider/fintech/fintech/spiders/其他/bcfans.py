# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote

class BcfansSpider(scrapy.Spider):
    name = 'bcfans'
    allowed_domains = ['bcfans.com']
    start_urls = ['http://bcfans.com/']

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        num=276
        for i in range(1,276):
            yield Request('http://www.bcfans.com/jishu/rumen/index_'+str(i)+
                          '.html',self.parse)
            print('BCfans：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'top20'})
        for j in bs:
            try:
                i=j.a.get('href')
                if 'html' in i:
                    yield Request('http://www.bcfans.com' + i, self.parse_2,
                                  meta={'url': 'http://www.bcfans.com' + i})
            except:
                pass

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (bsObj)
        # print (response.text)
        content = ''
        bs = bsObj.find_all(attrs={'class': 'top30'})
        for i in bs[2].find_all(['p', 'em'])[:-1]:
            content = f'{content}{i.text}'
        title = bsObj.find_all('h1')[1].text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('| 区块链爱好者_区块链技术_区块链开发_区块链是什么','')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        item['abstract'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item