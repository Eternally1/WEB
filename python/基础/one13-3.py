# 绑定
class A:
    def printA():  #注意这里少了self，此时代表没有绑定
        print("AAA")
A.printA()    # 但是可以使用类名访问
a = A()
# a.printA()    #没有绑定的情况下，实例化对象不能访问

#查看A的属性
print(a.__dict__)



class AA:
    def setX(self,x):
        self.x = x
    def printX(self):
        print(self.x)

aa = AA()
aa.setX(5)
print(aa.__dict__)
print(AA.__dict__)

del AA
aa.printX()  #注意这里还是可以打印的，类中定义的属性和方法都是静态的，就算类对象被删除了
                #他们任然存在于内存中，只有当程序退出时才被释放。

