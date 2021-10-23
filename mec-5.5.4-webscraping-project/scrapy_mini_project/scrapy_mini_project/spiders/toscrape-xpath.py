import scrapy

class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.selector.xpath('//div[contains(@class, "quote")]'):
            yield {
                'text' : quote.xpath('span[contains(@class, "text")]/text()').extract()[0],
                'author' : quote.xpath('span/small[contains(@class, "author")]/text()').extract()[0],
                'tags' : quote.xpath('div[contains(@class, "tags")]/a[contains(@class, "tag")]/text()').extract()
            }

        yield from response.follow_all(xpath='//nav/ul/li[contains(@class, "next")]/a/@href', callback=self.parse)  
            

