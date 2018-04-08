# @author: "QiuJunan"
# @date: 2018/4/3 10:40
# 对一篇指定的文章进行分类，是从NF34中分离出来的一个模块
import os
from ExSQL import EXSQL
import jieba

class NFilter(object):
    def __init__(self,titlename):
        self.file_read = None   # 要进行分类的article
        self.stopwords = None   # 停用词
        self.libs =None         # 词表
        self.titlename = titlename
        self.sql = EXSQL('emergency')    # 将EXSQL实例化对象存储为sql，这里传入数据库表名
        self.entype =None           # 这篇文章所属类型
        self.sorts = ['事故灾害','公共卫生','社会安全','自然灾害']


    def _get_ready(self):
        """设置停用词，分类特征词，还有获取案例内容"""
        path = os.getcwd()
        print("当前路径为:",path)

        def read_stopwords(_file):
            """读取停用词"""
            sw_set = set()
            # print(_file)
            with open(_file,'r',encoding='utf-8')as f:
                print(f)
                for line in f:
                    sw_set.add(line.strip("\n"))
            print("停用词集合为",sw_set)
            return sw_set

        def read_libs(_file):
            """读取分类特征词"""
            libraries = [[],[],[],[]]
            with open(_file,'r',encoding='utf-8')as f:
                index = -1
                for line in f:
                    strs = line.strip('\n').split(" ")
                    if "" in strs:
                        strs.remove("")
                    if len(strs) == 1:  # 大类的名称
                        index +=1
                    else:
                        # strs是列表
                        libraries[index].append(strs)
            print("分类特征词：",libraries)
            return libraries

        def get_one_article(title,select):
            return self.sql.search_one_by_title(title,select)

        self.file_read = get_one_article(self.titlename,'title,content')
        self.stopwords = read_stopwords(os.path.join(path, 'stopwords1.txt'))
        # 注意libs的结构
        self.libs = read_libs(os.path.join(path, 'lib.txt'))

    def run(self):
        """对该article进行分类"""
        self._get_ready()
        strs = []
        title = self.file_read[0]       # 获取文章标题
        article = title+" "+self.file_read[1]   # 案例标题加内容
        words = jieba.cut(article)          # 分词
        for word in words:
            if word not in self.stopwords and word != "": # 将不是停用词和不为空的词放入strs列表中
                strs.append(word)
        flag = 0        # 设置一个标志，用于判断什么时候停止进行分类
        for i in range(len(self.libs)): # 长度为4，主要是四大类
            for index,l in enumerate(self.libs[i]): # l表示每一大类中的第一行
                # l代表的是列表，也就是每一行
                if(len(set(l) & set(strs)) > 1):
                    print(set(l) & set(strs))   # 看strs中和分类关键词中的词语的交集
                    # 设置时间类型分类
                    self.entype = self.sorts[i]
                    # 小类也可以输出来
                    print("所属小类为:",self.libs[i][index][0])
                    # print("i的值为",i,"**********")
                    flag = 1        # 找到所属类型就进行停止，然后跳出里层for循环
                    break
            # 如果已经找到分类的话就不需要再向下找，缺点是可能分类不准确
            if flag:
                break

if __name__ == '__main__':
    nf = NFilter('青海退耕还林还草工程')
    nf.run()
    print(nf.entype)