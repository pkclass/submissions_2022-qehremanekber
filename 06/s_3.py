# -*- coding: utf-8 -*-
import scrapy

class Musicians(scrapy.Item):
    name        = scrapy.Field()
    years       = scrapy.Field()
 

class LinksSpider(scrapy.Spider):
    name = 'musicians'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Musicians()

        name_xpath        = '//h1/text()'
        years_xpath       = '//th[text()="Years active"]/following-sibling::*/text()'

        p['name']        = response.xpath(name_xpath).getall()
        p['years']       = response.xpath(years_xpath).getall()
  
        yield p

