#coding = UTF-8
# 函数
'''
    def用来定义函数。需要先定义，再调用。
'''
# def MyFirstFunction():
#     print("my first function");
# MyFirstFunction();
#
# # 参数
# def SecondFunction(name):
#     print("你好,"+name);
# SecondFunction("Jacky Qiu");
#
# # 返回值
# def ThirdFunction(num1,num2):
#     return num1+num2;
# sum = ThirdFunction(1,3);
# print(sum);

# 函数文档
def FourthFunction():
    '这里是文档'
    print("第四个函数");
FourthFunction();
print(FourthFunction.__doc__);

# 关键字参数
def SaySome(name,words):
    print(name+"->"+words);
SaySome(name = "邱",words = "让编程改变世界");

# 默认参数
def SayHello(words = "hello"):
    print(words);
SayHello();
SayHello("say hello");

# 收集参数 （可变参数）
def ManyParams(*params,exp):
    print("参数长度是: ",len(params),exp);
    print("第二个参数是: ",params[1]);
ManyParams(1,2,3,4,5,6,exp = 6);








