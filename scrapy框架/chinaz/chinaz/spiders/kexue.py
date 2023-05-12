import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chinaz.items import ChinazItem


class KexueSpider(CrawlSpider):
    name = "kexue"
    allowed_domains = ["chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/taikongkexuetupian.html"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="tupian-list com-img-txt-list"]/div')),
             callback="parse_item", follow=False),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="new-two-page-box container"]/a')),
             callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        img_url = response.xpath(
            '//div[@class="img-box"]/img/@src').get()

        img_name = response.xpath(
            './/h1[@class="name"]/text()').get()

        # 实例化item对象
        item = ChinazItem()
        item['img_name'] = img_name
        item['img_url'] = response.urljoin(img_url)

        yield item
