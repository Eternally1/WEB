# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 可以修改这里的名字
class DomzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 首先通过分析指导要获取的是三部分的内容，分别是title  link  desc
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


