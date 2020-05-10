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




disease_abstract_map=pd.read_csv('disease_abstract_map_for_gene.csv')
gene_abstract_map=pd.read_csv('gene_abstract_map_for_gene.csv')
print("disease and gene done")


with open('disease_gene_common_abstract_for_gene.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Approved symbol','Common metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1

for disease_index, disease_row in disease_abstract_map.iterrows():
	print(i)
	i = i + 1
	if isnan(disease_row['metaId']):
		continue
	disease = disease_row['Disease Name']
	disease_article_list = disease_row['metaId'].split(", ")
	for gene_index, gene_row in gene_abstract_map.iterrows():
		if isnan(gene_row['metaId']):
			continue
		gene = gene_row['Approved symbol']
		gene_article_list = gene_row['metaId'].split(", ")
		common_article_list = list(set(disease_article_list) & set(gene_article_list)) #intersection
		common_article_list_str = ', '.join(common_article_list)
		if len(common_article_list) != 0:
			with open('disease_gene_common_abstract_for_gene.csv', 'ab') as csvfile:
				fieldnames = [disease,gene,common_article_list_str]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()