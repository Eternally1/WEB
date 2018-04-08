# @author: "QiuJunan"
# @date: 2018/3/28 11:57


# 判断一个字符是否为数字
s = '123';
print(s.isdigit())

# 求一个列表所有元素乘积
def multiple(l):
    ret = 1
    for i in range(len(l)):
        ret *= l[i]
    return ret


if __name__=='__main__':
    print(multiple([1,2,3,4,]))