# -*- coding: utf-8 -*-
"""
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: qachat.py
@Software: PyCharm
@time: 2019/2/27 10:38
@desc: 一个最简单的Q&A问答，快速实现，未优化重复模块、结构、模型

qa_bot.csv结构：
-------------------------------------------------------------------------------------
| question                     | answer
-------------------------------------------------------------------------------------
| windows命令行关机             | 打开cmd-> 输入：shutdown(直接关机)   shutdown -r(重启)
-------------------------------------------------------------------------------------
| windows下查看ip地址           | 打开cmd-> 输入：ipconfig
-------------------------------------------------------------------------------------
"""


from gensim import corpora, models, similarities
import jieba
import csv
import pandas as pd


def stopwordslist(filepath):
    wlst = [w.strip() for w in open(filepath,'r',encoding='utf8').readlines()]
    return wlst


def seg_sentence(sentence,stop_words):
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        if word not in stop_words:
            if word != '\t':
                outstr += word
                outstr += ' '

    return outstr.split(' ')


# 0、获取数据
data = pd.read_csv('/home/pywork/kf7899/datas/qa_bot.csv', encoding='gbk')
Question = data["Question"].tolist()
Answer = data["Answer"].tolist()
stop_words = stopwordslist('/home/pywork/kf7899/rasa_chatbot_cn/data/stop_words.txt')
# 1、将【文本集】生成【分词列表】
texts = [seg_sentence(text, stop_words) for text in Question]
# 2、基于文本集建立【词典】，并提取词典特征数
dictionary1 = corpora.Dictionary(texts)
feature_cnt = len(dictionary1.token2id)
# 3、基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】
corpus = [dictionary1.doc2bow(text) for text in texts]
# 4、使用【TF-IDF模型】处理语料库
tfidf = models.TfidfModel(corpus)


def get_qa(query):
    keyword = query
    # 5、同理，用【词典】把【搜索词】也转换为【稀疏向量】
    kw_vector = dictionary1.doc2bow(jieba.lcut(keyword))
    # 6、对【稀疏向量集】建立【索引】
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    # 7、相似度计算
    sim = index[tfidf[kw_vector]]
    result = []
    for i in range(len(sim)):
        temp = []
        # 只取相似度大于0.6的
        if sim[i] >= 0.8:
            temp.append(sim[i])
            temp.append(Question[i])
            temp.append(Answer[i])
            result.append(temp)
    df = pd.DataFrame(result, columns=['相似度分数', '问题','答案'])
    df1 = df.sort_values('相似度分数', ascending=False)
    # print(df1)
    if (len(df1)) >= 1:
        return df1.loc[0]['答案']
        # print(df1.loc[0]['答案'],df1.loc[0]['相似度分数'])
    else:
        return "未找到答案"
