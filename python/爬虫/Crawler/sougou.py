import urllib.request
import re
import os

# 网上找的一个爬取搜狗图片的程序，并不能运行。关键在于反爬取怎么解决。

def getHTMLtext(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    try:
        r = urllib.requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("cannot scrapy the url")
        return ""

        # 解析html文本，筛选出连接


def HTMLparse(link, html):
    try:
        plt = re.findall(r'"thumbUrl":"http://(.*?)"', html)
        for i in range(len(plt)):
            plt[i] = re.sub(r"thumbUrl", "", plt[i])
            plt[i] = re.sub(r":", "", plt[i])
            plt[i] = re.sub(r'"', "", plt[i])
            if plt[i][-1] == 'g' and plt[i][-2] == 'p' and plt[i][-3] == 'j':
                link.append(r"http://" + plt[i])
    except:
        print("error")


def main():
    source = input("请输入要查找的图片：")
    link = []
    try:
        url = "http://pic.sogou.com/pics?pid=sogou-site-3b24156ad560a696&query=美女"

        html = getHTMLtext(url)
        HTMLparse(link, html)
    except:
        print("error2")
    root = "E://爬虫//requests项目//source//"
    headers = {'user-agent': 'Mozilla/5.0'}
    count = 0
    for url in link:
        path = root + url.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url, headers=headers)
                with open(path, 'wb') as file:
                    file.write(r.content)
                    file.close()
                    print("successful safed:" + url.split('/')[-1])
                    count = count + 1
            else:
                print(url.split('/')[-1] + "has already existed")
        except:
            print("cannot safed:" + url.split('/')[-1])
            pass
    print("total count = ", count)


main()