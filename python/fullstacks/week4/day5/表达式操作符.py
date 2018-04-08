# @author: "QiuJunan"
# @date: 2018/3/31 11:25

# 三元选择表达式,如果y为真，将x赋值给ret1，否则将z赋值给ret1
x = 5
y = False
z = True
ret1 = x if y else z
print(ret1)

# 另一种写法--暂时用不了
ret2 = (y,z)[ret1]
print(ret2)

# 两种除法
i1 = 5/3
i2 = 5//3
print(i1," ",i2)

# 幂运算,取反
i3 = 2 ** 3
print(i3)
print(bin(i3),"",bin(~i3)," ",~i3)

# 一元加减法
print(-i3," ",+i3)

