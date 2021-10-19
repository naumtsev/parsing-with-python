import platform
import scrapy
from scrapy.selector import Selector
import logging
import json
from scrapy.crawler import CrawlerProcess
from w3lib.html import strip_html5_whitespace as shw
from IPython.core.interactiveshell import InteractiveShell
import warnings
warnings.filterwarnings('ignore')
InteractiveShell.ast_node_interactivity = "all"

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('cian_data.jl', 'w')

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
        'FEED_URI': 'cian_data.json'
    }
    
    def __init__(self, html_list, *args, **kwargs):
        self.start_urls = html_list
        super(QuotesSpider, self).__init__(*args, **kwargs)
    
    def parse(self, response):
        
        for obj in response.xpath("//article[@data-name='CardComponent']"):
            yield {
                'name': Selector(text=obj.get()).xpath("//span[@data-mark='OfferTitle']/span/text()").get(),
                'price': Selector(text=obj.get()).xpath("//span[@data-mark='MainPrice']/span/text()").get(),
                'location': Selector(text=obj.get()).xpath("//a[@data-name='GeoLabel']/text()").getall(),
                }


#тут список файлов html
def parse_habr_scrapy(html_source_list):
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(QuotesSpider, html_source_list)
    process.start()
    #функция ничего не возвращает, а сохраняет файл с данными в папке
