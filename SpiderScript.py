# Scrapy without the need of other files from Scrapy Project

import scrapy
from scrapy.crawler import CrawlerProcess


class WhiskySpider(scrapy.Spider):
    name = 'singlemalts'

    def start_requests(self):
        yield scrapy.Request('https://www.thewhiskyexchange.com/c/320/single-malt-irish-whiskey')

    def parse(self, response):
    
        for product in response.css('li.product-grid__item'):
            yield {
                'name': product.css('p.product-card__name::text').get(),
                'meta': product.css('p.product-card__meta::text').get(),
                'price': product.css('p.product-card__price::text').get().strip()
            }


        next_page = response.css('a[title="Show More"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        pass

# CrawlerProcess allows the spider to run without a scrapy project
# Add settings normally used in a Scrapy Project
process =CrawlerProcess(settings= {
    'FEED_URI': 'whisky.json',
    'FEED_FORMAT': 'json'
})

process.crawl(WhiskySpider)
process.start()