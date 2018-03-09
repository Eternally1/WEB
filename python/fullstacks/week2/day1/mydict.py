# @author: "QiuJunan"
# @date: 2018/3/6 14:03

# 单元测试相关
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'dict' object has no attribute %s"%key)

    def __setattr__(self,key,value):
        self[key] = value



