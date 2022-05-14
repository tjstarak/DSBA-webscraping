# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

# Page limiter harcoded to True - change to False to allow setting via command line 
LIMIT_PAGES = True

# Shoe class, inheriting from Item, that will be used to collect info about single shoe and will be yielded from the parse method
class Shoe(scrapy.Item):
    first_name = scrapy.Field()
    second_name = scrapy.Field()
    regular_price = scrapy.Field()
    special_price = scrapy.Field()

class ShoeSpider(scrapy.Spider):
# Name of the spider - use in command line call
    name = 'shoes'
    allowed_domains = ['ebouwie.com.pl']

# Default initialization overriden to allow passing additional arguments from command line and to allow setting instance variables
    def __init__(self, pages=500, *args, **kwargs):
# Original initialization from Spider class called
        super().__init__(*args, **kwargs)
# Page limiter overriding the command line argument (or the default value if no cl arg passed)
        if LIMIT_PAGES:
            self.pages = 100
        else:
            self.pages = pages
# Reading the categories to be crawled
        try:
            with open("category_links.csv", "rt") as f:
                category_links = [url.strip() for url in f.readlines()][1:]
                print('Category links to be crawled:', category_links)
            self.start_urls = []
# List of links with numbered pages generated
# Setting this via instance variables is not necessary, but convenient, since list comprehension can be used (using list compr. inside classes is tricky due to variable scope issues).
            for cl in category_links:
                page_links = [f'{cl}?p={i}' for i in range(1, int(self.pages)+1)]
                self.start_urls += page_links
        except Exception as e:
            self.start_urls = []
# No callback function specified for start_urls, so Parse method will be used for all of them
    def parse(self, response):
# Shoe box html extracted
        selection = response.xpath('//li[@class="products-list__item"]').getall()
        print(len(selection), 'shoes found on', response.url)
        for s in selection:
# Shoe box html used to re-create the Selector
            sel = Selector(text=s)
# Individual shoe info extracted from the Selector
            first_name = sel.xpath('//span[@class="products-list__name-first"]/text()').get()
            second_name = sel.xpath('//span[@class="products-list__name-second"]/text()').get()

            old_price = sel.xpath('//div[@class="products-list__old-price"]/text()').get()
            special_price = sel.xpath('//div[@class="products-list__special-price"]/text()').get()
            regular_price = sel.xpath('//div[@class="products-list__regular-price"]/text()').get()
# Old_price exists only if special_price is present but means the same as regular_price. Both are assigned to regular_price to simplify analysis.
            if regular_price is None:
                regular_price = old_price
# Some basic string cleaning, whitespace removed
            if special_price is not None:
                special_price = special_price.replace('zł', '').replace(' ', '').replace(',', '.').strip()
            regular_price = regular_price.replace('zł', '').replace(' ', '').replace(',', '.').strip()
            first_name = first_name.strip()
            second_name = second_name.strip()
# Individual shoe info packages into an instance of a Shoe class and yielded from the parse method
            s = Shoe()
            s['first_name'] = first_name
            s['second_name'] = second_name
            s['regular_price'] = regular_price
            s['special_price'] = special_price
            yield s