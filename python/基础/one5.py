"""
    lambda  匿名函数
"""
temp = lambda x: 2 * x + 1
print(temp(5))

temp1 = lambda x,y : x+y
print(temp1(2, 5))

print("-----------filter()**1---------------")
temp2 = filter(None,[1,0,False,True])
print(list(temp2))

print("-----------filter()筛选出奇数---------------")
def odd(x) :
    return x % 2
temp3 = filter(odd,range(1,10))
print(list(temp3))

print("-----------filter()筛选出奇数,使用lambda---------------")
print(list(filter(lambda x : x%2,range(1,10))))


print("-------------map()---------------")
print(list(map(lambda x: x*2,[1,2,3,4,5])))