# @author: "QiuJunan"
# @date: 2018/3/13 10:48
"""
这里的是在网页代码中可以直接获取的。
1、user-Agent的设置
2、关于requests编码问题，设置response.encoding = 'utf-8'
3、关于BeautifulSoup的使用。
"""
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import os

TXT_FOLDER = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/public_opinion"

def get_one_page(url):
    """
    根据url，获取网页中的文章内容
    :param url:
    :return:
    """
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers)
        # 设置encoding，避免乱码
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def get_article_link(html):
    """
    根据html文件，获取文章链接
    :param html:
    :return:
    """
    article_lists = []
    if html:
        soup = BeautifulSoup(html,'lxml')
        #按照类名过滤
        li_lists = soup.find_all("li",class_='clearfix')
        for li in li_lists:
            article = {}
            # 使用select方法 注意>两边的空格
            a = li.select('h3 > a')[0]
            # 获取属性的值,获取text内容
            article['url'] = a['href']
            article['title'] = a.text
            article_lists.append(article)
    return article_lists

def _extract_html_(html,article):
    """
    抽取html格式中的内容，返回文章内容
    :param html:
    :return:
    """
    soup = BeautifulSoup(html,'lxml')
    title = soup.find('div',class_='h-title')
    if title:
        title = title.text
    elif soup.find('div',id='title'):
        title = soup.find('div',id='title').text
    else:
        title = article['title']
    content = ""
    detail = soup.find('div',id='p-detail')
    if detail:
        p_list = detail.find_all('p')
        for p in p_list:
            content += "   "+p.text
            content += "\n\n"
    elif soup.find('div',class_='article'):
        p_list = soup.find_all('p')
        for p in p_list:
            content += "   "+p.text
            content += "\n\n"
    else:
        print(article)
    return title+content

def write_to_file(article):
    html = get_one_page(article['url'])
    content = _extract_html_(html,article)
    filename = os.path.join(TXT_FOLDER,article['title'])+'.txt'
    filename = filename.replace('"','_')
    with open(filename, 'w',encoding='utf-8')as f:
        f.write(content)

def main():
    url = "http://www.xinhuanet.com/yuqing/alk.htm"
    html = get_one_page(url)
    article_lists = get_article_link(html)
    count = 0
    for article in article_lists:
        write_to_file(article)
        count +=1
        print("正在写入第"+str(count)+"个文件")

if __name__ == '__main__':
    main()
    # article = {'url': 'http://www.xinhuanet.com/yuqing/2018-03/05/c_129823092.htm', 'title': '海南省政府应对旅客滞留事件获舆论点赞'}
    # write_to_file(article)
