# @author: "QiuJunan"
# @date: 2018/3/7 11:25
"""
小结：1、执行insert等操作之后要调用commit提交事务
    2、mysql的sql占位符是%s
"""

import mysql.connector

conn = mysql.connector.connect(user="root",password="root",database="test")
cursor = conn.cursor()

# 创建表
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
# 插入一行记录
cursor.execute('insert into user(id,name) values (%s,%s)',['10001','Tom'])
print(cursor.rowcount)
# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute("select * from user where id =%s",('10001',))
values = cursor.fetchall()
print(values)