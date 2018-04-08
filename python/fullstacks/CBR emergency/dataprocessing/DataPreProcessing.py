# @author: "QiuJunan"
# @date: 2018/3/10 11:42
# 将数据预处理相关的需要的方法封装在一起。

import os
import re
import shutil
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.converter import PDFPageAggregator

# 33个事件类别
# event_catagory = {
#     "自然灾害类":["水旱灾害","气象灾害","地震灾害","地质灾害","海洋灾害","生物灾害","森林草原灾害","宇宙灾害"],
#     "事故灾难类":["战争和暴力","工矿商贸安全事故","交通运输安全事故","城市生命线事故","通讯安全事故","环境污染和生态破坏",
#              "严重火灾","中毒事件","急性化学事故","放射事故","医药事故","探险遇难","旅游事故"],
#     "公共卫生事件":["传染病疫情","群体性不明原因疾病","食品安全和职业危害","动物疫情","其他严重影响公众健康和生命安全的事件"],
#     "社会安全事件":["恐怖袭击事件","重大刑事事件","经济安全事件","涉外突发事件","规模较大的群体性事件","民族宗教","反政府和反社会主义骚乱暴动"]}

# 将filename【pdf】文件中的字提取出来
# 返回的是这个pdf文档中的字。
def _parse(filename):
    fp = open(filename,'rb') #以二进制模式打开
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

# 获取file_dir目录下面的文件名，然后保存在filename文件中
def _save_pdf_filename(file_dir):
    # 设置所有pdf文件名保存的txt文件名
    str_dir= file_dir.split("/")
    str_dir.pop()
    filename = '/'.join(str_dir)+"/filename.txt"
    print(filename)
    #将文件清空,以w格式打开文件，如果文件存在，则清空，否则创建文件。
    with open(filename,'w') as f:
        pass;
    for root,dirs,files in os.walk(file_dir):
        # print("当前目录路径--",root)
        # print("子目录有--",dirs)
        # print("文件有--",files)
        # 每一个files是一个列表，这里需要将名字改成完整形态
        for file in files:
            file_name = os.path.join(root,file)
            #写入到文件
            with open(filename, 'a') as f:
                f.write(file_name)
                f.write("\n")
    # print("文件名已经写入到", filename, "文件中")
    return filename

# pdf_name是pdf文件的名字，file_dir是txt格式文件保存的目录
def get_fielname(pdf_name, file_directory):
    paths = pdf_name.split('/')[-1]
    new_file_name = os.path.splitext(paths)[0] + '.txt'
    return os.path.join(file_directory, new_file_name)


# 将目录下面的文件转换为txt
def convert_to_txt(file_dir):
    # 转换之后的txt文件保存位置。
    txt_file_dir = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT"
    #获取pdf文件名保存的位置
    filename = _save_pdf_filename(file_dir)
    #读取文件内容，依次处理
    count = 0
    with open(filename, 'r')as f:
        for file in f:
            count += 1
            #确保路径正确，出现反斜杠是在使用os.walk遍历目录的时候出现的。
            file = file.replace("\\", '/').strip()
            print("**********正在转换第", count, "*************个pdf文件")
            # 调用parse获取pdf内容
            results = _parse(file)
            txt_file = get_fielname(file,txt_file_dir)
            with open(txt_file,"w") as f:
                f.write(results)

def _delete_space_and_newline(string):
    # 因为有中文，英文冒号，所以这里分别处理
    return string.strip().replace("\n","").replace(":","").replace("：","").strip()

def _regexp_txt(content,key1,key2,way=0):
    pattern = re.compile(key1+'(.*?)'+key2,re.S)
    result = re.findall(pattern,content)
    # print(result[0])
    if result:
        if way == 0:
            return _delete_space_and_newline(result[0])[:-3]
        # 如果是大的编号，去掉最后两个字符
        elif way == 1:
            return _delete_space_and_newline(result[0])[:-2]
    else:
        # print("没找到对应字段")
        return None
# 根据传入的txt文件，读取文件中内容，并获取关键字，事件类型等
def _get_keywords(filename):
    case = {}
    with open(filename,'r')as f:
        txt_content = f.read()
        case['keywords'] = _regexp_txt(txt_content, "关键词", "教学应用")
        case['case_properties'] = _regexp_txt(txt_content,"案例属性","案例描述",1)
    return case

# 判断指定filename中是否包含下面这些关键字，包含，则返回True
def is_meet_demand(filename):
    catagory = ["问题类型","案例类型","事故类型","事件类型","食品安全"]
    keywords = ["生产安全","食品安全","药品安全","校园安全","社会安全","安全","政府危机管理","污染","安全事故","公共卫生","传染病","医患纠纷","自然灾害",
                "医疗","群体性事件","暴力","医疗卫生","医患关系"]
    case = _get_keywords(filename)
    # print(case)
    for value in catagory:
        #排除城市管理和政府创新数据
        if case['case_properties'] and value in case['case_properties']:
            for keyword in keywords:
                #进一步筛选数据。
                if keyword in case["keywords"] or keyword in case["case_properties"]:
                    return True
                else:
                    print(filename)
    return False

def filter_cases(raw_dir,ripe_dir):
    for root,dirs,files in os.walk(raw_dir):
        for file in files:
            file = os.path.join(root,file).replace("\\",'/')
            if is_meet_demand(file):
                #如果符合要求,将文件移动到指定目录。
                shutil.move(file,ripe_dir)
    print("已经筛选出适合的数据")

#前面的过程有pdf转换成txt，然后在筛选txt文件，接下来是处理筛选出来的txt文件。

# 根据文件内容进行分类
def eventClassification(content):
    pass

# 案例名称  案例简介  案例属性 案例介绍
def _get_case_properties(filename):
    #获取案例的属性，返回一个dict对象
    case = {}
    with open(filename,'r')as f:
        case['case_name'] = f.readline().strip()
        content = f.read()
        case['case_desc'] = _regexp_txt(content,"案例简介","关键词")
        case['case_properties']  = _regexp_txt(content,"案例属性","案例描述",1)
        case['case_desc_all'] = _regexp_txt(content,"案例描述","观点综述",1)
        if not case['case_desc_all']:
            case['case_desc_all'] = _regexp_txt(content,"案例描述","相关参考",1)
        if not case['case_desc_all']:
            case['case_desc_all'] = _regexp_txt(content, "案例描述", "理论综述", 1)
        print(case['case_name'])
        print(case['case_desc_all'])

# 对所有文件进行剖析，然后提取出属性进行存储
def write_to_mysql(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file = os.path.join(root, file).replace("\\", '/')
            _get_case_properties(file)

filename = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT_Ripe/２００３年辽宁海城豆奶中毒事件.txt"
_get_case_properties(filename)
# raw_dir = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT"
# ripe_dir = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT_Ripe"
# filter_cases(raw_dir,ripe_dir)
# print(is_meet_demand(filename))
# print(_save_pdf_filename("C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZhe"))
# convert_to_txt("C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZhe")
# get_keywords("C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT/２００３年大连港发展中的政府定位与决策.txt")
# write_to_mysql(ripe_dir)
