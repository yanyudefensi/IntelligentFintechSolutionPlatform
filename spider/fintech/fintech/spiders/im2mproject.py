# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "im2mproject"
    allowed_domains = ["www.im2m.com.cn"]
    start_urls = ['http://www.im2m.com.cn/project/index.htm']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.article-item')
        
        for thing in things:
            next=thing.css('.title a::attr(href)').extract_first()
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
        item['title']=response.css('.title::text').extract_first()
        item['abstract']=response.css('.entry-content p::text').extract_first()
        item['type']='2'
        #content1=response.css('.entry-content p::text').extract()
        #content2=response.css('.entry-content span::text').extract()
        #item['content']=''.join(content1).join(content2)
        item['content']=response.css('.entry-content p::text').extract()
        yield item