import urllib.request

response = urllib.request.urlopen("http://img04.sogoucdn.com/app/a/100520020/8ef51177d730669b76b23c988032729d");
# 上面一句相当于下面两句
# req = urllib.request.Request("http://img04.sogoucdn.com/app/a/100520020/8ef51177d730669b76b23c988032729d")
# response = urllib.request.urlopen(req)

# 一些操作方法
print(response.geturl())
print(response.info())
print(response.getcode())


img = response.read()   #得到的是字节

with open('fengjing.jpg','wb') as f:
    f.write(img)


