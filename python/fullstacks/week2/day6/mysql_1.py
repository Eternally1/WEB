# @author: "QiuJunan"
# @date: 2018/3/11 11:47
# 创建数据库表操作
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","movie")
# 使用cursor()方法创建一个游标对象
cursor = db.cursor()
# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")
# 使用fetchone()方法获取单条数据
data = cursor.fetchone()
print("Database version ： %s" % data)

# 创建数据库表
cursor.execute("DROP TABLE IF EXISTS MOVIE")
# 使用预处理语句创建表
sql = """CREATE TABLE MOVIE(
        FIRST_NAME VARCHAR(20) NOT NULL,
        LAST_NAME VARCHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
)"""
cursor.execute(sql)


# 关闭数据库
db.close()
