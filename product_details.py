import scrapy
from search_url import *
 

class SearchProduct(scrapy.Spider):
    product=raw_input('Enter the name of product you want to search:')
    name = "keyword"
    start_urls = []
    start_urls.append(search_url(product))

    def parse(self, response):
        for keyword in response.css('div.keyword'):
            yield {
                'name': keyword.css('span.text::text').extract_first(),
                'price': keyword.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


