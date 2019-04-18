# -*- coding utf-8 -*-
import scrapy.cmdline


if __name__ == '__main__':
    scrapy.cmdline.execute("scrapy crawl weibo -o data.json".split())
