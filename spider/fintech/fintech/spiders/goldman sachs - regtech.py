# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "goldmansackregtech"
    allowed_domains = ["www.bankingtech.com"]
    start_urls = ['https://www.bankingtech.com/subject/regtech/']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.search-post')
        
        for thing in things:
            next=thing.css('.search-content.left a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
                 meta={'url':next})
            

        print('正在......')
        next = response.css('.pagination-centered .next.page-numbers::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.single-post-content_title::text').extract_first()
        item['summary']=response.css('.columns.small-12.single-post-content_text-container .first_paragraph::text').extract_first()
        item['type']='(2)'
        item['content']=response.css('.columns.small-12.single-post-content_text-container p::text').extract()
        yield item