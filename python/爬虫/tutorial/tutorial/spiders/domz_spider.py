import scrapy

class DomzSpider(scrapy.Spider):
    name = "domz"  #唯一的，确定蜘蛛的名字
    allowed_domains = ['domz.org']    # 要爬取的范围
    start_urls = [            #定义开始从哪爬取
        'http://www.baidu.com',
        'http://www.sina.com'
    ]

    def parse(self,response):
        # 写一个分析的方法
        filename = response.url.split('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)

