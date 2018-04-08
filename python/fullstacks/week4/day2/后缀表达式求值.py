# @author: "QiuJunan"
# @date: 2018/3/28 11:54
# 后缀表达式求值，目前可以输入的是后缀，可以扩展一下，后缀如何转前缀
operators = ['+','-','*','/']
operate = {
    '+':lambda a,b:a+b,
    '-':lambda a,b:a-b,
    '*':lambda a,b:a*b,
    '/':lambda a,b:a/b
}

def evalPostfix(s):
    result = []
    for i in s:
        if i.isdigit():  # 如果是数字，就压进栈,同时要注意转换类型
            result.append(int(i))
        if i in operators:
            if len(result)>=2:
                # 应该注意这里的a b的顺序,
                a = result.pop()
                b = result.pop()
                if i=='/' and a == 0:
                    print("ZeroDivisionError:除数不可为0")
                    return None
                ret = operate[i](b,a)
                result.append(ret)
            else:
                print("输入的后缀表达式不合法")
                return None
    return result[0]  # 最终结果

s = input("请输入一个后缀表达式：")
result = evalPostfix(s)
if result:
    print("运算结果为:",result)


