# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP


# 这里是自动摘要的代码

#//这里填注册后获得的key
nlp = BosonNLP('rTNpHME1.24458.d0fOMRwoKodM')#rTNpHME1.24458.d0fOMRwoKodM

contents = []

# s = '''中新网北京3月16日电 16日上午，十三届全国人大一次会议将举行代表团全体会议，审议监察法草案修改稿，关于批准国务院机构改革方案的决定草案，第十三届全国人大一次会议选举和决定任命的办法草案。
# 下午3时，代表团全体会议酝酿协商中华人民共和国主席、副主席的人选，中华人民共和国中央军事委员会主席的人选，全国人大常委会委员长、副委员长、秘书长的人选。
# 此外，上午10时，十三届全国人大一次会议新闻中心将在梅地亚中心多功能厅举行记者会，邀请教育部部长陈宝生就“努力让每个孩子都能享有公平而有质量的教育”相关问题回答中外记者提问。'''
# temp = nlp.summary('', s, word_limit=0.3, not_exceed=0).strip('\n')
# print(temp)

# with open(r'E:\soft\pycharm\workplace\yunyibei-emergency\text.txt', encoding='utf-8') as con:
#     for line in con:
#         #//这一句是生成摘要的代码，line就是原始文本，具体参数意思网上有
#         temp = nlp.summary('', line, word_limit=100, not_exceed=1).strip('\n')
#         print(temp,line)
#         xl = temp.split('\n')
#         y = ''.join(xl)
#
#         contents.append(y)

# 完整的参数调用如下：
# result = nlp.summary(title, content, word_limit=0.3, not_exceed=0)
# 修改标题为该文章标题，如下：
# title = '前优酷土豆技术副总裁黄冬加盟芒果TV任CTO'
# result = nlp.summary(title, content, word_limit=0.3, not_exceed=0)
# 修改word_limit选项为百分之二十，如下：
# result = nlp.summary(title, content, word_limit=0.2, not_exceed=0)
# 修改word_limit选项为具体字数200时，如下：
# result = nlp.summary(title, content, word_limit=200, not_exceed=0)
# 修改no_exceed选项为严格不超出字数限制时，如下：
# result = nlp.summary(title, content, word_limit=0.3, not_exceed=1)

# with open(r'E:\soft\pycharm\workplace\yunyibei-emergency\text.txt', 'wb') as cont:
#     for line in contents:
#         cont.write(line.encode())
#         cont.write(b'\n')#二进制写
#print(contents)

with open(r'E:\soft\pycharm\workplace\yunyibei-emergency\text.txt', 'r') as f:
    data = f.read().replace('\n', '')
    print(data)
    print('\n')
    temp = nlp.summary('', content=data, word_limit=0.2, not_exceed=0).replace('\n', '')
    print(temp)

#针对堆垛机设备在运行过程中呈现的复杂性、不确定性等问题，设计了基于故障树和贝叶斯网络的混合诊断专家系统。 概率计算混合诊断机制是一种快速诊断堆垛机的可行方式。