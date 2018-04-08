#from gensim.models.word2vec import Word2Vec, LineSentence
import gensim
model = gensim.models.Word2Vec.load(r'C:\others\doc\zhwiki_model\word2vec_gensim')  # 读取模型
print(model)        #模型训练的维度是200维度，窗口大小，默认为5, alpha =0.25. vocabulary=568985

print(model.most_similar('武汉', topn=10))  # 相关文本，topn为前几位model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,

print(model['武汉'])  # 向量值,也可以用model.wv['武汉']
print(model.similarity('男', '女'))  # 计算的是余弦相似度
print(model.doesnt_match("武汉 湖北 河南".split()))  # 筛选相关度最低的内容
list1 = ['the', 'cat', 'is', 'walking', 'in', 'the', 'bedroom']
list2 = ['the', 'dog', 'was', 'running', 'across', 'the', 'kitchen']

#计算两个集合之间的相似度
print(model.n_similarity(list1, list2))#n_similarity,接受的参数是什么形式？，列表形式的字符串
