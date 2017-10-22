# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XingyiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class XYCNDocument(scrapy.Item):
    # xingyiquan.cn
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    body = scrapy.Field()
    from_to = scrapy.Field()
    reference = scrapy.Field()
    des = scrapy.Field()
    created_time = scrapy.Field()
    update_time = scrapy.Field()
