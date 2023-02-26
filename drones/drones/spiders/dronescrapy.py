import scrapy


class DronescrapySpider(scrapy.Spider):
    name = "dronescrapy"
    allowed_domains = ["www.jessops.com"]
    start_urls = ["https://www.jessops.com/drones"]

    def parse(self, response):
        for product in response.css('div.details-pricing'):
            
            yield {
                'name': product.css('a::text').get(),
                'link': product.css('a::attr(href)').get(),
                'price': product.css('p.price.larger::text').get() 
            }
        

        next_page = response.css('ul.f-pagination.f-margin-large-top > li > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        pass

