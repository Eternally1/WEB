# @author: "QiuJunan"
# @date: 2018/3/11 12:08
# 数据库插入操作
import pymysql

db = pymysql.connect('localhost','root','root','movie')
cursor = db.cursor()


# 数据库插入操作
# sql = """INSERT INTO MOVIE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES
#         ('Mac','Mohan',20,'M',2000)"""

#sql的另一种书写方式
sql = "INSERT INTO MOVIE (FIRST_NAME,\
        LAST_NAME,AGE,SEX,INCOME)\
        VALUES('%s','%s','%d','%c','%d')" % \
      ('Jacky','Qiu',22,'M',900)

# 执行sql语句
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()

