# @author: "QiuJunan"
# @date: 2018/3/28 15:12
# 2017年机试题目，这里可以输出所有结果为13的组合，之后在寻找一个卡牌数目最多的情况即可
# 目前能做到的是按照顺序将牌一次计算进来，但是不能做到 如不要1，直接从3开始的一些卡牌组合。
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
i = 0
# desk = [1,3,4]
stack = [5]
count = 0
def mFind(num,i):
    if i<len(desk):
        global stack
        global count
        for op in ['+', '-', '*', '/']:
            stack.append(op)
            stack.append(desk[i])
            num  = opera(num,desk[i],op)
            if num == 13:
                count +=1
                print(stack)
            mFind(num,i+1)      # 这里通过递归可以获得所有的组合情况
            n = stack.pop()     # 这里是为了在回退到上一部的时候，对应的进栈数据需要出栈。
            m = stack.pop()
            if m == '+':        # num的值也要回退。
               num =  opera(num,n,'-')
            elif m =='-':
                num = opera(num, n, '+')
            elif m == '*':
                num = opera(num,n,'/')
            elif m == '/':
                num = opera(num,n,'*')
    else:
        # 在这里可以输出所有的组合情况
        pass

mFind(5,0)
print(count)