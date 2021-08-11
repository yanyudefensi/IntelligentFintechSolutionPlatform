# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "amazondemo"
    allowed_domains = ["aws.amazon.com"]
    start_urls = ['https://aws.amazon.com/marketplace/search/results?page=1']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.row.products')
        for thing in things:
            next=thing.css('.row .col-xs-12.col-sm-8 a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
            	meta={'url':next})

        print('正在爬取......')
        next = response.css('.pagination .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.productTitle::text').extract_first()
        item['abstract']=response.css('.sidebar-box p::text').extract_first()
        item['type']='1'
        item['vender']=response.css('.col-xs-8.sold-by-value a::text').extract_first()
        content1=response.css('div.product-description::text').extract()
        content2=response.css('.col-xs-6 p::text').extract()
        item['content']=''.join(content1).join(content2)
        print(item) 
        yield item

