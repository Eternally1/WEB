# @author: "QiuJunan"
# @date: 2018/3/11 12:12
#数据库查询操作
import pymysql
db = pymysql.connect("localhost","root","root","movie")
cursor = db.cursor()

# sql查询语句
sql = "SELECT * FROM MOVIE WHERE INCOME > '%d' " % (6000)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    if results:
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%d,sex=%c,income=%d"%(fname,lname,age,sex,income))
    else:
        print("There are no qualified data")
except:
    print("Error:unable to fetch data")

# 数据库更新操作
sql = "UPDATE MOVIE SET AGE = AGE + 10 WHERE INCOME = '%d'" % (5000)
try:
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    db.rollback()

# 删除操作
sql = "DELETE FROM MOVIE WHERE AGE < '%d'" % (30)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
