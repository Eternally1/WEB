#继承
class Parent:
    def hello(self):
        print("正在调用父类...")

class Child(Parent):    #定义Child，继承Parent。
    def hello(self):    #复写父类方法
        print("正在调用子类方法....")
    # pass    #不做任何事情，一般认为是占位语句

p = Parent()
p.hello()
c = Child()
c.hello()