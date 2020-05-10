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

disease_drug_common_sentence_with_id=pd.read_csv('disease_drug_common_sentence_with_id.csv',encoding="utf-8",skipinitialspace=True)


with open('disease_drug_common_sentence_final.csv', 'wb') as csvfile:
    fieldnames = ['Id','Disease Name','Drug Name','Common Sentence','Minimum Distance Between Disease and Drug','Common Paper Doi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")



i=1

for index, row in disease_drug_common_sentence_with_id.iterrows():
	disease = row['Disease Name'].encode("utf-8")
	drug = row['Drug Name'].encode("utf-8")
 	article = row['Common Sentence'].encode("utf-8")
	idd = row['Id']
	doi = row['Common Paper Doi']
	sentences = article.split('.')
	sentences = set(sentences)
	sentences = list(sentences)
	min_dis = 999999
	for sentence in sentences:
		if sentence == '':
			continue
		current_dis = abs(sentence.find(disease) - sentence.find(drug))
		if current_dis < min_dis:
			min_dis = current_dis
	print(min_dis)
	with open('disease_drug_common_sentence_final.csv', 'ab') as csvfile:
		fieldnames = [idd,disease,drug,article,min_dis,doi]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()