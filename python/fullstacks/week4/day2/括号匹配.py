# @author: "QiuJunan"
# @date: 2018/3/28 10:03
# http://python.jobbole.com/87581/ 【参考链接】

def match(expr):
    """
    括号匹配问题
    :param expr:传递过来的字符串
    :return: 返回True或者False
    """
    left = ['(','[','{']
    right = [')',']','}']

    stack = []  # 创建一个栈
    # 遍历字符串
    for i in expr:
        if i in left:
            stack.append(i)
        elif i in right:
            # 如果栈为空或者栈顶元素与当前元素不匹配，返回False
            if not stack or not 1<= ord(i)-ord(stack[-1]) <=2:
                return False
            else:
                stack.pop() # 列表删除元素

    return not stack    # 遍历完成之后，如果栈空，就表示匹配，返回True，否则返回False

ret1 = match("([]{()})")
ret2 = match("([{})]")
print(ret1,ret2)

# 根据ASCII码值来断定是否匹配。
a = ['{','}','(','[',')',']']
print(ord(a[0]),ord(a[1]),ord(a[2]),ord(a[3]),ord(a[4]),ord(a[5]))