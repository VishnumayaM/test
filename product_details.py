import scrapy
from search_url import *
 

class SearchProduct(scrapy.Spider):
    keyword=raw_input('Enter the name of product you want to search:')
    name = "products"
    start_urls = []
    start_urls.append(search_url(keyword))

    def parse(self, response):
        for product in response.css("ul.s-result-list"):
            yield {
                'product': product.css('a.a-link-normal::attr("title")').extract(),
                'price': product.css('span.a-color-price::text').extract(),
                #'price': product.xpath('span/small/text()').extract_first(),
				#'image':product.css('span.a-dynamic-image::img').extract(),
            }
        next_page = response.xpath('//*[@id="pagn"]/span[7]').css('a.pagnNext::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)


