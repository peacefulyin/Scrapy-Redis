# -*- coding: utf-8 -*-
import scrapy


class XinSpider(scrapy.Spider):
    name = "xin"
    allowed_domains = ["https://www.xin.com"]
    url = 'https://www.xin.com/changsha/i'
    offset = 1
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.css('.list-con ul li'):
            item = {}
            title = each.css('.yx-l2::text').extract_first()
            img = each.css('.aimg img::attr(src)').extract_first()
            price = each.css('.pad p em::text').extract_first()
            item = {
                'title':title,
                'img':img,
                'price':price
            }
            yield item
        if self.offset < 100:
            self.offset += 1
            yield scrapy.Request(url=self.url+str(self.offset), callback=self.parse)
        