# @author: "QiuJunan"
# @date: 2018/3/14 16:12
# 功能：将目前的txt数据根据标题和内容插入到数据库
import pymysql
import os
# txt文件所在目录
METADATA_FOLDER = r"C:\others\doc\teamAndPersonInfo\GraduationProject\DataSet\METADATA_ALL"

class EXSQL:
    #这里我的初始化都是我自己的默认值
    def __init__(self,tablename='emergency',user="root",password="root",db="graduate_pro"):
        #打开数据库连接，赋值给conn变量
        self.db = pymysql.connect(host="127.0.0.1",port=3306,user=user,password=password,db=db,charset="utf8mb4")
        self.tablename = tablename
        #创建一个游标对象
        self.cursor = self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc, value, tb):
        if exc:
            self.cursor.rollback()
        else:
            self.db.commit()

    def insert_data(self,field,value):
        """
        注意数据以元组的形式传入，field以字符串的形式传入
        :param field: '(title,content)'
        :param value: ('标题','加速企业创新能力发展')
        :return:
        """
        sql = "insert into %s  %s  values %s;"% (self.tablename,field,value)
        # print("insert_data:",sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            #发生错误则回滚
            print("insert_data Error:",e)
            self.db.rollback()

    def search_one_by_title(self,title,select="*"):
        """
        根据标题获取一条案例内容
        :param title: 案例标题（名称）
        :param select: 默认为获取这条案例的全部字段 ('title','title_time')
        :return: 返回获取到的一条数据（元组）
        注意这里的like后面的%s需要引号引起来。
        """
        sql = "select %s from %s where title like '%%%s%%'" % (select,self.tablename,title)
        print(sql)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as e:
            print("search_one_by_title error:",e)

    def get_content(self,select=None):
        """获取当前表的全部数据,存在列表过大的情况吧，可以改成生成器试试"""
        if not select:
            sql = "select * from %s" % self.tablename
            self.cursor.execute(sql)
        else:
            sql = "select %s from %s" % (select,self.tablename)
            print(sql)
            self.cursor.execute(sql)
        # 判断一下是否存在数据，若不存在，就返回空
        if self.cursor.rowcount:
            for case in self.cursor.fetchall():
                yield case
            # return self.cursor.fetchall()
        else:
            print("%s中没有符合条件的数据" % self.tablename)
            return None


    def update_data(self,field,value):
        pass
    #目前使用不到这方面的方法。


if __name__ == '__main__':
    # 这里将数据写入了数据库
    exsql = EXSQL("root","root","graduate_pro","emergency")
    # for value in write_to_mysql(METADATA_FOLDER):
    #     field = '(title,content)'
    #     exsql.insert_data(field,value)

    #emergency数据库表数据进行测试
    #测试search_one_by_title
    ret = exsql.search_one_by_title('生舆情：“时年夜饭”让年味打')
    case_id,title,news,title_time = ret
    print(ret)
