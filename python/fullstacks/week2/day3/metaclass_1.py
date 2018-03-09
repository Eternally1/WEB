# @author: "QiuJunan"
# @date: 2018/3/8 16:09
# 参考廖雪峰的教程
"""
先定义metaclass，然后创建类，最后创建实例。
"""
# metaclass是类的模板，所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        # 可以打印一下，看具体是什么。
        print(cls," ,",name," ,",bases,", ",attrs)
        def add(self,value):
            print(type(self))  #self是MyList的实例对象。
            # 要使用append，需要继承list。
            self.append(value)
        attrs['add'] = add
        return type.__new__(cls,name,bases,attrs)

# 使用ListMetaclass来定制类
class MyList(list,metaclass=ListMetaclass):
    pass
# 传入关键字metaclass，魔术就生效了。指示python解释器在创建MyList时
# 需要通过__new__方法创建。

L = MyList()
L.add(1)
print(L)
print(L.__dict__)
# 可以看到add方法是定义在MyList类上在。
print(L.__class__.__dict__)

# 直接在MyList中定义add方法
class MyList2(list):
    def add(self,value):
        self.append(value)

L2 = MyList2()
L2.add(2)
print(L2)
# L2也是list的子类，所以可以使用append方法
print(isinstance(L2,MyList2))
print(isinstance(L2,list))