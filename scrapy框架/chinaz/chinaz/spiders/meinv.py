import scrapy
from scrapy.linkextractors import LinkExtractor
from chinaz.items import MeinvItem


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/renwutupian.html"]

    def parse(self, response, **kwargs):
        tupian_list = response.xpath(
            '//div[@class="tupian-list com-img-txt-list"]/div')

        # 链接提取器
        # le = LinkExtractor(restrict_xpaths="xpath,")
        # 提取链接
        # links = le.extract_links(response)

        for tupian in tupian_list:
            detail_url = tupian.xpath('.//a/@href').extract_first()
            # print(response.urljoin(detail_url))

            yield scrapy.Request(
                url=response.urljoin(detail_url),
                method='GET',
                callback=self.parse_detail
            )

        # 下一页
        next_href = response.xpath(
            '//div[@class="new-two-page-box container"]/a[contains(text(), "下一页")]/@href').get()
        # print(next_href)

        if next_href:
            yield scrapy.Request(url=response.urljoin(next_href), method='GET', callback=self.parse)

    def parse_detail(self, resp, **kwargs):
        img_url = resp.xpath(
            '//div[@class="img-box"]/img/@src').extract_first()
        img_name = resp.xpath('.//h1[@class="name"]/text()').extract_first()
        # print(resp.urljoin(img_url))

        item = MeinvItem()
        item['img_name'] = img_name
        item['img_url'] = resp.urljoin(img_url)

        yield item
