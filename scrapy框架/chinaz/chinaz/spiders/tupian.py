import scrapy
from chinaz.items import ChinazItem


class TupianSpider(scrapy.Spider):
    name = "tupian"
    allowed_domains = ["chinaz.com"]
    # 爬取站长之家图片
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        # 拿到页面源代码
        # print(response.text)

        tupian_list = response.xpath(
            '//div[@class="tupian-list com-img-txt-list"]/div')

        for tupian in tupian_list:
            # 实例化item对象
            item = ChinazItem()
            item['img_name'] = tupian.xpath('.//img/@alt').get()
            item['img_url'] = tupian.xpath('.//img/@data-original').get()
            # print(item)
            # 需要用yield将数据传递给管道
            yield item
