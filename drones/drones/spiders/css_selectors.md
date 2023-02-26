# CSS Selectors

next_page = response.css('ul.f-pagination.f-margin-large-top > li > a::attr(href)').get()

products = response.css('div.details-pricing')

name = products.css('a::text').get()

link = products.css('a::attr(href)').get() 

text = products.css('p.price.larger::text').get() 