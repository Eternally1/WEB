import pymysql
#from mytoolbox import exceptionglogger
import datetime

#Logger_name = datetime.datetime.today().strftime('%Y-%m-%d')
#Logger = exceptionglogger.create_logger('{0}.log'.format(Logger_name))


class ExSQL:
    def __init__(self, user='root', password='root', db=None, tablename=None):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user=user, password=password, db=db,
                                    charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.db = db
        self.tablename = tablename
        self.content_flag = False
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
    
    #@exceptionglogger.exception(Logger)
    def insert_data(self, fields, values):
        """
        eg:
        exsql = ExSQL()
        exsql.insert_data('emergency','(Title,Time,Department,Post,News)',('标题', '2017-1-1', '中央办公厅', '新华日报', '加速企业创新能力发展'))
        
        :param tablename: emergency
        :param fields: '(Title,Time,Department,Post,News)'
        :param values: ('标题', '2017-1-1', '中央办公厅', '新华日报', '加速企业创新能力发展')
        """
        # self.cursor.execute(
        #     "insert into {0} {1} values {2};".format(self.tablename, fields, values)
        # )
        self.cursor.execute(
            "insert into %s %s values %s;" % (self.tablename,fields,values)
        )
        self.conn.commit()
    
    #@exceptionglogger.exception(Logger)
    def update_CutNews_data(self, content, title):
        self.cursor.execute(
            "update {2} set CutNews={0} where Title={1};".format(repr(content), repr(title), self.tablename)
        
        )
        self.conn.commit()
    
    #@exceptionglogger.exception(Logger)
    def update_EC_data(self, emergencycase, title):
        self.cursor.execute(
            "update {2} set EmergencyCase={0} where Title={1};".format(repr(emergencycase), repr(title), self.tablename)
        
        )
        self.conn.commit()
    
    def get_one(self):
        try:
            if self.content_flag:
                return self.cursor.fetchone()
            else:
                self.cursor.execute("select * from %s;" % self.tablename)
                self.content_flag = True
                return self.cursor.fetchone()
        except Exception as e:
            print(e)
            self.content_flag = False
    
    def get_content(self, select=None):
        """
        
        :param select: 'Title,News'
        :return:
        """
        if not select:
            self.cursor.execute("select * from %s;" % self.tablename)
        else:
            self.cursor.execute("select {0} from {1}".format(select, self.tablename))
        return self.cursor.fetchall()
    
    def search_one(self, title, select='*'):
        """
        根据标题提取出新闻
        :param title:
        :return:
        """
        self.cursor.execute("select {2} from {0} where  Title like '%{1}%';".format(self.tablename, title, select))
        return self.cursor.fetchone()
    
    def change_table(self, tablename):
        self.tablename = tablename


if __name__ == "__main__":
    with ExSQL('root', 'root', 'city', 'emergency') as exsql:

        print(exsql.search_one('2月1日 武汉三居民被困电梯 被救援人员救出'))
        # exsql = ExSQL()   # 使用with语句后，不需要此句
        # table = 'emergency'
        # exsql.set_tablename(table)
        
        # 插入数据测试
        # Title = '标题3'
        # Time = '2017-07-25 18:06'
        # Department = '武汉市政府'
        # Post = '楚天晚报'
        # News = '明日武汉冰雹'
        # fields = '(Title,Time,Department,Post,News)'
        # values = Title, Time, Department, Post, News
        # exsql.insert_data(fields, values)
        # 插入错误代码测试
        # values = Title, Time, Department, Post
        # exsql.insert_data(fields, values)
        
        # 更新数据测试
        # exsql.update_CutNews_data('今日 北京 暴雨', '标题1')
        # 更新数据错误代码测试
        # exsql.update_CutNews_data('今日 北京 暴雨')
        
        # 更新数据测试
        # exsql.update_EC_data(True, '标题1')
        # exsql.update_EC_data(False, '标题1')
        
        # 测试获取单个记录
        # print(exsql.get_one())
        # print(exsql.get_content())
        # print(exsql.get_content(select='Title,News'))
        # print(exsql.get_one())
        # print(exsql.get_one())
        # print(exsql.get_one())
        # print(exsql.get_one())
        

