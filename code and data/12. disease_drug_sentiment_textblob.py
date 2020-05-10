#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
from textblob import TextBlob 
from sklearn.feature_extraction.text import TfidfVectorizer
'''
s = TextBlob("antiviral agents include amantadine and rimantidine, which are used for the treatment of the common cold (rhinoviral disease), and interferon for hepatitis c infection ")
print(s.sentiment)
'''
#Id,Disease Name,Drug Name,Common Sentence,Minimum Distance Between Disease and Drug,Common Paper Doi
disease_drug_common_sentence_final=pd.read_csv('disease_drug_common_sentence_final_with_outlier_flag.csv',encoding="utf-8",skipinitialspace=True)
disease_drug_common_sentence_final = disease_drug_common_sentence_final[disease_drug_common_sentence_final['Outlier Flag'] != 1]


with open('disease_drug_sentiment_textblob_with_outlier_flag.csv', 'wb') as csvfile:
    fieldnames = ['Id','Disease Name','Drug Name','Common Sentence','Chosen Sentence','Minimum Distance Between Disease and Drug','Common Paper Doi','Polarity(textblob)','Label(textblob)','Agree/Disagree(textblob)','Outlier Flag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")



i=1

for index, row in disease_drug_common_sentence_final.iterrows():
	print(i)
	i+=1
	drug = row['Drug Name'].encode("utf-8")
	disease = row['Disease Name'].encode("utf-8")
	article = row['Common Sentence'].encode("utf-8")
	min_dis = row['Minimum Distance Between Disease and Drug']
	idd = row['Id']
	doi = row['Common Paper Doi']
	outlier_flag = row=['Outlier Flag']
	sentences = article.split('.')
	sentences = set(sentences)
	sentences = list(sentences)
	candidate_sentences = []
	sentence_1 = ""
	sentence_2 = ""
	polarity_diff = ""
	flag = ""
	comment = ""
	avg_polarity = ""
	status = ""
	chosen_sentence = ""
	temp = []
	for sentence in sentences:
		if sentence == '':
			continue
		temp.append(sentence)
	sentences = temp[:]
	
	for sentence in sentences:
		if len(sentence) > 200:
			continue
		candidate_sentences.append(sentence)
	if len(candidate_sentences) == 0 or len(candidate_sentences) == 1:
		candidate_sentences = sentences[:]
	if len(candidate_sentences) == 1:
		sentence = candidate_sentences[0]
		chosen_sentence = sentence + "."
		sentiment_dict = TextBlob(sentence.decode("utf-8"))
		sentiment = sentiment_dict.sentiment
		avg_polarity = sentiment.polarity
		if avg_polarity > 0:
			status = 1
		elif avg_polarity < 0:
			status = 0
		else:
			status = 1
		flag = "Not Determined"
		polarity_diff = "Not Applied"
		comment = "only one sentence"

	else:
		try:
			tfidf_vect = TfidfVectorizer(stop_words = 'english')
			X = tfidf_vect.fit(candidate_sentences)
			X = tfidf_vect.transform(candidate_sentences)
			tfidf_list =X.toarray().tolist()
			max_sum = -1
			max_index = -1
			ii=0
			for l in tfidf_list:
				current_sum = sum(l)
				if current_sum > max_sum:
					max_sum = current_sum
					max_index = ii
				ii+=1
			jj = 0
			second_max_sum = -1
			second_max_index = -1
			for l in tfidf_list:
				current_sum = sum(l)
				if current_sum > second_max_sum and jj != max_index:
					second_max_sum = current_sum
					second_max_index = jj
				jj+=1
			sentence_1 = candidate_sentences[max_index] + "."
			sentence_2 = candidate_sentences[second_max_index] + "."
			chosen_sentence = sentence_1 + ". " + sentence_2
			sentiment_dict_1 = TextBlob(sentence_1.decode("utf-8"))
			sentiment_1 = sentiment_dict_1.sentiment
			polarity_1 = sentiment_1.polarity
			sentiment_dict_2 = TextBlob(sentence_2.decode("utf-8"))
			sentiment_2 = sentiment_dict_2.sentiment
			polarity_2 = sentiment_2.polarity
			avg_polarity = (polarity_1 + polarity_2) / 2.0
			polarity_diff = abs(polarity_1-polarity_2)
			comment = "flagged"
			if polarity_1 * polarity_2 >= 0:
				flag = "Agree"
			else:
				flag = "Disagree"
			if avg_polarity > 0:
				status = 1
			elif avg_polarity < 0:
				status = 0
			else:
				status = 1
		except:
			chosen_sentence = "NONE"
			avg_polarity = "NONE"
			status = "NONE"
			polarity_diff = "NONE"
			flag = "NONE"
			comment = "Unknown"
	with open('disease_drug_sentiment_textblob_with_outlier_flag.csv', 'ab') as csvfile:
		fieldnames = [idd,disease,drug,article,chosen_sentence,min_dis,doi,avg_polarity,status,flag,outlier_flag]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()