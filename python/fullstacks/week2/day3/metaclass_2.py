# @author: "QiuJunan"
# @date: 2018/3/8 17:18

# ORM 对象关系映射   廖雪峰


# 2、定义Field类，负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)

# 3、在Field类型上定义各种类型Field
class StringField(Field):
    def __init__(self,name):
        super().__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super().__init__(name,'int')

# 4、编写ModelMetaclass
class ModelMeteclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print("Found model:%s"% name)
        mappings = dict()
        print("*************",attrs,"************")
        for k,v in attrs.items():
            if isinstance(v,Field):
                print("Found mapping : %s==>%s" % (k,v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  #保存属性和列的映射关系
        attrs['__table__'] = name   #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMeteclass):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 1、先写调用接口
class User(Model):
    id = IntegerField('id')
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")

# 创建一个实例
# 里面的参数就是ModelMeteclass里面的attrs
u = User(id=12345, name="Tom", email="test@orm.org", password="my-pwd")
# 保存到数据库
u.save()