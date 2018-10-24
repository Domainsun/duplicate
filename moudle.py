# coding:utf-8
from gensim import corpora, similarities, models
import os
from collections import defaultdict
import codecs
import json
import jieba

documents = []
"""句子相似性"""
f = codecs.open("A.txt", 'rb', "utf-8")
for line in f:
    if len(line) == 0 or line == '\n':
        continue
    seg_list = []
    it = jieba.cut(line, cut_all=False)
    for word in it:
        seg_list.append(word)
    documents.append(seg_list);
f.close()

'''stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]'''
# 去掉只出现一次的单词
'''frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]'''
texts = documents;
# texts的结构必须是[["你好,好久不见"],["你好,好久不见"]]
dictionary = corpora.Dictionary(texts)  # 生成词典# -*- coding: utf-8 -*-
dictionary.save('mydict.dic')  # store the dictionary, for future reference
corpus = [dictionary.doc2bow(list(text)) for text in texts]
corpora.MmCorpus.serialize('corpus.mm', corpus)  # store to disk, for later use
# 首先加载语料库
if os.path.exists('mydict.dic') and os.path.exists('corpus.mm'):
    dictionary = corpora.Dictionary.load('mydict.dic')
    corpus = corpora.MmCorpus('corpus.mm')
    print('used files generated from string2vector')
else:
    print('please run string2vector firstly')

# 创建一个model
tfidf = models.TfidfModel(corpus=corpus)
tfidf.save('model.tfidf')
# 使用创建好的model生成一个对应的向量
vector = tfidf[corpus[0]]
print(vector)
# 序列化
tfidf_corpus = tfidf[corpus]
corpora.MmCorpus.serialize('tfidf_corpus.mm', tfidf_corpus)

# lsi
lsi = models.LsiModel(corpus=tfidf_corpus, id2word=dictionary, num_topics=2)
lsi_corpus = lsi[tfidf_corpus]
lsi.save('model.lsi')
corpora.MmCorpus.serialize('lsi_corpus.mm', lsi_corpus)
print(
    'LSI Topics:')
lsitopics = lsi.print_topics(20)
print(json.dumps(lsitopics, ensure_ascii=False))

# lda
lda = models.LdaModel(corpus=tfidf_corpus, id2word=dictionary, num_topics=2)
lda_corpus = lda[tfidf_corpus]
lda.save('model.lda')
corpora.MmCorpus.serialize('lda_corpus.mm', lda_corpus)
print(
    'LDA Topics:')
ldatopics = lda.print_topics(20)
print(
    json.dumps(ldatopics, ensure_ascii=False))
