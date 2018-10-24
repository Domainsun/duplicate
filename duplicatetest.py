import logging
from gensim import corpora, models, similarities
def similarity(datapath, querypath, storepath):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    class MyCorpus(object):
        def __iter__(self):
            for line in open(datapath,encoding='utf-8'):
                yield line.split()

    Corp = MyCorpus()
    dictionary = corpora.Dictionary(Corp)
    corpus = [dictionary.doc2bow(text) for text in Corp]

    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]

    q_file = open(querypath, 'r',encoding='utf-8')
    query = q_file.readline()
    q_file.close()
    vec_bow = dictionary.doc2bow(query.split())
    vec_tfidf = tfidf[vec_bow]

    index = similarities.MatrixSimilarity(corpus_tfidf)
    sims = index[vec_tfidf]

    similarity = list(sims)

    sim_file = open(storepath, 'w')
    for i in similarity:
        sim_file.write(str(i)+'\n')
    sim_file.close()
# similarity('A.txt','B.txt','C.txt')

import difflib

a = open('A.txt', encoding='utf-8',).readlines()
b = open('B.txt', encoding='utf-8').readlines()
diff = difflib.ndiff(a, b)

print(diff)
for d in diff:
    print(d)
# sys.stdout.writelines(diff)