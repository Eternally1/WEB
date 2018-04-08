# @author: "QiuJunan"
# @date: 2018/3/17 10:11
# 上下文管理器，引言
# 2、使用装饰器
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

def dbconn(fn):
    def wrapper(*args,**kwargs):
        db = Database()
        db.connect()
        ret = fn(db,*args,**kwargs)
        db.close()
        return ret
    return wrapper

# handle_query = dbconn(handle_query)
@dbconn
def handle_query(db=None):
    print('handle--',db.query())

handle_query()