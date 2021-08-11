# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "insidebigdataSS"
    allowed_domains = ["insidebigdata.com"]
    start_urls = ['https://insidebigdata.com/category/special-sections/']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.entry-title')
        
        for thing in things:
            next=thing.css('a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
            					meta={'url':next})
            

        print('正在......')
        next = response.css('.pagination-next.alignright a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.entry-title::text').extract_first()
        item['abstract']=response.css('.pf-content p::text').extract_first()
        item['type']='2'
        item['content']=response.css('.pf-content p::text').extract()
        yield item