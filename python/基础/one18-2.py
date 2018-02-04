import one18 as one
# 尽管这里引用的时候会报错，但是程序可以执行。此时的问题是测试部分的代码也执行了一次

print("32摄氏度 = %.2f华氏度" % one.c2f(32))
print("99华氏度 = %.2f摄氏度" % one.f2c(99))


# print(__name__)  #获取当前模块的名字
# print(one.__name__)  # 获取被引用模块的名字