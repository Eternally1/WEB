# @author: "QiuJunan"
# @date: 2018/4/6 10:37
# 使用word2vec找相似词

# 使用下面这两句不会再出现警告信息，但是还是会出错
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim
model = gensim.models.Word2Vec.load(r'C:\others\doc\zhwiki_model\word2vec_gensim')  # 读取模型
# print(model)
# shi_gu_zai_hai = [['战争','暴力'],['工矿','商贸'],['交通运输','安全事故'],['城市','生命线','事故'],['通讯','安全事故'],
#                   ['环境污染','生态','破坏'],'严重火灾','中毒事件','急性化学事故','放射事故','医药事故','探险遇难','旅游事故']
# 只留下特征名词，去掉事故这些词,因为数据集中已经是突发事件的，所以只要和这些词相关，可能就是事故类
accident = [['战争','暴力'],['工矿','商贸'],['交通运输'],['城市','生命线'],['通讯'],
                  ['环境污染','生态'],'火灾','中毒','化学','放射','医药','探险','旅游']
public_health = [['传染病','疫情'],['群体性','疾病'],'食品安全',['动物','疫情'],['健康','生命安全']]
natural_disater = [['水旱'],'气象','地震','地质','海洋','生物',['森林','草原','火灾'],'宇宙']
social_safety = ['恐怖袭击','刑事',['经济','安全'],['涉外','突发'],'群体性',['民族','宗教'],['骚乱','暴动']]   # 7类

for i in social_safety:
    # print(model.most_similar(i, topn=15))
    temp = model.most_similar(i, topn=15)
    for item in temp:
        print(item[0],end= " ")
    print("\n")