from scrapy.cmdline import  execute

import os
import sys

# 设置ArticleSpider工作目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 调用execute函数运行spider
execute(['scrapy','crawl','movie'])