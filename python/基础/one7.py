# 字典  使用大括号创建...
dict1 = {"Tom":"right","Mary":"good","Tim":"fine"}
print(dict1["Tom"])

#  dict()  只接受一个参数，故使用列表封装起来，然后每一项使用的是元组
dict2 = dict([('a',96),('C',67),('F',70)])
print(dict2)
dict2['a'] = 98
print(dict2)    # 可以修改。

# 另一种创建方法，注意小甲鱼不能使用双引号
dict3 = dict(小甲鱼="让编程改变世界",Tom="good good study")
print(dict3)
dict3['mary'] = "right"
print(dict3)

# 字典的内建方法  copy()浅拷贝和赋值
a = {1:"Tom",2:"Mary",3:"Jack"}
# 潜赋值
b = a.copy()
# 赋值
c = a
# 查看地址  通过地址可以发现，a c指向同一个字典
print("id(a)",id(a))
print("id(b)",id(b))
print("id(c)",id(c))

print(a.pop(1))
print(a.popitem())  # 随机弹出，一般是尾部的