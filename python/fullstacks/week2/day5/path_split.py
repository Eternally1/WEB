# @author: "QiuJunan"
# @date: 2018/3/9 9:29
"""
测试路径拆分
"""
import os
import time
start_time = time.clock()
path = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZhe/20180303122522/２０１３年云南昆明抵制ＰＸ项目事件.pdf"
paths = path.split('/')[-1]
new_file_name = os.path.splitext(paths)[0]
print(new_file_name)
end_time = time.clock()
# time.sleep(2)
print(end_time,start_time)
print("总共用时:",end_time-start_time)

path = "C:/others/doc/teamAndPersonInfo/GraduationProject/DataSet/MaiNiZhe"
paths = path.split("/")
paths.pop()
print('/'.join(paths))

