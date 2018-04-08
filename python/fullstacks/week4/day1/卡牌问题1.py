# @author: "QiuJunan"
# @date: 2018/3/27 16:08
# 暂时没有做出来
# 求用最多的桌上卡牌与小明手中的卡牌进行加减乘除四则运算 最后使 果达到13.如小明卡牌是5，桌上卡牌是1
# 3 9 4 2 2，此题答案即5+1/3+9+4-2 即最多可容纳5张牌（此题不考乘除优先级，先到优先，桌上卡牌可重）

# def run():
#     xm = 5
#     desk = [1,3,9,2,4,4]
#
#     for i in range(6):
#         # ret1,ret2,ret3,ret4 = opera(xm,desk[i])
#         # print(ret1,ret2,ret3,ret4)
#         ret = opera(xm,desk[i])
#         i +=1
#         for j in range(len(ret)):
#             result = opera(j,desk[i])
#             print(result)
#
#
#
# def opera(a,b):
#     # return(a+b,a-b,a*b,a/b)
#     return [a+b,a-b,a*b,a/b]
#
# run()

def opera(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


xm = 5
desk = [1, 3, 9, 2, 4, 4]
k = 0  # 定义一个游标
stack = [5]
while k < len(desk) or stack:
    while k < len(desk) and xm < 13:
        xm += desk[k]
        stack.append(k)
        k += 1
    if xm == 13:
        print(stack)
    k = stack.pop()
    xm -= desk[k]
    k += 1

# 可以解决的问题是当只使用加法的时候，得到3中情况，使得所得结果为13，思路和day2中的背包问题一样。

# 还是没有思路

