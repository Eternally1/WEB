# @author: "QiuJunan"
# @date: 2018/3/17 10:08
# 上下文管理器
# 1、普通的数据库资源的创建和释放场景
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

def handle_query():
    db = Database()
    db.connect()
    print('handle ---',db.query())
    db.close()

handle_query()