import scrapy


# image http://lacor.es/images/productos/53828p.jpg
#                      /images/productos/53828p.jpg
class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['lacor.es']
    start_urls = ['http://lacor.es/eng/catalogo/chef-sets/4335/%s/' % index for index in range(1, 75)]

    def parse(self, response):
        all_books = response.xpath('//article[@class="product_pod"]')  # /html/body/div/div[2]/section

        for book in all_books:
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('.//img[@class="thumbnail"]/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('.//h3/a/@href').extract_first()

            yield {
                'title': title,
                'price': price,
                'Image URL': image_url,
                'Book URL': book_url,
            }
