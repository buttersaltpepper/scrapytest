import scrapy


class PlantsSpider(scrapy.Spider):
    name = "plants"
    allowed_domains = ["fake-plants.co.uk"]
    start_urls = ["http://fake-plants.co.uk/"]

    def parse(self, response):
        for link in response.css('li.product-category.product a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        yield {
            'category': response.css('span.ast-woo-product-category::text').get().strip(),
            'name': response.css('h2.woocommerce-loop-product__title::text').get()
        }


