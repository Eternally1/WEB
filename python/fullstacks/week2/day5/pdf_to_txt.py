# @author: "QiuJunan"
# @date: 2018/3/7 11:58
"""
可以解析pdf称为文本内容，需要改进的就是如何便利目录下的pdf文件，然后分别解析成txt文件。
"""

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.converter import PDFPageAggregator

import os
# file_directory = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT"

def get_fielname(path,file_directory):
    paths = path.split('/')[-1]
    new_file_name = os.path.splitext(paths)[0]+'.txt'
    return os.path.join(file_directory,new_file_name)
    # print(new_file_name)


def parse(path,file_directory):
    # 转换成pdf之后的保存路径。
    filename =get_fielname(path,file_directory)
    print(filename)
    # return
    fp = open(path,'rb') #以二进制模式打开
    # 用文件对象创建一个pdf文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始密码，无的话就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供TXT转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF资源管理器，来管理共享资源
        rsrcmgr =  PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device =PDFPageAggregator(rsrcmgr,laparams=laparams)

        #创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr,device)

        #循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  #获取page列表
            interpreter.process_page(page)
            #接受该页面的LTPage对象
            layout = device.get_result()
            #这里的layout是一个LTPage对象，里面存储着这个page解析出的各种对象，一般包括LTPageBox，LTFigure，LTImage，LYTextBoxHorizontal等等
            #想要获取文本就获得对象的text属性
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open(filename,'a') as f:
                        results = x.get_text()
                        # print(results)
                        f.write(results+'\n')

if __name__== '__main__':
            parse()