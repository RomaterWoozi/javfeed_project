# -*- coding: utf-8 -*-
import scrapy


class JavfeedSpider(scrapy.Spider):
    name = 'javfeed'
    allowed_domains = ['javfeed.com']
    start_urls = ['http://javfeed.com/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers={
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'},
                             callback=self.parse)

    def parse(self, response):
        for sub_tab in  response.xpath("//ul[@class='nav']/li"):
            tab_name=sub_tab.xpath("./a/@href")
            tab_link=sub_tab.xpath("./a/text()")
            yield {'tab_name':tab_name,'tab_link':tab_link}

        pass
