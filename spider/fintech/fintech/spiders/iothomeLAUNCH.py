# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "iothomeLAUNCH"
    allowed_domains = ["iothome.com"]
    start_urls = ['http://iothome.com/launch/']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.listl.list2 ul li')
        
        for thing in things:
            next=thing.css('h3 a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
            					meta={'url':next})
            

        print('正在......')
        next = response.css('.next::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.listltitle h3::text').extract_first()
        item['abstract']=response.css('.say p::text').extract_first()
        item['type']='2'
        item['content']=response.css('.article-content.fontSizeSmall.BSHARE_POP span::text').extract()
        yield item