# @author: "QiuJunan"
# @date: 2018/3/9 9:23

"""
将所有pdf文件转换为TXT文件。
"""
import pdf_to_txt as ptt
import file_name as fn
import warnings

import time

warnings.filterwarnings("ignore")
# dir_name是pdf文件目录   filename存储所有的pdf文件名字的位置。  file_directory是转换成txt之后文件保存的目录
dir_name = "C:\\others\\doc\\teamAndPersonInfo\\GraduationProject\\DataSet\\MaiNiZhe"
filename = "C:\\others\\doc\\teamAndPersonInfo\\GraduationProject\\DataSet\\filename.txt"
file_directory = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZheTXT"
filename = fn.file_name_list(dir_name,filename)
# print(filename)
count = 0
# 开始对每个pdf文件进行转换
start_time = time.clock()
with open(filename,'r')as f:
    for file in f:
        count +=1
        file_name = file.replace("\\",'/').strip()
        print("**********正在转换第",count,"*************个pdf文件")
        # 调用pdf转txt方法，将pdf转换成txt并保存到指定位置中。
        ptt.parse(file_name,file_directory)
end_time = time.clock()
print("转换pdf文件总共用时",end_time-start_time,"秒")

