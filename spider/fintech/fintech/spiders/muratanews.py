# -*- coding: utf-8 -*-

import scrapy


from ..items.antfin import AntfinItem



class QuotesSpider(scrapy.Spider):
    name = "muratanews"
    allowed_domains = ["murata.eetrend.com"]
    start_urls = ['http://murata.eetrend.com/news']
    headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    
    def parse(self, response):
        things = response.css('.views-row')
        for thing in things:
            next=thing.css('.row-list-content a::attr(href)').extract_first()
            sub_url = response.urljoin(next)
            yield scrapy.Request(url=sub_url,callback=self.parse_url,
                meta={'url':next})

        print('正在爬取......')
        next = response.css('.pager__item a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse_url(self, response):
        item = AntfinItem()
        item['url']=response.meta['url']
        item['title']=response.css('.page-header span::text').extract_first()
        item['abstract']=response.css('.field.field--name-body.field--type-text-with-summary.field--label-hidden.field--item p::text').extract_first()
        item['type']='2'
        item['content']=response.css('.field.field--name-body.field--type-text-with-summary.field--label-hidden.field--item p::text').extract()
        yield item

