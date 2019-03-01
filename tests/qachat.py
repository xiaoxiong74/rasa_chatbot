# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: qachat.py
@Software: PyCharm
@time: 2019/2/27 10:38
@desc:
'''
from gensim import corpora, models, similarities
import jieba
import csv
import pandas as pd

texts1 = []
texts2 = []
with open('/home/pywork/kf7899/datas/qa_bot.csv','r',encoding='gbk') as csvfile:
    reader = csv.reader(csvfile)
    texts1 = [row[0]for row in reader]
with open('/home/pywork/kf7899/datas/qa_bot.csv','r',encoding='gbk') as csvfile:
    reader = csv.reader(csvfile)
    texts2 = [row[1]for row in reader]


def stopwordslist(filepath):
    wlst = [w.strip() for w in open(filepath,'r',encoding='utf8').readlines()]
    return wlst


stop_words = stopwordslist('/home/pywork/kf7899/rasa_chatbot_cn/data/stop_words.txt')


def seg_sentence(sentence,stop_words):
    sentence_seged = jieba.cut(sentence.strip())
    # sentence_seged = set(sentence_seged)
    outstr = ''
    for word in sentence_seged:
        if word not in stop_words:
            if word != '\t':
                outstr += word
                outstr += ' '

    return outstr.split(' ')


# 1、将【文本集】生成【分词列表】
texts = [seg_sentence(text, stop_words) for text in texts1]
# 2、基于文本集建立【词典】，并提取词典特征数
dictionary1 = corpora.Dictionary(texts)
feature_cnt = len(dictionary1.token2id)
# 3、基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】
corpus = [dictionary1.doc2bow(text) for text in texts]
# 4、使用【TF-IDF模型】处理语料库
tfidf = models.TfidfModel(corpus)

def get_qa(query):
    # print("********************************************************************************")
    keyword = query
    # if keyword == 'quit' or keyword == 'exit':
    #     break

    # 5、同理，用【词典】把【搜索词】也转换为【稀疏向量】
    kw_vector = dictionary1.doc2bow(jieba.lcut(keyword))
    # 6、对【稀疏向量集】建立【索引】
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    # 7、相似度计算
    sim = index[tfidf[kw_vector]]
    # dictionary = dict(zip(texts1,sim))
    # list1= sorted(dictionary.items(),key=lambda x:x[1])
    # print(list1)
    dictionary = {}
    result = []
    for i in range(len(sim)):
        temp = []
        # print('keyword 与 text%d 相似度为：%.2f' % (i + 1, sim[i]),texts1[i])
        if sim[i] >= 0.6:
            temp.append(sim[i])
            temp.append(texts1[i])
            temp.append(texts2[i])
            result.append(temp)
    df = pd.DataFrame(result, columns=['相似度分数', '问题','答案'])
    df1 = df.sort_values('相似度分数', ascending=False)
    # print(df1)
    if (len(df1)) >= 1:
        # print("相似度分数:",df1.loc[0]['相似度分数'],"相似问题:",df1.loc[0]['问题'],"答案:",df1.loc[0]['答案'])
        # print("--Score--:", df1.loc[0]['相似度分数'])
        # print("**小智**:", df1.loc[0]['答案'])
        return df1.loc[0]['答案']
    else:
        return "未找到答案"
