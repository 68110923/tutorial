import scrapy
from scrapy import cmdline
from lxml import etree
import re

class QuqiubaSpider(scrapy.Spider):
    name = 'quqiuba'
    allowed_domains = ['*']
    start_urls = ['https://www.suncentgroup.com/index.html']

    def parse(self, response, *args, **kwargs):
        for i in range(300):
            yield scrapy.Request(url=f'http://crawler.suncentgroup.com/it/examine_data/', callback=self.parse_sun, dont_filter=True, meta={'download_timeout': 2})
    def parse_sun(self, response, *args, **kwargs):
        yield scrapy.Request(url=f'http://crawler.suncentgroup.com/it/examine_data/', callback=self.parse_sun, dont_filter=True, meta={'download_timeout': 2})



if __name__ == '__main__':
    cmdline.execute('scrapy crawl quqiuba'.split())