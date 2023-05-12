# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinazItem(scrapy.Item):
    # define the fields for your item here like:
    img_name = scrapy.Field()
    img_url = scrapy.Field()


class MeinvItem(scrapy.Item):
    img_name = scrapy.Field()
    img_url = scrapy.Field()
