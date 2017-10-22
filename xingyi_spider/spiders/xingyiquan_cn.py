#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from __future__ import unicode_literals
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http.request import Request
from xingyi_spider.items import XYCNDocument


class XYQCNSpider(scrapy.spiders.Spider):
    name = "xyq_cn"
    allowed_domains = ["www.xingyiquan.cn"]
    index_url = 'http://www.xingyiquan.cn/'
    start_urls = [
        "http://www.xingyiquan.cn/",
        'http://www.xingyiquan.cn/Article_Show.asp?ArticleID=883'
    ]

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        doc = BeautifulSoup(response.body_as_unicode()).find('table', class_='border2')
        if doc and doc.find('tr', class_='tdbg_rightall'):
            try:
                item = XYCNDocument()
                item['url'] = response.url
                item['title'] = doc.find('strong').text
                afr = doc.find('tr', class_='tdbg_rightall').text
                afr_text = afr.split('：')
                item['author'] = afr_text[1].split('\xa0')[0]
                item['from_to'] = afr_text[2].split('\xa0')[0]
                item['update_time'] = afr_text[4].split('\xa0')[0]
                item['reference'] = afr_text[-1].split('\r')[0]
                item['des'] = afr
                item['body'] = doc.find('table').text.strip()
                yield item
            except Exception as e:
                print(e)

        all_urls = response.xpath('//a/@href').extract()
        for url in all_urls:
            if not url.startswith('http'):
                url = self.index_url + url
                url.replace('//', '/')
            yield Request(url)

        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码
