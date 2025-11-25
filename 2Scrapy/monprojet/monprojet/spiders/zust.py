import scrapy


class ZustSpider(scrapy.Spider):
    name = "zust"
    allowed_domains = ["zust.edu.cn"]
    start_urls = ["https://zust.edu.cn"]

    def parse(self, response):
        pass
