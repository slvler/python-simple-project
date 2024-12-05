import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_url = [
        'https://www.lipsum.com/'
    ]

    def parse(self, response):
        title = response.css('title').extract()
        yield {'titletext': title}