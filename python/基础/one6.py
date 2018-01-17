# 递归  求阶乘


# 非递归版本
def NoRecursion(x):
    result = x
    for i in range(1,x):
        result *=i
    return result
print(NoRecursion(5))


#递归版本
print("-----------递归实现阶乘--------------")
def factorial(n):
    if(n == 1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

print("-----------递归实现斐波那契--------------")
# 分治思想
def factorial2(n):
    if n <1:
        return -1
    if n == 1 or n==2:
        return 1
    else:
        return factorial2(n-1)+factorial2(n-2)
print(factorial2(12))

print("------------汉罗塔----------------")
def hanoi(n,x,y,z):    # n个盘子，x y z三根针，借助y，从x移到z。
    #1、判断结束条件
    if(n == 1):
        print(x,'-->',z)
    else:
        #1、将前n-1个盘子从x移到y，借助z将x移到y
        hanoi(n-1,x,z,y)
        #2、将最后一个盘子从x移到z上
        print(x, "-->", z)
        #3、将y上的n-1个盘子移到z上
        hanoi(n-1,y,x,z)
hanoi(4,'a','b','c')