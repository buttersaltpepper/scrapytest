import scrapy
from ..items import ToysItem
from scrapy.loader import ItemLoader

class ToyspiderSpider(scrapy.Spider):
    name = "toyspider"
    allowed_domains = ["magnatiles.com"]
    start_urls = ["https://www.magnatiles.com/products/"]

    def parse(self, response):
        for product in response.css('ul.products.columns-4 li'):
            
            yield {
                'name': product.css('h2.woocommerce-loop-product__title::text').get(),
                'price': product.css('bdi::text').get()
            }


