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


disease_article_map=pd.read_csv('disease_article_map.csv',encoding="utf-8",skipinitialspace=True)
drug_article_map=pd.read_csv('drug_article_map.csv',encoding="utf-8",skipinitialspace=True)
print("disease and drug done")


with open('disease_drug_common_article.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Drug Name','Common Article No.']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1

for disease_index, disease_row in disease_article_map.iterrows():
	print(i)
	i = i + 1
	if isnan(disease_row['Article No.']):
		continue
	disease = disease_row['Disease Name'].encode("utf-8")
	disease_article_list = disease_row['Article No.'].encode("utf-8").split(", ")
	for drug_index, drug_row in drug_article_map.iterrows():
		if isnan(drug_row['Article No.']):
			continue
		drug = drug_row['Drug Name'].encode("utf-8")
		drug_article_list = drug_row['Article No.'].encode("utf-8").split(", ")
		common_article_list = list(set(disease_article_list) & set(drug_article_list)) #intersection
		common_article_list_str = ', '.join(common_article_list)
		if len(common_article_list) != 0:
			with open('disease_drug_common_article.csv', 'ab') as csvfile:
				fieldnames = [disease,drug,common_article_list_str]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()