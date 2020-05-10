import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import re
from re import sub
import pandas as pd
import numpy as np
import re
from re import sub
import multiprocessing

from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
import pickle

from time import time 
from collections import defaultdict

import logging
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

def preprocess(text,disease,gene):
	#text = str(text)
	#string.replace(old, new)
	disease_old = disease
	#print disease
	disease = re.sub(' ', '_', disease)
	#print disease

	gene_old = gene
	#gene_new = gene.replace(' ','_')
	#gene_new = gene_new.replace('-','_')
	#gene_new = gene_new.replace('.','_')
	gene = re.sub(' ', '_', gene)
	gene = re.sub('-','_',gene)
	
	text = re.sub(gene_old, gene, text)
	text = re.sub(disease_old, disease, text)
	

	tokens = word_tokenize(text.decode('utf-8'))
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if w == 'no' or w == 'not' or not w in stop_words]
	porter = PorterStemmer()
	stems = []
	for t in tokens:
		if t == disease:
			stems.append(t)
		elif t==gene:
			stems.append(t)
		else:
			try:
				stems.append(porter.stem(t.lower()))
			except:
				pass


	return stems


dg_abs_paper_final = pd.read_csv("dg_abs_paper_final_dropnull.csv")

iii=1
processed_abstract_list = []

for index, row in dg_abs_paper_final.iterrows():
	print(iii)
	iii+=1
	disease = row['Disease Name']
	gene = row['Approved symbol']
	abstract = row['Abstract']
	processed_abs = preprocess(abstract,disease,gene)
	processed_abstract_list.append(processed_abs)

print("preprocessing done")

#sent = processed_article_list #just to keep it as source
#phrases = Phrases(sent, min_count=1, progress_per=50000)
#bigram = Phraser(phrases)
#sentences = bigram[sent]

sentences=processed_abstract_list

'''with open('sentences_word2vec_for_gene.pkl', 'wb') as f:
	pickle.dump(sentences, f)'''

w2v_model = Word2Vec(min_count=1,
                     window=4,
                     size=300,
                     sample=1e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     workers=multiprocessing.cpu_count()-1)


start = time()
w2v_model.build_vocab(sentences, progress_per=50000)
print('Time to build vocab: {} mins'.format(round((time() - start) / 60, 2)))


start = time()
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=10, report_delay=1)
print('Time to train the model: {} mins'.format(round((time() - start) / 60, 2)))
w2v_model.init_sims(replace=True)


w2v_model.save("word2vec_for_gene.model")

