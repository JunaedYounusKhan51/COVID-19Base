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




drug_abstract_map=pd.read_csv('drug_abstract_map_for_pdb.csv')
pdb_abstract_map=pd.read_csv('pdb_abstract_map_for_pdb.csv')
print("drug and pdb done")


with open('drug_pdb_common_abstract_for_pdb.csv', 'wb') as csvfile:
    fieldnames = ['Drug Name','PdbId','Common metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")

removed_drug = ['balance','capture','date','dimension','house dust','mate','monitor','olive oil','camp']

i = 1

for drug_index, drug_row in drug_abstract_map.iterrows():
	print(i)
	i = i + 1
	if isnan(drug_row['metaId']):
		continue
	drug = drug_row['Drug Name']
	if len(drug)<=3:
		continue
	if drug in removed_drug:
 		continue
 	drug_article_list = drug_row['metaId'].split(", ")
	for pdb_index, pdb_row in pdb_abstract_map.iterrows():
		if isnan(pdb_row['metaId']):
			continue
		pdb = pdb_row['PdbId']
		pdb_article_list = pdb_row['metaId'].split(", ")
		common_article_list = list(set(drug_article_list) & set(pdb_article_list)) #intersection
		common_article_list_str = ', '.join(common_article_list)
		if len(common_article_list) != 0:
			with open('drug_pdb_common_abstract_for_pdb.csv', 'ab') as csvfile:
				fieldnames = [drug,pdb,common_article_list_str]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()