import requests
from requests.exceptions import RequestException
import re
import json
# 多进程
from multiprocessing import Pool
import time


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # re.S  点可以匹配任意字符，包括换行符
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # findall 以列表的形式返回元素，每一项为元组，包含的元素是正则中使用括号的部分
    items = re.findall(pattern, html)
    # 这里的yield不怎么理解。
    for item in items:
        yield {
            'index': item[0],
            'iamge': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4][5:],
            'scotr': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # dumps是将字典格式转化字符串格式
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
        # print(item)

        # print(html)


if __name__ == '__main__':

    # print(time.localtime(time.time()))
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
    # print(time.localtime(time.time()))
