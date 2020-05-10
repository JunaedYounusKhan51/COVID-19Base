import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle
import math


def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False


with open('articles_pkl.pkl', 'rb') as f:
    articles = pickle.load(f)
print(len(articles))

with open('dois_pkl.pkl', 'rb') as f:
    dois = pickle.load(f)
print(len(dois))
print("articles done")


disease_drug_common_article=pd.read_csv('disease_drug_common_article.csv',encoding="utf-8",skipinitialspace=True)
print("disease and drug common article done")

'''
with open('disease_drug_common_article.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Drug Name','Common Article No.']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")
'''

with open('disease_drug_common_sentence.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Drug Name','Common Sentence','Common Paper Doi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")



i = 1


for index, row in disease_drug_common_article.iterrows():
	if i % 500 == 0:
		print(i)
	i=i+1
	drug = row['Drug Name'].encode("utf-8")
	if len(drug)<=3:
		continue
	common_sentence = ""
	common_titles = []
	disease = row['Disease Name'].encode("utf-8")
	common_article_list = row['Common Article No.'].encode("utf-8").split(", ")
	for common_article_id in common_article_list:
		common_article_id = int(common_article_id)
		article = articles[common_article_id]
		sentences = article.split('.')
		for sentence in sentences:
			sentence = " " + sentence + " "
			disease_space = " " + disease + " "
			drug_space = " " + drug + " "
			if disease_space in sentence and drug_space in sentence:
				common_sentence = common_sentence + ". " + sentence
				common_titles.append(dois[common_article_id])
	if common_sentence != "":
		common_titles = list(set(common_titles))
		common_titles_str = ', '.join(common_titles)
		with open('disease_drug_common_sentence.csv', 'ab') as csvfile:
			fieldnames = [disease,drug,common_sentence,common_titles_str]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()