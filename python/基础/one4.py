# 全局变量和局部变量

print("-----------global测试---------------");
count = 5;
def PartFunc():
    count = 10;
    print(count);

PartFunc(); #10
print(count); #5


def OverallFunc():
    # 当内部作用域想修改外部作用域的变量时，就要用到global.
    global count;
    count = 10;
    print(count);

OverallFunc();
print(count);



#内嵌函数
# func2()只能在func1()类调用
print("-----------内嵌函数---------------");
def func1():
    print("func1()执行了");
    def func2():
        print("func2()执行了");
    func2();
func1();

print("-----------闭包---------------");
def FuncX(x):
    def FuncY(y):
        return x*y;
    return FuncY;
temp = FuncX(8);
print(temp(2));
# print(FuncX(8)(2));    #这种做法也行


print("-----------闭包一个错误案例---------------");
# 这里的FuncZ()函数里面有一个变量z，内嵌函数FuncZZ()里面也有一个z，Python为了
# 保护变量的作用于，故将外部的z屏蔽了
# def FuncZ():
#     z = 5;
#     def FuncZZ():
#         print(z);
#         z *= z;    # 可以打印z，但是不能修改；z是一个非全局的外部变量，在内部不能修改，只能引用
#         return z;
#     return FuncZZ();
# print(FuncZ());

print("-----------闭包案例修改python3之前的方法---------------")
# 通过容器来解决，容器是存储在栈里面，不会被屏蔽。
def FuncZ():
    z = [5];
    def FuncZZ():
        z[0] *= z[0];
        return z[0];
    return FuncZZ();
print(FuncZ());


print("-----------闭包案例修改python3的方法---------------");
# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，
def FuncZ():
    z = 5
    def FuncZZ():
        nonlocal z
        z *= z
        return z
    return FuncZZ()
print(FuncZ())


