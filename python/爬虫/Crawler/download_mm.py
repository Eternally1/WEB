"""
抓取网络上的图片
试着爬取搜狗图片
"""

import urllib.request
import os
from bs4 import BeautifulSoup


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")

    # 使用代理
    # proxies = []
    # proxy = random.choice(proxies)
    # proxy_support = urllib.request.ProxyHandler({'http':proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)

    # 使用代理出现的问题是获取到的图片不是自己想要的。

    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def find_imgs(url):
    html = url_open(url)
    print(html.decode('gbk'))
    img_addrs = []
    # print(html)
    soup = BeautifulSoup(html,'html.parser')
    img_lists = soup.find_all('img')
    for each in img_lists:
        print(each.get('src'))
        img_addrs.append(each.get('src'))
    return img_addrs


def save_imgs(folder,img_addrs):
    count = 0;
    for each in img_addrs:
        # 通过打印图片的链接可以发现，有些些是获取不到，从而显示的是None，因此直接过滤掉即可
        if each == None:
            continue
        else:
            filename = str(count)+each.split("/")[-1]
            count += 1
            with open(filename, 'wb')as f:
                # 保存图片
                img = url_open(each)
                f.write(img)

def download_mm(folder="mmm"):
    # 通过绝对路径来创建目录
    filepath = os.getcwd()
    # print(filepath)
    folder = filepath+'/'+folder
    # print(folder)
    if os.path.exists(folder) == False:
        os.mkdir(folder)   #创建目录
    os.chdir(folder)   #切换到工作目录

    url = "http://pic.sogou.com/pics?pid=sogou-site-3b24156ad560a696&query="

    # 获取图片地址，返回一个src列表
    img_addrs = find_imgs(url)
    # 将图片保存起来
    # save_imgs(folder,img_addrs)
    print("下载完成")

if __name__ == '__main__':
    download_mm()