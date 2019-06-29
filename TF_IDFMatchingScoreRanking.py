# -*- coding: utf-8 -*-
"""## Imports"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words

import nltk
import os
import string
import numpy as np
import copy
import pandas
import pandas as pd
import pickle
import re
import math
import csv
import time
import psutil

def readfile(Input):
    start_time = time.time()

    """# Preprocessing"""

    def convert_lower_case(data):
        return np.char.lower(data)

    def remove_stop_words(data):
        stop_words = stopwords.words('english')
        words = word_tokenize(str(data))
        new_text = ""
        for w in words:
            if w not in stop_words and len(w) > 1:
                new_text = new_text + " " + w
        return new_text

    def remove_punctuation(data):
        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        for i in range(len(symbols)):
            data = np.char.replace(data, symbols[i], ' ')
            data = np.char.replace(data, "  ", " ")
        data = np.char.replace(data, ',', '')
        return data

    def remove_apostrophe(data):
        return np.char.replace(data, "'", "")

    def stemming(data):
        stemmer= PorterStemmer()
        
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            new_text = new_text + " " + stemmer.stem(w)
        return new_text

    def convert_numbers(data):
        tokens = word_tokenize(str(data))
        new_text = ""
        for w in tokens:
            try:
                w = num2words(int(w))
            except:
                a = 0
            new_text = new_text + " " + w
        new_text = np.char.replace(new_text, "-", " ")
        return new_text

    def preprocess(data):
        data = convert_lower_case(data)
        data = remove_punctuation(data) #remove comma seperately
        data = remove_apostrophe(data)
        data = remove_stop_words(data)
        data = convert_numbers(data)
        data = stemming(data)
        data = remove_punctuation(data)
        data = convert_numbers(data)
        data = stemming(data) #needed again as we need to stem the words
        data = remove_punctuation(data) #needed again as num2word is giving few hypens and commas fourty-one
        data = remove_stop_words(data) #needed again as num2word is giving stop words 101 - one hundred and one
        return data

    alpha = 0.3
    arrayURL = []
    arrayList = []
    CutarrayList = []

    URLDatas = []
    arrayURLDatas = []
    CutarrayListDatas = []
    times = ''
    timesFile = []
    CountBinay = []
    number = []
    url = 100
    URL = pandas.read_csv('url1000.csv')
    # for i in range(0,len(URL)):
    for i in range(0,url):
        arrayURL.append(URL['url'][i])

    with open('DataSets.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            arrayList.append(row)

    # for x in range(0,len(arrayList)):
    #     print(len(arrayList))
    #     print(arrayList[x])
    #     print('*******************')

    DF = {}

    for i in range(0,url):
        tokens = arrayList[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}

    for i in DF:
        DF[i] = len(DF[i])

    # print(DF)
    # DF

    total_vocab_size = len(DF)

    total_vocab_size

    total_vocab = [x for x in DF]

    # print([x for x in DF])
    # print(total_vocab[:20])

    def doc_freq(word):
        c = 0
        try:
            c = DF[word]
        except:
            pass
        return c

    """### Calculating TF-IDF for body, we will consider this as the actual tf-idf as we will add the title weight to this."""

    doc = 0

    tf_idf = {}

    for i in range(0,url):
        
        tokens = arrayList[i]
        
        counter = Counter(tokens)
        words_count = len(tokens)

        # print('tokens : ', tokens)
        # print('counter : ', counter)
        # print('words_count : ', words_count)
        
        for token in np.unique(tokens):
            
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = np.log((url+1)/(df+1))
            
            tf_idf[doc, token] = tf*idf

        doc += 1

    # print(type(tf_idf))
    # print(len(tf_idf))
    # print(tf_idf[(0,Input)])

    # tf_idf

    """## Merging the TF-IDF according to weights"""

    for i in tf_idf:
        tf_idf[i] *= alpha

    def matching_score(k, query):
        preprocessed_query = preprocess(query)
        tokens = word_tokenize(str(preprocessed_query))

        # print("Matching Score")
        # print("\nQuery:", query)
        # print("")
        # print(tokens)
        
        query_weights = {}
        
        for key in tf_idf:
            
            if key[1] in tokens:
                try:
                    print('yes')
                    query_weights[key[0]] += tf_idf[key]
                except:
                    print('no')
                    query_weights[key[0]] = tf_idf[key]

        query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)

        # print("")
        
        l = []
        
        for i in query_weights[:k]:
            l.append(i[0])
        
        # print(l)
        # print(sorted(l))
        # print(len(l))
        # print(type(l))

        # Ranking = {}
        # for x in range(0,url):
        #     Ranking[l[x]] = arrayURL[x]
        #     # print(arrayURL[x])

        # time_2f = '%.2f' % (time.time() - start_time)
        # times = ((" %s seconds " % time_2f ))

        # cpu = psutil.cpu_percent(interval=1)
        # memory = psutil.swap_memory()[3]
        # disk = psutil.disk_usage('/')[3]


        # return tokens, dict(sorted(Ranking.items())), times, cpu, memory, disk
        

    Q = matching_score(url, Input)

    # def cosine_similarity(k, query):
    #     # print("Cosine Similarity")
    #     preprocessed_query = preprocess(query)
    #     tokens = word_tokenize(str(preprocessed_query))
        
    #     # print("\nQuery:", query)
    #     # print("")
    #     # print(tokens)
        
    #     d_cosines = []
        
    #     query_vector = gen_vector(tokens)
        
    #     for d in D:
    #         d_cosines.append(cosine_sim(query_vector, d))
            
    #     out = np.array(d_cosines).argsort()[-k:][::-1]
    #     # print(len(d_cosines))
    #     # print(d_cosines)
    #     # print(sorted(d_cosines))
    #     # print("")
        
    #     # print(out)
    #     # print(sorted(out))

    #     time_2f = '%.2f' % (time.time() - start_time)
    #     times = ((" %s seconds " % time_2f ))
    #     # print(times)
    # #     for i in out:
    # #         print(i, dataset[i][0])
    #     Ranking = {}
    #     for x in range(0,url):
    #         Ranking[out[x]] = arrayURL[x]
    #         # print(arrayURL[x])

    #     cpu = psutil.cpu_percent(interval=1)
    #     memory = psutil.swap_memory()[3]
    #     disk = psutil.disk_usage('/')[3]

    #     return tokens, dict(sorted(Ranking.items())), times, cpu, memory, disk, sorted(d_cosines)
    
    # Q = cosine_similarity(url, Input)
    # print('********')
    # print(Q[0])
    # print(len(Q[1]))
    # print(Q[2])
    # print('*****************')
    # print(dict(sorted(Q[3].items())))
    # for key, value in sorted (Q[3].items()):
    #     print(key, value)
    # return Q[0], Q[1], Q[2], Q[3], Q[4], Q[5]
    return Q

print(readfile("Without the drive of Rebeccah's insistence, Kate lost her momentum. She stood next a slatted oak bench, canisters still clutched, surveying"))
# print(readfile('to'))