# -*- coding: utf-8 -*-
import scrapy


class CiieSpider(scrapy.Spider):
    name = 'ciie'
    allowed_domains = ['https://www.ciie.org']
    # start_urls = ['http://https://www.ciie.org/']

    def parse(self, response):
        pass
