# 谁放在第一个就显示的是暗色的？？？
# 目前并不能正常运行，有错误
import urllib.parse
import urllib.request
import json

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# head = {}
# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'


data = {}
data['i'] = '你好'
data['from'] = 'zh-CHS'
data['to'] = 'en'
data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt']='1516859352050'
data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] ='FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'
# data['sign']='bbf1e1cd4c3599bd95c2e035a8affaaf'

print(data)

data = urllib.parse.urlencode(data).encode('utf-8')
print(data)
# req = urllib.request.Request(url,data,head)
#另一种方法
req = urllib.request.Request(url,data)
req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

print(json.loads(html))
print(json.loads(html)['errorCode'])
print(req.headers)



