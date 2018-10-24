# coding:utf-8
from gensim import corpora, similarities, models
import os
import jieba

# 首先加载语料库
if os.path.exists('lsi_corpus.mm') and os.path.exists('mydict.dic'):
    dictionary = corpora.Dictionary.load('mydict.dic')
    corpus = corpora.MmCorpus('lsi_corpus.mm')
    model = models.LsiModel.load('model.lsi')
    print(
    'used files generated from topics')
else:
    print(
    'please run topics firstly')

index = similarities.MatrixSimilarity(corpus)
index.save('lsi_similarity.sim')

document = u'当地时间18时许，习近平在第71届联合国大会主席汤姆森和联合国秘书长古特雷斯陪同下步入万国宫大会厅，全场起立，热烈鼓掌欢迎。'
bow_vec = dictionary.doc2bow(jieba.lcut(document))
lsi_vec = model[bow_vec]
sims = index[lsi_vec]
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(
sims)

