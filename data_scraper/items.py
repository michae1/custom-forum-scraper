# -*- coding: utf-8 -*-
import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    content = scrapy.Field()
    comment_id = scrapy.Field()

