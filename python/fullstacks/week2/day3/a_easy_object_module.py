# @author: "QiuJunan"
# @date: 2018/3/7 15:35
# 这里的是参考 http://aosabook.org/en/500L/a-simple-object-model.html 的文章。
#  所有类继承的基类 Base
class Base(object):
    def __init__(self,cls,fields):
        self.cls = cls
        self._fields = fields

    def read_attr(self,fieldname):
        # 读取对象fieldname的值
        return self._read_dict(fieldname)

    def write_attr(self,fieldname,value):
        #写入对象fieldname属性和值
        self._write_dict(fieldname,value)

    def isinstance(self,cls):
        #？？？
        return self.cls.issubclass(cls)

    def _read_dict(self,fieldname):
        # 如果没有这个属性，返回的就是MISSING，而MISSING是object的实例对象。
        return self._fields.get(fieldname,MISSING)

    def _write_dict(self,fieldname,value):
         self._fields[fieldname] = value;

MISSING = object()

class Instance(Base):
    # 实例化一个用户定义的类
    def __init__(self,cls):
        # print("***************",Class)
        # 问题出在这里，这里的Class怎么理解？？？？
        assert isinstance(cls,Class)
        Base.__init__(self,cls,{})

class Class(Base):
    def __init__(self,name,base_class,fields,metaclass):
        Base.__init__(self,metaclass,fields)
        self.name = name
        self.base_class = base_class

OBJECT = Class(name="object",base_class=None,fields={},metaclass=None)
# TYPE是OBJECT的子类
TYPE = Class(name="type",base_class=OBJECT,fields={},metaclass=None)
# TYPE是他自身的实例
TYPE.cls = TYPE
# OBJECT是TYPE的实例
OBJECT.cls = TYPE

def test_read_write_field_class():
    A = Class(name="A",base_class=OBJECT,fields={"a":1},metaclass=TYPE)

    assert A.read_attr("a") == 1
    print(A.read_attr("a"),A.name,A.base_class)
    # 关于base_class 和 metaclass不清楚。
    # print(object())
    A.write_attr("a",6)
    print(A.read_attr("a"),A.name,A.base_class)

def test_isinstance():
    class A(object):
        pass
    class B(A):
        pass
    b = B()
    assert isinstance(b, B)
    assert isinstance(b, A)
    assert isinstance(b, object)
    assert not isinstance(b, type)

    A = Class(name="A",base_class=OBJECT,fields={},metaclass=TYPE)
    B = Class(name="B",base_class=A,fields={},metaclass=TYPE)
    b = Instance(B)

test_isinstance()









