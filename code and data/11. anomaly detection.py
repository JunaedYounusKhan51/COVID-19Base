import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from re import sub

import pickle
import pandas as pd
import numpy
import re
import os
import numpy as np
import gensim
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from gensim.models import Doc2Vec
import matplotlib.pyplot as plt
import collections
#import logging
#logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
#%matplotlib inline
#plt.figure


def preprocess(text):
	text = str(text)

	#alpha numeric, punctuation remove kortesi
	text = sub(r"[^A-Za-z0-9^,!?.\/'+]", " ", text)
	text = sub(r"\+", " plus ", text)
	text = sub(r",", " ", text)
	text = sub(r"\.", " ", text)
	text = sub(r"!", " ! ", text)
	text = sub(r"\?", " ? ", text)
	text = sub(r"'", " ", text)
	text = sub(r":", " : ", text)
	text = sub(r"\s{2,}", " ", text)


	tokens = word_tokenize(text)
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if w == 'no' or w == 'not' or not w in stop_words]
	porter = PorterStemmer()
	stems = []
	for t in tokens:
		stems.append(porter.stem(t))

	clean_words = []	
	rx = re.compile(r'\D*\d')
	for s in stems:
		if rx.match(s):
			continue 
		clean_words.append(s)
	return clean_words


data = pd.read_csv("disease_drug_common_sentence_final.csv")


disease_list = data['Disease Name'].tolist()
drug_list = data['Drug Name'].tolist()
article_list_ = data['Common Sentence'].tolist()

article_list = []
i = 0

for article in article_list_:
	print(i)
	i+=1
	article_list.append(preprocess(article))



LabeledSentence1 = gensim.models.doc2vec.TaggedDocument

all_content_train = []

j=0

for em in article_list:
    all_content_train.append(LabeledSentence1(em,[j]))
    j+=1


d2v_model = Doc2Vec(all_content_train, size = 300, window = 10, min_count = 3, workers=7, dm = 1,alpha=0.025, min_alpha=0.001)
d2v_model.train(all_content_train, total_examples=d2v_model.corpus_count, epochs=10, start_alpha=0.002, end_alpha=-0.016)


kmeans_model = KMeans(n_clusters=2, init='k-means++', max_iter=100) 
X = kmeans_model.fit(d2v_model.docvecs.doctag_syn0)
labels=kmeans_model.labels_.tolist()



min_element = min(labels,key=labels.count)
ii = 0
freq = 0
for l in labels:
	if l == min_element:
		freq+=1
		print("---------------------------------------------------------------")
		print(article_list_[ii])
		print("---------------------------------------------------------------")
	ii+=1

counter=collections.Counter(labels)
print(counter)
print(freq)


data['Outlier Flag'] = labels
data.to_csv('disease_drug_common_sentence_final_with_outlier_flag.csv', index=False)

l = kmeans_model.fit_predict(d2v_model.docvecs.doctag_syn0)
pca = PCA(n_components=2).fit(d2v_model.docvecs.doctag_syn0)
datapoint = pca.transform(d2v_model.docvecs.doctag_syn0)


label1 = ["#FFFF00", "#008000", "#0000FF", "#800080"]
color = [label1[i] for i in labels]
plt.scatter(datapoint[:, 0], datapoint[:, 1], c=color)
centroids = kmeans_model.cluster_centers_
centroidpoint = pca.transform(centroids)
plt.scatter(centroidpoint[:, 0], centroidpoint[:, 1], marker='^', s=150, c='#000000')
plt.show()