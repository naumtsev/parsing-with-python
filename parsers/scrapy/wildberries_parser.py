import platform
import scrapy
from scrapy.selector import Selector
import logging
import json
from scrapy.crawler import CrawlerProcess
import pandas as pd
from w3lib.html import strip_html5_whitespace as shw
from IPython.core.interactiveshell import InteractiveShell
import warnings
warnings.filterwarnings('ignore')
InteractiveShell.ast_node_interactivity = "all"

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('wb1.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
    
    
class QuotesSpider(scrapy.Spider):
    
    start_urls = []
    name = "quotes"
    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1},
        'FEED_FORMAT':'json',
        'FEED_URI': 'wb1.json'
    }
    
    def __init__(self, html_list, *args, **kwargs):
        self.start_urls = html_list
        super(QuotesSpider, self).__init__(*args, **kwargs)
    
    def parse(self, response):
        
        product_card_list = response.xpath("//div[@class='product-card-list']").get()
        product_card = Selector(text=product_card_list).css("div.product-card__wrapper").getall()
        for product in product_card:
            name = Selector(text=product).xpath("//span[@class='goods-name']/text()").get()
            prices = Selector(text=product).xpath("//div[@class='price-commission']").get()
            img_url = Selector(text=product).xpath("//div[@class='product-card__img-wrap']/img/@src").get()
            
            if prices:
                current_price = Selector(text=prices).xpath("//span[@class='price-commission__current-price']/text()").get()
                old_price = shw(Selector(text=prices).xpath("//del[@class='price-commission__old-price']/text()").get())
            else:
                current_price =  Selector(text=product).css("span.lower-price::text").get()
                old_price = '0'

            yield {
                'name' : name,
                'current_price' : current_price,
                'old_price': old_price,
                'img_url': img_url,
              }


#тут список файлов html
def parse_cian_scrapy(html_source_list):
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(QuotesSpider, html_list)
    process.start()
    #функция ничего не возвращает, а сохраняет файл с данными в папке
