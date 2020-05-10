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


from time import time 
from collections import defaultdict

import logging
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

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

	#tagged_text = nltk.tag.pos_tag(text.split())
	#edited_text = [word for word,tag in tagged_text if tag != 'CC' and tag != 'CD' and  tag != 'FW' and tag != 'IN' and  tag != 'NN' and tag != 'NNS' and  tag != 'NNP' and tag != 'NNPS' and tag != 'PRP' and tag != 'PRP$' and  tag != 'TO' and tag != 'UH' and  tag != 'WDT' and tag != 'WP' and  tag != 'WP$' and tag != 'WRB']
	#text = ' '.join(edited_text)

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




data = pd.read_csv("disease_drug_sentiment_textblob_with_outlier_flag_final.csv")

disease_list = data['Disease Name'].tolist()
drug_list = data['Drug Name'].tolist()
article_list = data['Common Sentence'].tolist()

processed_article_list = []

for article in article_list:
	processed_article = preprocess(article)
	processed_article_list.append(processed_article)

print("preprocessing done")

sent = processed_article_list #just to keep it as source
phrases = Phrases(sent, min_count=1, progress_per=50000)
bigram = Phraser(phrases)
sentences = bigram[sent]



w2v_model = Word2Vec(min_count=5,
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
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
print('Time to train the model: {} mins'.format(round((time() - start) / 60, 2)))
w2v_model.init_sims(replace=True)


w2v_model.save("word2vec.model")



new_article_list = []

for processed_article in processed_article_list:
	new_article = ' '.join(bigram[processed_article])
	new_article_list.append(new_article)


zippedList =  list(zip(disease_list, drug_list, new_article_list))
clean_data = pd.DataFrame(zippedList, columns = ['disease' , 'drug', 'title']) 
clean_data.to_csv('cleaned_dataset.csv', index=False)