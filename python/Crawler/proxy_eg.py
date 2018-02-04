"""
代理的使用步骤
成功过，但是好像代理IP不稳定。很容易被拒绝。
"""
import  urllib.request
import random

url = 'http://www.whatismyip.com.tw'
iplist = ['120.39.167.121:45984','117.69.96.37:39293','60.167.21.117:40678']
#看课后作业完善

proxy_support = urllib.request.ProxyHandler({'http':'120.39.167.121:45984'})
# 定制，创建一个opener
opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")]
# 安装opener
urllib.request.install_opener(opener)
# 调用opener
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')

print(html)


