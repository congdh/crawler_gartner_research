# -*- coding: utf-8 -*-
import scrapy
import re
from crawler_gartner_research.items import Document


class GartnerSpider(scrapy.Spider):
    name = 'gartner'
    allowed_domains = ['https://www.gartner.com/doc/3834683']
    start_urls = [
        'https://www.gartner.com/doc/2780019',
        'https://www.gartner.com/doc/3198817',
        'https://www.gartner.com/doc/3210717',
        'https://www.gartner.com/doc/3363117',
        'https://www.gartner.com/doc/3406918',
        'https://www.gartner.com/doc/3579052',
        'https://www.gartner.com/doc/3605417',
        'https://www.gartner.com/doc/3621330',
        'https://www.gartner.com/doc/3624517',
        'https://www.gartner.com/doc/3645329',
        'https://www.gartner.com/doc/3650617',
        'https://www.gartner.com/doc/3655717',
        'https://www.gartner.com/doc/3665917',
        'https://www.gartner.com/doc/3674817',
        'https://www.gartner.com/doc/3698947',
        'https://www.gartner.com/doc/3723447',
        'https://www.gartner.com/doc/3726517',
        'https://www.gartner.com/doc/3732120',
        'https://www.gartner.com/doc/3732517',
        'https://www.gartner.com/doc/3742417',
        'https://www.gartner.com/doc/3755464',
        'https://www.gartner.com/doc/3756063',
        'https://www.gartner.com/doc/3762163',
        'https://www.gartner.com/doc/3762274',
        'https://www.gartner.com/doc/3764963',
        'https://www.gartner.com/doc/3765965',
        'https://www.gartner.com/doc/3772083',
        'https://www.gartner.com/doc/3772135',
        'https://www.gartner.com/doc/3775165',
        'https://www.gartner.com/doc/3778898',
        'https://www.gartner.com/doc/3800064',
        'https://www.gartner.com/doc/3803469',
        'https://www.gartner.com/doc/3803523',
        'https://www.gartner.com/doc/3810881',
        'https://www.gartner.com/doc/3815269',
        'https://www.gartner.com/doc/3815368',
        'https://www.gartner.com/doc/3834578',
        'https://www.gartner.com/doc/3834694',
        'https://www.gartner.com/doc/3836964',
        'https://www.gartner.com/doc/3843965',
        'https://www.gartner.com/doc/3844970',
        'https://www.gartner.com/doc/3860563',
        'https://www.gartner.com/doc/3868568',
        'https://www.gartner.com/doc/3874070',
        'https://www.gartner.com/doc/3875421',
        'https://www.gartner.com/doc/3876789',
        'https://www.gartner.com/doc/3877090',
        'https://www.gartner.com/doc/3878764',
        'https://www.gartner.com/doc/3879572',
        'https://www.gartner.com/doc/3882466',
        'https://www.gartner.com/doc/3883270',
        'https://www.gartner.com/doc/3885667',
        'https://www.gartner.com/doc/3889969',
        'https://www.gartner.com/doc/3890130',
        'https://www.gartner.com/doc/3891111',
        'https://www.gartner.com/doc/3891375',
        'https://www.gartner.com/doc/3891675',
        'https://www.gartner.com/doc/3892089',
        'https://www.gartner.com/doc/3892568',
        'https://www.gartner.com/doc/3892576',
        'https://www.gartner.com/doc/3894108',
        'https://www.gartner.com/doc/3894573',
        'https://www.gartner.com/doc/3894576',
        'https://www.gartner.com/doc/3894769',
        'https://www.gartner.com/doc/3895089',
        'https://www.gartner.com/doc/3895093',
        'https://www.gartner.com/doc/3895567'
    ]

    def parse(self, response):
        title = response.css('title::text').extract_first()
        published = ''.join(response.css('div.new-date::text').extract()).strip()
        id = int(re.findall('\d+', response.url)[0])
        authors = [x.strip() for x in response.css('h3.analysts a::text').extract()]
        author_urls = [x.strip() for x in response.css('h3.analysts a::attr(href)').extract()]
        document = Document(id=id, title=title, published=published, url=response.url)
        yield document
