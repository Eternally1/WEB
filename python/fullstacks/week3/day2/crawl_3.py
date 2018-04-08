# @author: "QiuJunan"
# @date: 2018/4/3 9:23
# 爬取应急分析测试平台食品领域400多条条数据

import requests
import re
import json
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.converter import PDFPageAggregator

# 修改两部分内容
# 1、爬取下来的TXT文档存储的位置修改
# 2、URL host修改

TXT_FOLDER = r"C:\others\doc\teamAndPersonInfo\GraduationProject\DataSet\emergency_analysis1"
# 这里最后的空出来的，需要填写page，从0-7
URL = "http://www.ceas.org.cn/ajax/ajax.aspx?minute=33&second=52&action=Search&NodeID=4&type=6&keyWord=&page="
host = "http://www.ceas.org.cn"

def get_one_page(url):
    """
    根据url，获取网页返回的数据，然后正则匹配.
    :param url:
    :return:返回一个json字符串，里面有文章所在的url
    """
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers)
        # 设置encoding，避免乱码
        response.encoding = "utf-8"
        if response.status_code == 200:
            return response.text
        print("error code:",response.status_code)
        return None
    except RequestException as e:
        print("error:",e)
        return None


def get_article_list(html):
    """
    获取每篇文章所在的url地址，并返回
    :param html:
    :return:
    """
    # print(html)
    html = json.loads(html)['m2serUl']
    pattern = re.compile("<li><a.*?href='(.*?)'.*?class='m2a1'>(.*?)</a><span class='m2_time1'>(.*?)</span></li>",re.S)
    items = re.findall(pattern,html)
    article_list = []
    for item in items:
        # print(host+item[0])
        # yield{
        #     "url":item[0],
        #     "title":item[1],
        #     "time":item[2]
        # }
        article = {
            "title":item[1],
            "url":host+item[0]
        }
        article_list.append(article)
    return article_list

def get_pdf_url(url):
    """
    通过传入的url获取到pdf文件地址，因为所给的url里面只是部分内容，需要获取pdf的位置
    :param url:
    :return:
    """
    try:
        html = get_one_page(url)
        if html:  # 判断是否找到html内容
            html = BeautifulSoup(html,'lxml')
            a = html.find('a',text="全文浏览")
            pdf_url = host+a.attrs['href']
            return pdf_url
    except Exception as e:
        print("get_pdf_url Error:",e)
        return None # 不存在这篇文章的时候

def readPDF(pdf_url):
    """
    通过pdf的url读取文件，然后获取文件内容并返回
    :param pdf_url:
    :return:
    """
    try:
        fp = urlopen(pdf_url)
    # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)

    # Create a PDF document object that stores the document structure
        doc = PDFDocument()

    # Connect the parser annd document objects.
        parser.set_document(doc)
        doc.set_parser(parser)

    # Supply the password for initialization.
        # (If no password is set, give an empty string.)
        doc.initialize("")

        # 创建PDF资源管理器
        resource = PDFResourceManager()

        # 参数分析器
        laparam = LAParams()

        # 创建一个聚合器
        device = PDFPageAggregator(resource, laparams=laparam)

        # 创建PDF页面解释器
        interpreter = PDFPageInterpreter(resource, device)

    except:
        print("UnicodeError:")
        return
    results = ""
    # 使用文档对象从页面读取内容
    for page in doc.get_pages():
        # 使用页面解释器来读取
        interpreter.process_page(page)

        # 使用聚合器来获取内容
        layout = device.get_result()

        for out in layout:
            if hasattr(out, "get_text"):
                results += out.get_text()
    return results

def _parse(filename):
    fp = urlopen(filename,'rb') #以二进制模式打开
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr =  PDFResourceManager()
        laparams = LAParams()
        device =PDFPageAggregator(rsrcmgr,laparams=laparams)

        interpreter = PDFPageInterpreter(rsrcmgr,device)
        results = ""
        for page in doc.get_pages():  #获取page列表
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                        results += x.get_text()
        return results

def write_to_txt(content,filename):
    """
    将content写入到文件中。
    :param content:
    :return:
    """
    if(content):
        try:
            filename = TXT_FOLDER+'/'+filename+'.txt'
            print(filename)
            with open(filename,'w',encoding="utf-8")as f:
                f.write(content)
        except:
            return
    else:
        print(filename,"写入失败")

if __name__ == '__main__':
    # html = get_one_page(URL+'0')
    # article_list = get_article_list(html)
    # print(article_list)
    # for article in article_list:
    #     pdf_url = get_pdf_url(article["url"])
    #     if pdf_url:
    #         content = readPDF(pdf_url)
    #         # content = _parse(pdf_url)
    #         write_to_txt(content,article['title'])
    for page in range(46):
        html = get_one_page(URL + str(page))
        article_list = get_article_list(html)
        print(article_list)
        for article in article_list:
            pdf_url = get_pdf_url(article["url"])
            if pdf_url:
                content = readPDF(pdf_url)
                # content = _parse(pdf_url)
                write_to_txt(content, article['title'])
