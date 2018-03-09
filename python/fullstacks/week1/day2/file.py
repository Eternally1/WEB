# @author: "QiuJunan"
# @date: 2018/2/25 10:55

f = open("file",'r',encoding="utf-8")
# read后面读取的是5个字符。
data = f.read(10)
f.close()
print(data)


import sys,time
# 等0.2*30秒才会打印出所有的字符
for i in range(30):
    # sys.stdout.write("*")
    # # 添加缓冲区刷新可以让实时打印出来，在进度条的时候可能会用上
    # sys.stdout.flush()
    print("*",end=" ",flush=True)
    time.sleep(0.2)