# @author: "QiuJunan"
# @date: 2018/3/17 10:18
# 上下文管理器
class Database(object):
    def __init__(self):
        self.connected = False
    def connect(self):
        self.connected = True
    def close(self):
        self.connected = False
    def query(self):
        if self.connected:
            return 'query data'
        else:
            raise ValueError('DB not connected')
    def __enter__(self):
        self.connect()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.close()


def handle_query():
    with Database() as db:
        print('handle--',db.query())

handle_query()


#上下文管理器的解释
class Contextor:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

contextor = Contextor()

with contextor as var:
    #with_body
    pass

# 执行 contextor 以获取上下文管理器
# 加载上下文管理器的 exit() 方法以备稍后调用
# 调用上下文管理器的 enter() 方法
# 如果有 as var 从句，则将 enter() 方法的返回值赋给 var
# 执行子代码块,这里使用pass了
# 调用上下文管理器的 exit() 方法，如果 with_body 的退出是由异常引发的，那么该异常的 type、value 和 traceback 会作为参数传给 exit()，否则传三个 None
# 如果 with_body 的退出由异常引发，并且 exit() 的返回值等于 False，那么这个异常将被重新引发一次；如果 exit() 的返回值等于 True，那么这个异常就被无视掉，继续执行后面的代码
# 【S】只要记住在使用的时候会自动调用enter，执行完之后会自动执行exit即可。

