# @author: "QiuJunan"
# @date: 2018/3/28 9:32
# 在二维数组中查找


import numpy as np

str1 = input("请输入一个二维数组，以;区分:")
str2 = input("请输入要查询的数字:")
lines = str1.split(";")
lists = []
for line in lines:
    list = [int(x) for x in line.split(",")]    # 将列表中数据转换成int类型
    lists.append(list)

count = 0
for list in lists:
    if int(str2) in list:
        print("数字",str2,"存在于二维数组中")
        break
    else:
        count += 1
# 二维列表长度计算
# print(len(lists)*len(lists[0]))
# 只需要知道维数就行了
if count == len(lists):
    print("数字",str2,"不存在二维数组中")




