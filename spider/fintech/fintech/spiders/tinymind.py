# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class TinymindSpider(scrapy.Spider):
    name = 'tinymind'
    allowed_domains = ['tinymind.cn']
    start_urls = ['http://tinymind.cn/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for i in range(10,820,10):
            data = {'size': 10,'offset': i,'maxId': -1,'sort': 4}
            ajax = s.get('https://www.tinymind.cn/rest/articles?',
                         params=data, headers=headers)
            total = json.loads(ajax.text)
            for j in total['payload']['list']:
                yield Request('https://www.tinymind.cn/articles/'+str(j['id']),self.parse,
                                  meta={'url':'https://www.tinymind.cn/articles/'+str(j['id'])})
            print('tinymind：' + '%.2f' % ((i-1) /820  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find(attrs={'class':'markdown-content content'}).find_all('p')[:-3]
        title = bsObj.find(attrs={'class': 'article-title'}).text
        # print (bs,title)
        #         print(bsObj.find(['title']).text)
        content = ''
        for i in bs:
            if i.text != '' and i.text not in content:
                content = f'{content}{i.text}'

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