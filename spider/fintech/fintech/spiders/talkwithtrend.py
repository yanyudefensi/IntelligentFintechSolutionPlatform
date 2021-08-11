# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "talkwithtrend"
    allowed_domains = ["www.talkwithtrend.com"]
    start_urls = ['http://www.talkwithtrend.com/Column?&p=1']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things_noimg = response.css('.fL_item')
        things_img = response.css('.fL_item.haveImg')

        for thing in things_noimg:
            next=thing.css('.fLI_title a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
            					meta={'url':next})

        for thing in things_img:
            next=thing.css('.fLI_title a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
                                meta={'url':next})
            

        print('正在......')
        next = response.css('.next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.articleM_title::text').extract_first()
        item['abstract']=response.css('.articleM_body.editor-html-preview p::text').extract_first()
        item['type']='2'
        item['content']=response.css('.articleM_body.editor-html-preview p::text').extract()
        yield item