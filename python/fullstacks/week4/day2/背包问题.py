# @author: "QiuJunan"
# @date: 2018/3/28 12:17
# 寻找所有符合条件的组合
# 改进：goods定义成对象列表

weight = 10 # 背包总重量
goods = [1,8,4,3,5,2]   # 商品重量

stack = []  # 用于存储已经选择的商品
k = 0       # 当前物品的游标
l = len(goods) # 可选的物品
w = weight  # 背包的可用空间

while k<l or stack:
    while w>0 and k<l: # 当背包有空间并且有物品可以装时
        if w >= goods[k]:
            stack.append(k)  # 放入背包中的是对应的商品的编号0-5
            w -= goods[k]
        k += 1  # 不管是否转入背包，都需要移动游标
    if w == 0: # 终止条件，表示刚好装满【重要】,找到就打印一下
        print(stack)
    # 这里的回退是在没有找到的时候执行
    k = stack.pop() # 回退
    w += goods[k]   # 更新背包容量
    k +=1


