# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

LIMIT_PAGES = False

class Shoe(scrapy.Item):
    first_name = scrapy.Field()
    second_name = scrapy.Field()
    regular_price = scrapy.Field()
    special_price = scrapy.Field()

class ShoeSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['ebouwie.com.pl']

    def __init__(self, pages=500, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if LIMIT_PAGES:
            self.pages = 100
        else:
            self.pages = pages

        try:
            with open("category_links.csv", "rt") as f:
                category_links = [url.strip() for url in f.readlines()][1:]
                print('Category links to be crawled:', category_links)
            self.start_urls = []
            for cl in category_links:
                page_links = [f'{cl}?p={i}' for i in range(1, int(self.pages)+1)]
                self.start_urls += page_links
        except Exception as e:
            self.start_urls = []

    def parse(self, response):
        selection = response.xpath('//li[@class="products-list__item"]').getall()
        print(len(selection), 'shoes found on', response.url)
        for s in selection:
            sel = Selector(text=s)
            first_name = sel.xpath('//span[@class="products-list__name-first"]/text()').get()
            second_name = sel.xpath('//span[@class="products-list__name-second"]/text()').get()

            old_price = sel.xpath('//div[@class="products-list__old-price"]/text()').get()
            special_price = sel.xpath('//div[@class="products-list__special-price"]/text()').get()
            regular_price = sel.xpath('//div[@class="products-list__regular-price"]/text()').get()

            if regular_price is None:
                regular_price = old_price
            
            if special_price is not None:
                special_price = special_price.replace('zł', '').replace(' ', '').replace(',', '.').strip()
            regular_price = regular_price.replace('zł', '').replace(' ', '').replace(',', '.').strip()
            first_name = first_name.strip()
            second_name = second_name.strip()
            
            s = Shoe()
            s['first_name'] = first_name
            s['second_name'] = second_name
            s['regular_price'] = regular_price
            s['special_price'] = special_price
            yield s