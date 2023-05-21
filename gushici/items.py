# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GushiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题 m.title_pad b::text()
    title = scrapy.Field()

    # 朝代 .mainDiv .content  span::text()
    time  = scrapy.Field()

    # 作者 .mainDiv .content span::text()="作者:" sibling span>a::text()
    author = scrapy.Field()

    # .mainDiv .content .scmk a::text()
    themes = scrapy.Field()

    # .mainDiv .content p 原文： p
    content = scrapy.Field()

    


