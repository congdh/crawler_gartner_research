# -*- coding: utf-8 -*-
import scrapy
import re
from crawler_gartner_research.items import Document


class GartnerSpider(scrapy.Spider):
    name = 'gartner'
    allowed_domains = ['https://www.gartner.com/doc/3834683']
    start_urls = ['https://www.gartner.com/doc/3834683/']

    def parse(self, response):
        title = response.css('title::text').extract_first()
        published = ''.join(response.css('div.new-date::text').extract()).strip()
        id = int(re.findall('\d+', response.url)[0])
        authors = [x.strip() for x in response.css('h3.analysts a::text').extract()]
        author_urls = [x.strip() for x in response.css('h3.analysts a::attr(href)').extract()]
        document = Document(id=id, title=title, published=published, url=response.url)
        yield document
