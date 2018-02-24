import json
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
import os


def get_page_index(offset,keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": 20,
        "cur_tab": 3,
        "from":"gallery"
    }
    # urlencode将键值对转换成
    url = "https://www.toutiao.com/search_content/?"+urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页失败")
        return None

def parse_page_index(html):
    # 转换成JSON格式
    data = json.loads(html)
    # data.keys()返回data所有的键值
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

# 获取了文章的链接之后，开始获取里面的图片链接
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求详情页出错")
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('gallery:.*?JSON.parse\("(.*?)"\)',re.S)
    result = re.search(images_pattern,html)
    if result:
        # print(type(result.group(1)))
        # print(result.group(1).decode("string_escape"))
        data = json.loads(json.loads('"'+result.group(1)+'"'))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return{
                "title":title,
                "images":images
            }

def create_folder():
    # 创建目录
    filepath = os.getcwd()
    folder = filepath + '/' + "images"
    if os.path.exists(folder) == False:
        os.mkdir(folder)
    os.chdir(folder)

def download_images(images):
    for image in images:
        if image == None:
            continue
        else:
            filename = image.split("/")[-1]+".png"
            with open(filename,'wb') as f:
                print("downloading..."+filename)
                response = requests.get(image)
                f.write(response.content)


def main():
    create_folder()
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        result = parse_page_detail(html)
#       此时图片的链接已经获取了。
#         print(result['images'])
        download_images(result['images'])

if __name__ == '__main__':
    main()


