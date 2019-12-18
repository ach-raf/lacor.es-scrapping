import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        allowed_domains = ['http://lacor.es']
        urls = [
            'http://lacor.es/eng/catalogo/chef-sets/4335/',
            'http://lacor.es/eng/catalogo/home-cooking-sets/4385/',
            'http://lacor.es/eng/catalogo/pressure-cookers/4491/',
            'http://lacor.es/eng/catalogo/frypans/4510/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url_example:http://lacor.es/eng/catalogo/chef-sets/4335/
        # split the url by '/' and take the 3rd item from last, chef-sets in this example
        page_name = response.url.split('/')[-3]
        filename = '{}.html'.format(page_name)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))

