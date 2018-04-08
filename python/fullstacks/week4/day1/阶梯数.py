# @author: "QiuJunan"
# @date: 2018/3/27 16:59
# 阶梯走法  N阶楼梯上楼问题：一次可以走两阶或一阶，问有多少种上楼方式。（要求采用非递归）

# 可以计算走0-10级阶梯中的走法。（非递归）
def run():
    a = [0,1,2]
    for i in range(3,10):
        ret = a[i-1]+a[i-2]
        a.append(ret)

    print(a)

run()

# 使用递归实现
def run_digui(i):
    # 递归要有终止条件。
    if i==1:
        return 1
    if i==2:
        return 2

    return run_digui(i-1)+run_digui(i-2)

ret = run_digui(4)
print(ret)