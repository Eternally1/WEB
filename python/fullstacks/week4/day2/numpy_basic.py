# @author: "QiuJunan"
# @date: 2018/3/28 9:10
# numpy模块，二维数组创建

import numpy as nu
# 创建一个元素全为0的两行三列的二维数组
a = nu.zeros((2,3))
b = nu.array([(1,2,3),(4,5,6)])
# 起始为10，终止为30（不包括30），步长为3，返回值是一个列表
c = nu.arange(10,30,3)
# 在0-11共12个数中构建成4行3列。
d = nu.arange(12).reshape(4,3)
print("a=",a,'\nb=',b,'\nc=',c,'\nd=',d)

# 给二维数组赋值,需要和列数相同
a[0] = [1,2,3]
print(a)

# 使用列表解析创建一个7*7的二维数组，并且初始化为0
e =[[0]*7 for i in range(7)]


