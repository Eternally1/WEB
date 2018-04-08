from inputnews1 import ExSQL
import jieba
import datetime
import re
import jieba.posseg as pseg
from c2a import c2a
import os


class Record:
    """以每一条新闻数据记录为单位，进行要素提取"""
    
    def __init__(self, title, database=None):
        self.title = title
        self.database = database
        self.title_time = None
        self.news = None
        self.Nno = None
        self.cur_time = '2017-02-03'
        self.first_time = None
        self.place = None
        self.death = None
        self.loss = None
        self.entype = None
        self.tdeath = None
    
    def news_search(self, select='*'):
        """目前功能为限定4个字段"""  # TODO 根据需求修改为多个字段提取
        record = self.database.search_one(self.title, select)
        self.Nno, self.title, self.title_time, self.news = record
        return record
    
    def get_time(self):
        """
        获取最小时间，第一时间
        :return: 最小时间
        """
        try:
            if isinstance(self.title_time, datetime.date):
                self.title_time = self.title_time.strftime("%Y-%m-%d")
            self.first_time, self.cur_time = Record._rep(self.title_time, self.title+self.news)
            self.cur_time = self.cur_time.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
            return self.cur_time
        except:
            self.cur_time = ''
    
    def get_place(self):
        patern = re.compile('[^中国美国刊报道记者.｛2,4｝网]') #设定表达式，出去报刊，当加上nr 中含的地名影响
        string = re.findall(patern, self.title+self.news)  # 返回的是一个列表
        string = ''.join(i for i in string)
        f = pseg.cut(string)  # 词性标注
        result = []
        flag = []
        count = 0
        for word, cixin in f:
            if count == 0:
                if cixin == 'ns'  and word not in ["台风", "哥哥", "悉", "小乖乖"]:  # 弥补结巴分词不足
                    result.append(word)
                    flag.append(1)
                    count += 1
            else:
                if (cixin == 'ns' or cixin == 'nr') and word not in ["台风", "哥哥", "悉", "小乖乖"]:  # 弥补结巴分词不足
                    result.append(word)
                    flag.append(1)
                else:
                    if flag:
                        flag.append(0)
                    else:
                        flag = []
                if not all(flag):
                    self.place = ''.join(result)
                    return ''.join(result)
        if not result:
            self.place = ''
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
            renyuan = ['学生', '老人', '儿童', '消防人员', '工人', '老人', '消防员', '农民工', '韩国人', '女性','男性',  '旅客', '顾客', '师生', '乘客', '中国工人']
            etc = ['不同程度', '全部', '当场', '受', '已']
            #造成约40人失踪 事故死亡人数升至26人
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
            print(e)
    
    def get_loss(self):
        try:
            
            trigger = ['经济损失', '损失', '过火面积', '直接损失', '扑火费用', '扑火', '农作物受灾面积', '牲畜', '麦田', '房屋',
                       '森林面积', '折款', '桥梁受损', '损坏道路', '受灾面积', '受旱面积', '林木', '死亡大小牲畜', '桥梁', '重损', '轻损', '蔬菜大棚', '受灾人口',
                       '民房', '小麦受灾面积', '电杆', '塌方','房屋倒塌']
            shuzi = '一二三四五六七八九十百千万亿'
            loss_shu = ['十', '百', '千', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
            liangci = ['元', '美元', '人民币', '间', '元钱', '亩', '座', '头', '户', '公里', '公顷', '立方米', '只', '个', '人', '平方米']
            ext = ['约', '左右', '已达', '多达', '至少', '达', '多', '近', '估计', '估计在', '余']
            
            # 受伤12人  倒塌房屋902间', 匹配1：'农作物受灾面积75.17千公顷，匹配2：民房受损844户2731间
            # ；直接经济损失近200万元
            p1 = '|'.join([r'({触发词})+({ext})?([\d{中文数字}\.\d{中文数字}]+)({数})?(ext)?({单位量词})*'.format(触发词=each,
                                                                                            中文数字='|'.join(shuzi),
                                                                                            数='|'.join(loss_shu),
                                                                                            单位量词='|'.join(liangci),
                                                                                            ext='|'.join(ext))
                           for each in trigger])
            #265间房屋不同程度损坏
            p2 = '|'.join(
                [r'({触发词})+({ext})?([\d]+)({单位量词})+([\d]+)({单位量词})+'.format(触发词=each, 单位量词='|'.join(liangci),
                                                                            ext='|'.join(ext)) for each in
                 trigger])

            pattern1 = re.compile(p1)
            pattern2 = re.compile(p2)
            pattern3 = re.compile(r'\d*[间户坐]?[房屋桥梁][不同程度损坏]')
            result = list(set([i.group() for i in re.finditer(pattern1, self.news)])) + list(
                set([i.group() for i in re.finditer(pattern2, self.news)])) +list(
                set([i.group() for i in re.finditer(pattern3, self.news)]))
            self.loss = result
            return self.loss
        
        except Exception as e:
            print(e)
            self.loss = []
    
    @staticmethod
    def _rep(title_time, news):  # 数据库存放的时间，即传入报道时间，和正文内容
        try:
            # p = re.compile(r'\d{4}年\d{1,2}月\d{1,2}日|\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}')匹配年月日
            pattern = re.compile(r'\d{1,2}月\d{1,2}日|[一二三四五六七八九十]+月[一二三四五六七八九三十]+日|\d{1,2}月\d{1,2}日')
            cur_time = re.findall(pattern, news)
            
            for i in range(len(cur_time)):
                try:
                    temp = c2a([cur_time[i]])[0]
                    cur_time[i] = temp.replace('年', '-').replace('月', '-').replace('日', '').replace('号','')
                except:
                    cur_time[i] = cur_time[i].replace('年', '-').replace('月', '-').replace('日', '').replace('号', '')
            return Record._get_first_time(title_time, cur_time), Record._get_cur(title_time, cur_time)
        
        except Exception as e:
            print(e)
    
    @staticmethod
    def _get_cur(title_time, cur_time):
        """
        获取最小时间
        :param title_time:
        :param cur_time:
        :return:
        """
        m = []
        n = []
        time = []
        try:
            if not cur_time:
                return title_time
            
            for i in range(len(cur_time)):
                m.append(cur_time[i].split('-')[0])  # 保存月份
                n.append(cur_time[i].split('-')[1])  # 保存日子
            
            # 统一日期格式， 月份小于10，且长度不为2，即这种格式5-xx ->05-xx
            for i in range(len(m)):
                if len(m[i]) != 2 and int(m[i]) < 10:
                    m[i] = '0' + m[i]
            
            for j in range(len(n)):  # 天数小于10，且长度不为2，即这种格式xx-9 ->xx-09
                if len(n[j]) != 2 and int(n[j]) < 10:
                    n[j] = '0' + n[j]
            
            # 记录最小日期的位置
            for i in range(len(n)):
                time.append(int(m[i] + n[i]))  # 转换为整型比较大小
            
            # 找到最小日期的下标，
            mint = time[0]
            k = 0
            for i in range(1, len(time)):
                if time[i] < mint:
                    mint = time[i]
                    k = i
            
            # print("最小时间  ：" + title_time[:5] + m[k] + '-' + n[k])  # 组合输出
            
            return title_time[:5] + m[k] + '-' + n[k]
        
        except Exception as e:
            print(e)
    
    @staticmethod
    def _get_first_time(title_time, cur_time):  # findall返回的是一个列表
        """
        获取第一个时间
        :param title_time:
        :param cur_time:
        :return:
        """
        try:
            m = []
            n = []
            if not cur_time:
                return title_time
            
            A_time = cur_time[0].replace('年', '-').replace('月', '-').replace('日', '').replace('号', '')
            
            m.append(A_time.split('-')[0])  # 保存月份
            n.append(A_time.split('-')[1])  # 保存日子
            
            if int(m[0]) < 10 and len(m[0]) != 2:  # 只有前面没0的时候，长度才会小于2，所以同时判断，长度为2和小于10
                m[0] = '0' + m[0]
            
            if len(n[0]) != 2 and int(n[0]) < 10:
                n[0] = '0' + n[0]
            
            # print("第一个时间：" + title_time[:5] + m[0] + '-' + n[0])
            
            return title_time[:5] + m[0] + '-' + n[0]
        
        except Exception as e:
            print(e)
    
    def insert_to_database(self, tablename):
        """
        插入突发事件基本信息框架
        :return:
        """
        # print(type(self.cur_time))#str类型，需要转换成date
        print(self.cur_time)
        # print(self.Nno,self.title,self.news,self.cur_time,self.place,self.entype,self.loss,self.death,self.tdeath)
        with ExSQL(db=self.database.db, tablename=tablename) as tb:
            tb.insert_data('(Nno,Etitle,Edep,Stime,Eplace,ENtype,Eloss,Eharm,Etharm)',
                           (self.Nno, self.title, self.news, self.cur_time, self.place, self.entype,
                            ','.join(set(self.loss)), ','.join(set(self.death)), self.tdeath))
    def run(self):
        self.get_time()
        self.get_place()
        self.get_death()
        self.get_loss()
        self.insert_to_database("emergency_frame")  # TODO 改为形式参数


class NewFilter:
    """以每一个数据库表为单元，一次性进行新闻分类"""
    # 实例化的时候指定表的名字tablename
    def __init__(self, tablename, db='graduate_pro'):
        self.tablename = tablename
        self.db = db
        self.sql = ExSQL(db=self.db, tablename=self.tablename)
        self.file_read = None
        self.stopwords = None
        self.libs = None
        # self.file_out = []
        # self.file_out_with_sort = []
        self.sort = ["事故灾害", "公共卫生", "社会安全", "自然灾害"]#这个地方怎么改？？
    
    def _get_tabledate(self, select=None):
        """获取数据表内全部数据"""
        return self.sql.get_content(select=select)
    
    def _get_ready(self):
        """读取分类词，停用词，数据"""
        ''
        # path = r'C:\Users\letian\PycharmProjects\untitled\chou\demo'
        # path = r'C:\Users\zss0330816\Desktop\demo'
        path = os.getcwd()

        # files = [path + r'\text\地震.txt',
        #          path + r'\text\火灾.txt',
        #          path + r'\text\交通事故.txt',
        #          path + r'\text\恐怖袭击.txt',
        #          path + r'\text\食物中毒.txt']
        
        # def read_files(_files):   # 从数据库读取后无用了
        #     read = []
        #     for file in _files:
        #         with open(file, encoding="utf-8") as f:
        #             for l in f:
        #                 read.append(l)
        #     return read
        
        def read_stopwords(_file):
            """读取停用词"""
            sw_set = set()
            with open(_file, encoding='utf-8') as sw:
                for line in sw:
                    sw_set.add(line.strip('\n'))
            return sw_set
        
        def read_libs(_file):
            """读取分类特征词"""
            libraries = [[], [], [], [], []]
            with open(_file, encoding="utf-8") as f:
                index = -1
                for line in f:
                    strs = line.strip('\n').split(' ')
                    if '' in strs:
                        strs.remove('')
                    if len(strs) == 1:
                        index += 1
                    else:
                        libraries[index].append(strs)
            return libraries
        
        self.file_read = self._get_tabledate(select='title,content')
        # 这里修改了一下。
        self.stopwords = read_stopwords(os.path.join(path,'stopwords1.txt'))
        self.libs = read_libs(os.path.join(path,'lib.txt'))
    
    def run(self):
        self._get_ready()
        for line in self.file_read:
            strs = []
            title = line[0]
            line = ''.join(line)
            words = jieba.cut(line)
            # print(words)
            for word in words:
                if word not in self.stopwords and word != '':
                    strs.append(word)
            flag = 0
            for i in range(len(self.libs)):
                for l in self.libs[i]:
                    # if l[0] in strs and len((set(strs).union(set(l[1:len(l)]))) ^ (set(strs) ^ set(l[1:len(l)]))) > 0:
                    # self.file_out.append(line)
                    # self.file_out_with_sort.append(self.sort[i] + ' ' + line)   # self.sort[i]为事件分类
                    # record = Record(title, self.sql)
                    # record.news_search(select='Nno,Title,Time,News')
                    # record.entype = self.sort[i]
                    # record.run()
                    # print(record.Nno, record.entype, record.title, record.cur_time, record.place, record.death,
                    #       record.loss)
                    #
                    # flag = 1
                    # break
                    if len(set(l) & set(strs)) > 1:  # 获取新闻较多,但分类可能不够准确
                        #     self.file_out.append(line)
                        #     self.file_out_with_sort.append(self.sort[i] + ' ' + line)
                        record = Record(title, self.sql)
                        record.news_search(select='case_id,title,title_time,content')
                        record.entype = f.sort[i]
                        record.run()
                        print(record.Nno, record.entype, record.title, record.cur_time, record.place, record.death,
                              record.loss)
                        flag = 1
                        break
                if flag:
                    break


if __name__ == '__main__':
    # for table in ['地震', '火灾', '交通事故', '食物中毒', 'emergencies']:
    #     nf = NewFilter(table)
    #     nf.run()
    table = 'emergency'
    nf = NewFilter(table)
    nf.run()

