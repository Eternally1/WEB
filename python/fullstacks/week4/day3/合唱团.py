# @author: "QiuJunan"
# @date: 2018/3/29 8:59
# 题目来源：牛客网



def init_input():
    stu_num = input("请输入学生个数:")
    stus = input("请输入每个学生的能力值:")
    control = input("请输入选取学生名数，学生位置编号最大允许差：")
    # 数据类型进行转化
    stu_num = int(stu_num)
    stus = [int(i) for i in stus.split(" ")]
    k = int(control.split(" ")[0])
    d = int(control.split(" ")[1])
    return (stu_num,stus,k,d)   # 以元组返回，便于赋值


def computeMultiple(stack,stus):
    """计算能力值的乘积"""
    ret = 1 # 这步是关键
    for i in range(len(stack)):
        index = stack[i]    # 取得能力值学生索引
        temp = stus[index]      # 取得能力值
        ret *= temp
    return ret

# # 先手动定义一下初始值
# stu_num = 6
# stus = [7,1,7,2,7,3]
# k = 3
# d = 2
# 分析一下问题：
# 1、按照顺序从n个学生中选取k名
def get_max_multiple():
    stu_num,stus,k,d = init_input()
    stack = []   # 用于存储当前选择的学生
    count = 0   # 用于在为1的时候，表示此时还没有maxMultiple,从而给它赋值
    i = 0
    while stack or i<stu_num:
        while i<stu_num:
            if len(stack)<k:
                # 3、判断间隔是否为小于d
                if not stack:
                    stack.append(i)
                elif stack and i-stack[-1]<=d:
                    stack.append(i)
            if len(stack)==k:
                # 将这k个数里面的能力值计算出来，然后和maxMutiple进行比较
                ret = computeMultiple(stack,stus)
                count += 1
                # 2、能力值乘积的初始化为多少合适？
                # 【s】根据输入数据的范围，但是这里的范围比较大，不适合判断
                # 【s】另一种，将第一个计算出来的值赋值给maxMutiple.
                if count == 1 or ret > maxMultiple:
                    maxMultiple = ret
                break   # 得到一种满足条件的就退出循环，开始下一种
            i += 1
        # 回退操作--关键【回溯？？】
        i = stack.pop()
        i += 1
    return maxMultiple

if __name__=='__main__':
    print("最大值是:",get_max_multiple())







