import scrapy

class QuotesSpider(scrapy.Spider):
    name = "toscrape-css"

    #def start_requests(self):
    #    urls = [
    #        'http://quotes.toscrape.com/page/1/',
    #        'http://quotes.toscrape.com/page/2/',
    #        ]
    #    for url in urls:
    #       yield scrapy.Request(url=url, callback=self.parse)

    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        print('URL: ' + response.url)
        for quote in response.css("div.quote"):
            yield {
                'text' : quote.css("span.text::text").get(),
                'author' : quote.css("small.author::text").get(),
                'tags' : quote.css("div.tags a.tag::text").getall()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)   

# The following line causes the crawler to repeat crawling page 1 for some reason.
#        yield from response.follow_all(css='ul.pager a', callback=self.parse)     