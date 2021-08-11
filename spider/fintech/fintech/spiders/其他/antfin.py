# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem
import json

class AntfinSpider(scrapy.Spider):
    name = 'antfin'
    key_words = ['大数据', '人工智能', '区块链', '云', '物联网']
    url_format = 'https://tech.antfin.com/_search?query={query}&type=all&size=10&from={start}&_input_charset=utf-8'

    def start_requests(self):
        for word in self.key_words:
            yield scrapy.Request(self.url_format.format(query=word, start=0), callback=self.parse, meta={'query': word})

    def parse(self, response):
        res = json.loads(response.text)
        result_list = res['data']['hits']['hits']
        for index, value in enumerate(result_list):
            item = AntfinItem()
            item['title'] = value['_source']['title']
            item['abstract'] = value['highlight']['content']
            item['type'] = value['_source']['type']
            item['content'] = value['_source']['content']
            yield item

        total = res['data']['hits']['total']
        query = response.meta.get('query')
        if total > 10:
            for i in range(10, total, 10):
                yield scrapy.Request(self.url_format.format(query=query, start=i), callback=self.parse)



