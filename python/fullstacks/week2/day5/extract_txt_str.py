# @author: "QiuJunan"
# @date: 2018/3/9 11:47
# 从txt文件中提取需要使用的字段。
# case_description 案例简介


path = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT/２００３年大连港发展中的政府定位与决策.txt"
import re
def regexp_txt(content,key1,key2):
    pattern = re.compile(key1+'(.*?)\d\.\d.*?'+key2,re.S)
    result = re.findall(pattern,content)
    # print(result[0])
    if result:
        return delete_space_and_newline(result[0])
    else:
        print("没找到对应字段")
        return None

def delete_space_and_newline(string):
    # 因为有中文，英文冒号，所以这里分别处理
    return string.strip().replace("\n","").replace(":","").replace("：","").strip()

def print_case():
    print(case)

case = {}
words = ["案例编号","案例名称","事件分类","发生地","发生时间","发生地点","案例描述","事件原因","人员伤亡","经济损失","社会影响","影响范围","处理主体","平息原因。"]

def extract_field(path):
    with open(path,'r') as f:
        # print(path)
        # case["casename"] = f.readline().strip()
        txt_content = f.read()
        case['keywords'] = regexp_txt(txt_content,"关键词","教学应用")
        # print_case()
        # print(case['keywords'])
        return case['keywords']

if __name__ == '__main__':
    extract_field(path)


