# 小实例
import random as r
class Fish:
    #定义初始化时候的坐标
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是:",self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # 在这里需要调用父类的初始化方法
        # 1--调用未绑定的父类方法
        # Fish.__init__(self)     # 这里的self应该是子类传递给父类的
        # 2--使用super函数（好处就是如果继承多个类的话不用知道基类的名字，同时一条语句即可。但是使用
        # 第一种方法就需要写多个继承的基类的方法，同时基类名字修改的话，这里也需要修改。
        super().__init__()        # 也不用传递self函数
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃...")
            self.hungry = False
        else:
            print("太撑了，吃不下了")
fish = Fish()
fish.move()
shark = Shark()
shark.move()



# 多重继承
class Base1:
    def foo1(self):
        print("我是foo1")

class Base2:
    def foo2(self):
        print("我是foo2")

class C(Base1,Base2):
    pass

c = C()
c.foo1()
c.foo2()


# 类的组合
class Turtle:
    def __init__(self,x):
        self.num = x     #定义乌龟的数量

class Fish:
    def __init__(self,x):
        self.num = x   #定义鱼的数量

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里有乌龟%d只，鱼%d条" % (self.turtle.num,self.fish.num))

pool = Pool(3,5)
pool.print_num()


# 类对象，实例对象
class D:
	count = 0
a = D()
b = D()
c = D()
a.count = 10   #这里只是修改a的实例属性，类属性并没有被修改
print(a.count)
print(b.count)
print(c.count)

D.count = 100
print(a.count)   #这里还是输出10，是因为实例对象中已经有值了，因此访问的时候先访问实例对象中的值
print(b.count)
print(c.count)

# 如果属性名和方法名相同，那么属性名会覆盖方法名
class E:
    def name(self):
        print("mmmm")
e = E()
e.name = "Tom"
print(e.name)
# e.name()   会出错
