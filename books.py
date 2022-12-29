import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
       for element in response.xpath('//article[@class="product_pod"]'):
            title = element.xpath('.//h3/a/text()').get()
            price = element.xpath('.//div[@class="product_price"]/p[1]/text()').get()
            stock = element.xpath('.//p[@class="instock availability"]/text()[2]').get().strip()
            yield {'title':title,
                   'price':price,
                   'stock':stock}