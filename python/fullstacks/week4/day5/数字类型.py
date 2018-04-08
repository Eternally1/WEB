# @author: "QiuJunan"
# @date: 2018/3/31 11:11
# 关于十六进制，八进制，二进制相关

# 分别定义二、八、十六进制的数据
bin0 = 0b01001
oct0 = 0o17
hex0 = 0x1A
# 输出的时候会转化为10进制输出
print(bin0," ",oct0," ",hex0)

# 内置方法将整数转换成对应的进制表示的--字符串
z = 22
bin1 = bin(z)
oct1 = oct(z)
hex1 = hex(z)
print(bin1," ",oct1," ",hex1)

# 通过给定的base=8，将传入的字符串看做为八进制的形式，转换成对应的十进制
s = "22"
i = int(s,base=8)
print(i)

# 复数
com = complex(2,5)
print(com)

# 还有许多处理数字对象的工具，比如内置数学函数，公用模块random math等

# 数字类型格式化输出
print("{0:b},{1:0},{2:x}".format(8,16,64))
print("%o,%x" % (8,16,64))