# @author: "QiuJunan"
# @date: 2018/3/17 10:35

from ExSQL import EXSQL         #导入EXSQL类
import datetime
import re
from c2a import c2a
import jieba.posseg as pseg
import jieba
import os

class Record(object):
    """
    解析一条案例，获取以下属性
    """
    def __init__(self,title,db=None):
        self.title = title      #案例名称（标题）[F]
        self.Nno = None         #案例编号【案例的id】[F]
        self.entype = None      #事件分类 [No]
        self.title_time = None  #事件标题中的年份，一般是具体到哪一年[F]
        self.least_time = None  #最小时间[F]
        self.first_time = None  #文中第一次出现的时间[F]
        self.place = None       #发生地点[F]
        self.news = None        #案例描述[F]
        self.death = None       #人员伤亡[F]
        self.loss = None        #经济损失[F]
        self.tdeath = None      #字符串形式展示人员伤亡情况[F]
        self.db = db            #EXSQL类的对象
        #还有一些属性，这里还没有涉及。

    def get_basic_info(self,select="*"):
        """
        获取一些基本的信息，也就是原始数据提供的一些基本信息，目前包含四个
        :param select: 默认为所有字段，可以设置
        :return: 无返回值
        """
        # select = 'case_id,title,content'   #具体需要根据数据库字段进行修改
        record = self.db.search_one_by_title(self.title,select)
        # print(record)
        if record:  #当获取到的时候才赋值
            self.Nno,self.title,self.news = record

    def get_time(self):
        """
        获取最小时间，第一时间并赋值。
        :return:
        """
        try:
            #看数据库中是否存在title_time,存在的话是int类型
            self.first_time,self.least_time = Record._get_times(self.title_time,self.title+self.news)
            if self.least_time:
                self.least_time = self.least_time.translate(str.maketrans('０１２３４５６７８９','0123456789'))
        except Exception as e:
            print("get_time Error:",e)
            #当没有最小时间的时候赋值为None。
            self.least_time = None

    @staticmethod
    def _get_times(title_time,news):
        """
        静态方法，传入标题时间和新闻内容，从新闻内容中提取最小时间和第一时间并返回
        :param title_time:
        :param news:
        :return:
        """
        try:
            pattern_year = re.compile('\d{4}年\d{1,2}月')
            years = re.findall(pattern_year,news)
            #如果title_time为空，且文中找到"XXXX年XX月"
            if years and not title_time:
                title_time = years[0][0:4]
            pattern = re.compile('\d{1,2}月\d{1,2}[日|号]|[一二三四五六七八九十]月[一二三四五六七八九十][日|号]')
            # 使用()将一整个部分括起来，然后添加次数，如果不需要捕获可以添加?:
            # pattern = re.compile('(?:\d{2,4}年){0,}\d{1,2}月\d{1,2}[日|号]|(?:\d{2,4}年){0,}[一二三四五六七八九十]月[一二三四五六七八九十][日|号]')
            times = re.findall(pattern,news)
            # print("title_time=",title_time,"文中出现的月日列表=",times)
            # 将时间中的年月日前面如果是数字，就转换成对应的阿拉伯数字，并替换为-
            for i in range(len(times)):
                try:
                    temp = c2a([times[i]])[0]
                    times[i] = temp.replace("年","-").replace("月","-").replace("日","").replace("号","")
                except:
                    times[i] = times[i] = temp.replace("年","-").replace("月","-").replace("日","").replace("号","")
            return Record._get_first_time(title_time,times),Record._get_least_time(title_time,times)

        except Exception as e:
            print("_get_times Error:",e)

    @staticmethod
    def _get_first_time(title_time,times):
        """
        获取第一个时间
        :param title_time: 标题中的时间,字符串
        :param cur_time: 事件中出现的 月-日 时间列表
        :return:
        """
        try:
            if not times:
                #如果文中没有出现时间，就返回标题中的时间
                return title_time

            if not title_time:
                # 如果没有年份，那么就不用在找月份了，没有意义。
                return None

            month = times[0].split("-")[0]  #保存月份和日
            day = times[0].split("-")[1]

            if int(month)<10 and len(month)!=2:
                month = '0'+month
            if int(day) < 10 and len(day) != 2:
                day = '0' + day

            # print("第一时间为:",str(title_time) + "-"+month +"-"+ day)
            return str(title_time) + "-"+month +"-"+ day

        except Exception as e:
            print("_get_first_time Error:",e)

    @staticmethod
    def _get_least_time(title_time,times):
        """
        获取最小时间
        :param title_time: 标题中的时间，可能为空
        :param times: 新闻中出现的  月-日 格式的时间列表
        :return:
        """
        try:
            if not times:
                # 如果文中没有出现时间，就返回标题中的时间
                return title_time

            if not title_time:
                # 如果没有年份，那么就不用在找月份了，没有意义。
                return None

            timelist = []

            for i in range(len(times)):
                # 保存所有的月份和日
                time = {}
                time["month"] = times[i].split("-")[0]
                time["day"] = times[i].split("-")[1]
                timelist.append(time)

            min_time = 10000
            for time in timelist:
                # 转换成标准格式，如0916表示9月16
                if int(time["month"])<10 and len(time["month"])!=2:
                    time["month"] = '0'+time["month"]
                if int(time["day"])<10 and len(time["day"])!=2:
                    time["day"] = '0'+time["day"]

                #转换成数字进行比较，如0916 和 0826直接进行大小比较即可
                if int(time["month"]+time["day"])<min_time:
                    min_time = int(time["month"]+time["day"])

            #左侧位数不够时，补0
            min_time  = str(min_time).zfill(4)
            # print("最小时间为:",str(title_time)+"-"+str(min_time)[:2]+"-"+str(min_time)[2:])
            return str(title_time)+"-"+str(min_time)[:2]+"-"+str(min_time)[2:]

        except Exception as e:
            print("_get_least_time Error:",e)

    def get_place(self):
        """
        获取发生地点信息
        :return:
        """
        # 换一个思路，找出含有这些词的字符串，然后从新闻中删除，然后在进行地名的处理
        pattern = re.compile('(?:中国|美国|报道|期刊|刊).{2,4}网')#设定表达式，除去报刊，当加上nr中含的地名影响
        string = re.findall(pattern,self.title+self.news)   #返回一个列表
        results = self.title+self.news
        if string:  # 如果存在匹配结果，那么就进行删除
            for i in string:
                # print(i)
                index = self.news.index(i)
                results = results[:index]+results[index+len(i):]
        f = pseg.cut(results)                                #词性标注
        result = []
        flag = []
        count = 0
        for word,cixin in f:
            if count == 0:    # 如果找到一个符合if条件的之后，count就会自增然后在下一次循环时就执行else语句
                if cixin == 'ns' and word not in ["台风","哥哥","悉","小乖乖"]:# 词性ns表示地名，弥补jieba分词不足
                    result.append(word)
                    flag.append(1)
                    count +=1
            else:
                if (cixin == 'ns' or cixin == 'nr') and word not in ["台风","哥哥","悉","小乖乖"]:  # nr表示人名
                    result.append(word)
                    flag.append(1)
                else:
                    if flag: # 如果找到符合条件的，就在flag后面添加一个标志位 0
                        flag.append(0)
                    else: # flag为空，表示没有搜寻到地名或者人名信息
                        flag = [1]  # 【S】我觉得这里应该是这样写
                if not all(flag):  # 如果flag中存在一个为0，则执行下面的语句。
                    self.place = "".join(result)
                    return

        if not result:
            self.place = ""
            return

    def get_death(self):
        try:
            siwang = ['死亡', '遇难', '溺死', '罹难', '死', '殉职', '丧生', '身亡', '撞死']
            shoushang = ['重伤', '受伤', '伤', '轻微伤', '轻伤']
            sishang = ['伤亡', '死伤']
            trigger = ['失踪', '受灾', '被困'] + siwang + shoushang + sishang
            # trigger = ['重伤', '受伤', '轻伤', '死亡', '遇难', '伤亡', '丧生', '失踪', '溺死', '罹难', '受灾', '死', '伤', '殉职', '轻微伤', '死伤']   修改本条代码需要注释掉death和harm
            shuzi = '零两俩一二三四五六七八九十百千万亿'
            shu = ['十', '百', '千', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
            liangci = ['人', '名', '例']
            renyuan = ['学生', '老人', '儿童', '消防人员', '工人', '老人', '消防员', '农民工', '韩国人', '女性', '男性', '旅客', '顾客', '师生', '乘客',
                       '中国工人']
            etc = ['不同程度', '全部', '当场', '受', '已']
            # 造成约40人失踪 事故死亡人数升至26人
            p1 = '|'.join(
                [r'([\d{中文数字}]+)(多|左右|余|约)?({数})?({量词})?({人员})?({其他})?{触发词}'.format(触发词=each, 量词='|'.join(liangci),
                                                                                    人员='|'.join(renyuan),
                                                                                    中文数字=shuzi, 数='|'.join(shu),
                                                                                    其他='|'.join(etc)) for
                 each in
                 trigger])
            p2 = '|'.join(
                [r'{触发词}([\d{中文数字}]+)(多|左右|余)?({数})?({量词})({人员})?'.format(触发词=each, 量词='|'.join(liangci),
                                                                          人员='|'.join(renyuan),
                                                                          中文数字=shuzi, 数='|'.join(shu)) for each in
                 trigger])
            pattern1 = re.compile(p1)
            pattern2 = re.compile(p2)

            result = list(set([i.group() for i in re.finditer(pattern1, str(self.news).replace(' ', ''))])) + list(
                set([i.group() for i in re.finditer(pattern2, str(self.news).replace(' ', ''))]))
            if result:
                # print(i + 1, result)
                result = list(set(c2a(result)))
                # print(i + 1, result)

                death = list(filter(lambda x: re.search('|'.join(siwang), x), result))
                harm = list(filter(lambda x: re.search('|'.join(shoushang), x), result))
                # print(i + 1, death)
                # print(i + 1, harm)
                # print('死', [re.search('\d+({数})?'.format(数='|'.join(shu)), i).group() for i in death])
                # print('伤', [re.search('\d+({数})?'.format(数='|'.join(shu)), i).group() for i in harm])
                death_nums = [re.search('\d+({数})?'.format(数='|'.join(shu)), i).group() for i in death]
                if death_nums:
                    death_num = max(map(int, death_nums))
                else:
                    death_num = 0
                harm_nums = [re.search('\d+({数})?'.format(数='|'.join(shu)), i).group() for i in harm]
                if harm_nums:
                    harm_num = max(map(int, harm_nums))
                else:
                    harm_num = 0
                self.tdeath = '死亡{0}人,受伤{1}人'.format(death_num, harm_num)
                self.death = death + harm
            else:
                result = 0
                self.tdeath = ''
                self.death = []
            return self.death

        except Exception as e:
            print("get_death Error:",e)

    def get_loss(self):
        """获取损失情况"""
        try:

            trigger = ['经济损失', '损失', '过火面积', '直接损失', '扑火费用', '扑火', '农作物受灾面积', '牲畜', '麦田', '房屋',
                       '森林面积', '折款', '桥梁受损', '损坏道路', '受灾面积', '受旱面积', '林木', '死亡大小牲畜', '桥梁', '重损', '轻损', '蔬菜大棚', '受灾人口',
                       '民房', '小麦受灾面积', '电杆', '塌方', '房屋倒塌']
            shuzi = '一二三四五六七八九十百千万亿'
            loss_shu = ['十', '百', '千', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
            liangci = ['元', '美元', '人民币', '间', '元钱', '亩', '座', '头', '户', '公里', '公顷', '立方米', '只', '个', '人', '平方米']
            ext = ['约', '左右', '已达', '多达', '至少', '达', '多', '近', '估计', '估计在', '余']

            # 受伤12人  倒塌房屋902间', 匹配1：'农作物受灾面积75.17千公顷，匹配2：民房受损844户2731间
            # ；直接经济损失近200万元
            # 我这里修改了一下，可以通过具体的例子测试一下。
            p1 = '|'.join([r'({触发词})+({ext})?(\d|{中文数字}|\.)+(ext)?({数})?(ext)?({单位量词})?'.format(触发词=each,
                                                                                                  中文数字='|'.join(shuzi),
                                                                                                  数='|'.join(loss_shu),
                                                                                                  单位量词='|'.join(
                                                                                                      liangci),
                                                                                                  ext='|'.join(ext))
                           for each in trigger])
            # 265间房屋不同程度损坏
            p2 = '|'.join(
                [r'({触发词})+({ext})?([\d]+)({单位量词})+([\d]+)({单位量词})+'.format(触发词=each, 单位量词='|'.join(liangci),
                                                                            ext='|'.join(ext)) for each in
                 trigger])

            pattern1 = re.compile(p1)
            pattern2 = re.compile(p2)
            pattern3 = re.compile(r'\d*[间户坐]?(房屋|桥梁)(不同程度)*(损坏|坍塌)')
            result = list(set([i.group() for i in re.finditer(pattern1, self.news)])) + list(
                            set([i.group() for i in re.finditer(pattern2, self.news)])) + list(
                             set([i.group() for i in re.finditer(pattern3, self.news)]))
            self.loss = result
            return self.loss

        except Exception as e:
            print("get_loss Error:",e)
            self.loss = []

    def insert_to_database(self,tablename):
        """在数据获取完成之后，插入到具体的数据表中"""
        with EXSQL(tablename = tablename)as db:
            # 分别表示案例的编号、案例名称、案例描述、最小时间、发生地点、案例类型、损失情况、伤亡情况、伤亡情况
            db.insert_data('(Nno,Etitle,Edep,Stime,Eplace,ENtype,Eloss,Etharm)',
                           (self.Nno, self.title, self.news, self.least_time=='NULL' if self.least_time==None else self.least_time
                            , self.place, self.entype, ','.join(self.loss), self.tdeath))

    def run(self):
        """开始进行数据的抽取和插入到数据库表中"""
        self.get_time()
        self.get_place()
        self.get_death()
        self.get_loss()
        # 这里填写的是提取的信息存储的数据库
        self.insert_to_database("emergency_frame3")

class NewFilter:
    """对新闻进行分类，同时存储到不同的表中去"""
    def __init__(self,tablename):
        self.tablename = tablename              # 不同类型案例存储在不同的表中去
        self.db = EXSQL(tablename=tablename)    # 实例化EXSQL()对象
        self.file_read = None
        self.stopwrods = None
        self.libs = None
        self.sorts = ['事故灾害','公共卫生','社会安全','自然灾害']
        self.contents = None   #用于存储数据库表中的内容

    def _get_table_data(self,select=None):
        """获取数据表内全部数据"""
        return self.db.get_content(select=select)
        # self.contents = self.db.get_content(select=select)

    def _get_ready(self):
        """设置停用词，分类特征词，还有获取案例内容"""
        path = os.getcwd()
        print("当前路径为:",path)

        def read_stopwords(_file):
            """读取停用词"""
            sw_set = set()
            with open(_file,'r',encoding='utf-8')as f:
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

        # file_read是一个产生器，每一项代表一个title content的二元组
        self.file_read = self._get_table_data(select='title,content') # 获取案例的标题和内容
        self.stopwrods = read_stopwords(os.path.join(path,'stopwords1.txt'))
        # 注意libs的结构
        self.libs = read_libs(os.path.join(path,'lib.txt'))

    def run(self):
        """开始进行运行，分类，以及放在不同的数据库表中"""
        self._get_ready()
        count = 0
        # print(type(self.file_read))
        for line in self.file_read:
            count +=1
            print("处理第%d条数据.........." % count)
            # line是一个含2个元素的元组，分别为title和内容
            strs = []
            title = line[0]
            line = title+""+line[1]
            words = jieba.cut(line)  # 分词
            for word in words:
                if word not in self.stopwrods and word != "": # 将不是停用词和不为空的词放入strs列表中
                    strs.append(word)
            flag = 0
            # print(len(self.libs))
            for i in range(len(self.libs)):
                for l in self.libs[i]: # libs每一项都是一个列表中嵌套这列表
                    # l代表的是列表，也就是每一行
                    if(len(set(l) & set(strs)) > 1):
                        print(set(l) & set(strs))   # 看strs中和分类关键词中的词语的交集
                        record = Record(title,self.db)  # 实例化Record
                        record.get_basic_info(select='case_id,title,content') #获取一些案例的基本信息
                        # 设置事件类型分类
                        record.entype = self.sorts[i]
                        print("事件类型为",record.entype)
                        # 从新闻体中获取内容
                        record.run()
                        # print(record.Nno,record.entype,record.title,record.least_time,record.place,record.death,record.loss)
                        flag = 1
                        break
                # 如果已经找到分类的话就不需要再向下找
                if flag:
                    break
if __name__ == '__main__':
    # record = Record('２００３年辽宁孟家沟煤矿瓦斯爆炸事件',EXSQL("test_case"))
    # record.get_basic_info()
    # record.get_time()
    # record.get_place()
    # record.get_death()
    # record.get_loss()
    # print("最小时间=",record.least_time," 第一时间=",record.first_time,"地名=",record.place)
    # print(record.Nno,record.title,record.news,record.title_time)
    # print("伤亡情况:",record.tdeath,record.death)
    # print("损失情况:",record.loss)
    # 这里是存储原始数据的数据库
    # 只需要在这里修改原始数据的表名，之后数据会写入emergency_frame1中
    newfilter = NewFilter('mai_ni_zhe')
    newfilter.run()