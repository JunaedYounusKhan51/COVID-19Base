import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle
import math





disease_drug_common_sentence=pd.read_csv('disease_drug_common_sentence.csv',skipinitialspace=True)
print("disease and drug common article done")

'''
with open('disease_drug_common_article.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Drug Name','Common Article No.']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")
'''

with open('disease_drug_common_sentence_with_id.csv', 'wb') as csvfile:
    fieldnames = ['Id','Disease Name','Drug Name','Common Sentence','Common Paper Doi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")



i = 1


for index, row in disease_drug_common_sentence.iterrows():
	idd = i
	i+=1
	disease = row['Disease Name']
	drug = row['Drug Name']
	common_sentence = row['Common Sentence']
	common_titles_str  = row['Common Paper Doi']
	with open('disease_drug_common_sentence_with_id.csv', 'ab') as csvfile:
		fieldnames = [idd,disease,drug,common_sentence,common_titles_str]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()