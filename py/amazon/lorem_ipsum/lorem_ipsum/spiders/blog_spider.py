import scrapy

class BlogSpider(scrapy.Spider):
    name = "blog_spider"
    start_urls = ['https://example-blog.com']

    def parse(self, response):
        for post in response.css('div.post'):
            yield {
                'title': post.css('h2.title::text').get(),
                'date': post.css('span.date::text').get(),
            }
        # Bir sonraki sayfaya git
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
