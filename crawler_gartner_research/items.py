# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class Document(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    published = scrapy.Field()
    url = scrapy.Field()

    def to_csv(self):
        delim = '|'
        return '{1}{0}{2}{0}{3}{0}{4}'.format(delim, self['id'], self['title'], self['published'], self['url'])

    def to_json(self):
        data = dict(self)
        return json.dumps(data)
