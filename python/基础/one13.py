# 对象
class Turtle:   #python中类名约定以大写字母开头
    # 属性
    color="green"
    weight = 10

    # 方法
    def climb(self):
        print("我正在努力的向前爬....")

    def run(self):
        print("我正在向前跑")


# 实例化
tt = Turtle()
# print(tt.color)
# tt.climb()   #1--注意这里和下面对象调用climb()的时候显示不同的内容，这就是多态。

class TurtleA:
    def climb(self):
        print("我是TurtleA")

ta = TurtleA()
ta.climb()   #1--


# 理解self
class Ball:
    name = "AAA"
    def __init__(self,name):
        self.name = name
    def setName(self,name):
        self.name = name     # 这里的name和类中定义的name有什么区别？？
    def kick(self):
        print("我叫%s,该死的" % self.name)

a = Ball("")
a.setName("A-ball")
b = Ball("")
b.setName("B-ball")

c = Ball('土豆')


print(a.name)   #可以发现name被更新了
a.kick()
b.kick()
c.kick()


# 公有和私有的
class Person:
    name = "Qiu"
    __age = 18

    def getAge(self):
        return self.__age   #注意如何访问私有变量
p = Person()
# 注意这里如何格式化多个参数
print("name=%s,age = %d" % (p.name,p.getAge()))
# 另外一种访问的方法  对象._类名 私有变量名
print(p._Person__age)













