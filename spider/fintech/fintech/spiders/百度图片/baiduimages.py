# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import quote
from fintech.items.picture import CrawlpicturesItem
import json


class ImagesSpider(Spider):
    name = 'baiduimages'
    allowed_domains = ['images.baidu.com']
    start_urls = ['https://images.baidu.com/']

    def start_requests(self):
        # base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='
        keys = ['区块链']
        for key in keys:
            for pn in range(0, 61):
                pn=pn*30
                url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn={pn}&rn=30&gsm={pn2}'.format(
                    word=key, pn=pn,pn2=hex(pn))
                yield Request(url, self.parse ,meta={'keyword':key})

    def parse(self, response):
        images = json.loads(response.body)['data']
        for image in images:
            item = CrawlpicturesItem()
            try:
                item['image_urls'] = image.get('thumbURL')
                item['image_name'] = image.get('fromPageTitleEnc')
                item['keyword']=response.meta['keyword']
                yield item
            except Exception as e:
                print(e)
        pass


