# @author: "QiuJunan"
# @date: 2018/3/14 16:12
# 功能：将目前的txt数据根据标题和内容插入到数据库
import pymysql
import os
# txt文件所在目录
METADATA_FOLDER = r"C:\others\doc\teamAndPersonInfo\GraduationProject\DataSet\emergency_analysis1"

class EXSQL:
    def __init__(self,user="root",password="",db="",tablename=None):
        #打开数据库连接，赋值给conn变量
        self.conn = pymysql.connect(host="127.0.0.1",port=3306,user=user,password=password,db=db,charset="utf8mb4")
        self.tablename = tablename
        #创建一个游标对象
        self.cursor = self.conn.cursor()

    def insert_data(self,field,value):
        """
        注意数据以元组的形式传入，field以字符串的形式传入
        :param field: '(title,content)'
        :param value: ('标题','加速企业创新能力发展')
        :return:
        """
        sql = "insert into %s  %s  values %s;"% (self.tablename,field,value)
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            #发生错误则回滚
            self.conn.rollback()


def write_to_mysql(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            #获取文件名作为标题
            title = os.path.splitext(file)[0]
            # 将文件名中的英文引号换成空格
            file = file.replace('"'," ")
            file = os.path.join(root, file).replace("\\", '/')
            # print(file,title)
            with open(file,'r',encoding="utf-8")as f:
                try:
                    content = f.read()
                except UnicodeDecodeError:
                    with open(file, 'r', encoding="gbk")as f:
                        content = f.read()
            yield (title,content)



if __name__ == '__main__':
    #这里将数据写入了数据库
    # 需要修改两部分内容，一个是TXT文件所在目录，然后另一个就是数据库表的名字
    exsql = EXSQL("root","root","graduate_pro","ying_ji_fen_xi1")
    for value in write_to_mysql(METADATA_FOLDER):
        # print(value)
        field = '(title,content)'
        exsql.insert_data(field,value)