# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os


class ZendeskSpider(CrawlSpider):
    name = "zendesk"
    allowed_domains = ["fcoin.zendesk.com"]
    start_urls = ["https://fcoin.zendesk.com/hc/zh-cn"]
    rules = (
        Rule(LinkExtractor(allow=("categories",), deny=("en-us",))),
        Rule(LinkExtractor(allow=("articles",)), callback="parse_detail"),
    )

    def parse_detail(self, response):
        title = response.css("title::text").get()
        fname = os.path.join("rawHtml", title + ".html")
        with open(fname, "wb") as f:
            f.write(response.body)
