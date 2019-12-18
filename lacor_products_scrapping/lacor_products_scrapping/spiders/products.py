import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        allowed_domains = ['http://lacor.es']
        start_urls = ['http://lacor.es/eng/catalogo/chef-sets/4335/%s/' % index for index in range(1, 2)]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    @staticmethod
    def strip(string):
        return string.strip().replace('>\xa0', '')

    def parse(self, response):
        # url_example:http://lacor.es/eng/catalogo/chef-sets/4335/
        # split the url by '/' and take the 4th item from last, chef-sets in this example
        # page_name = response.url.split('/')[-4]
        all_products = response.xpath('/html/body/div/div[2]/section/child::*')  # /html/body/div/div[2]/section
        # image_url = ''
        # categories = [self.strip(response.xpath('/html/body/div/div[2]/section/h2/span/text()').extract_first())]
        for product in all_products:
            title = str(product.xpath('.//p/a/text()').extract_first())
            if title != 'None':
                # image_url = 'http://lacor.es' + product.xpath('.//a/img/@src').extract_first()
                product_url = 'http://lacor.es' + product.xpath('.//p/a/@href').extract_first()

                """my_product = {'title': title, 'categories': categories,
                              'image_url': image_url, 'product_url': product_url}
                yield {
                    'title': title,
                    'categories': categories,
                    'image_url': image_url,
                    'product_url': product_url,
                }"""

                yield scrapy.Request(product_url, callback=self.parse_product)

    def parse_product(self, response):
        self.log('test')
        print('==========================')
        print(f'hello {response}')

tt = 'http://lacor.es/images/productos/53828p.jpg'

print(tt.split('/')[-1])