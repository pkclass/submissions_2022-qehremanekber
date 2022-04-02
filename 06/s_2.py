# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("link_lists.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        print(response)
        xpath = '(//ul)[2]/li/a/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] ='https://en.wikipedia.org/' + s.get()
            print(l)
            yield l
