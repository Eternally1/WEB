# @author: "QiuJunan"
# @date: 2018/3/9 15:46
"""
将提取到的字段写入到数据库
"""
import os
import extract_txt_str as ets

keywords =set()
# 遍历下面这个目录下面的txt文件，分别完成提取
file_dir = "C:\\others\\doc\\teamAndPersonInfo\\GraduationProject\\DataSet\\MaiNiZheTXT"
keyword_filename = "C:\\others\\doc\\teamAndPersonInfo\\GraduationProject\\DataSet\\keywords.txt"
for root,dirs,files in os.walk(file_dir):
    # print(root,dirs,files)
    for file in files:
        path = os.path.join(file_dir,file)
        keyword = ets.extract_field(path)
        if keyword:
            keyword = set(keyword.split(";"))
            keywords = keywords.union(keyword)
            # print(keyword)

print(keywords)
# 关键词写入文件
for line in keywords:
    with open(keyword_filename, 'a')as f:
        f.write(line)
        f.write("\n")




