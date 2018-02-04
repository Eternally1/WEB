"""
属性访问方法的使用
"""
class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            # 注意   调用基类的设置属性的方法
            #  super().__setattr__(name,value)
            # 另一种方法
            self.__dict__[name] = value

    def getArea(self):
        return self.width * self.height

rect = Rectangle()
rect.square = 5
print(rect.getArea())
print(rect.__dict__)

rect2 = Rectangle(4,5)
print(rect2.getArea())