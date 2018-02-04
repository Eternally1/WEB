# -*- coding: utf-8 -*-
import scrapy
import re

# 目前没有写出来，因为考虑的比较多，还有数据库的链接方面。慢慢来

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        title =  response.xpath('//*[@id="post-110287"]/div[1]/h1/text()').extract()[0]
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("·",
                                                                                                                   "").strip()
        #点赞数  收藏数  25收藏，还有一个字符串
        praise_num = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        collect_num = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0].strip()

        math_re = re.match("(\d+).*", "25 收藏 ")
        if math_re:
            collect_num = math_re.group(1)

        content = response.xpath('//div[@class="entry"]').extract()[0]









