# @author: "QiuJunan"
# @date: 2018/4/6 10:59

# 一个简答的测试
import gensim

sentences = [['first','sentence'],['second','sentence','is']]

# 模型训练
model = gensim.models.Word2Vec(sentences,min_count=1)
# min_count,频数阈值，大于等于1的保留
# size，神经网络 NN 层单元数，它也对应了训练算法的自由程度
# workers=4，default = 1 worker = no parallelization 只有在机器已安装 Cython 情况下才会起到作用。如没有 Cython，则只能单核运行。

print(model)
print("***********相似度比较************")
print(model.similarity('first','second'))
# 一个词的向量？？
print("**********查看词的向量***************")
print(model['first'])