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


abstract_data = pd.read_csv('abstract_paper_for_gene.csv')

disease_gene_common_abstract=pd.read_csv('disease_gene_common_abstract_for_gene_with_id.csv')
print("disease and gene done")


with open('dg_abs_paper_final.csv', 'wb') as csvfile:
    fieldnames = ['DiseaseGeneId','Disease Name','Approved symbol','AbstractId','Abstract','Paper Title','Paper Doi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1
abs_id = 0

for index, row in disease_gene_common_abstract.iterrows():
	print(i)
	i = i + 1
	dgId = row['DiseaseGeneId']
	disease = row['Disease Name']
	gene=row['Approved symbol']
	common_abs_id_list = row['Common metaId'].split(", ")
	for common_abs_id in common_abs_id_list:
		abs_id += 1
		abs_id_str = "ABS"+str(abs_id)
		common_abs_id = int(common_abs_id)
		new_df = abstract_data.loc[abstract_data['metaId'] == common_abs_id]
		new_row = new_df.iloc[0]
		abstract = new_row['abstract']
		title = new_row['title']
		doi = new_row['doi']
		with open('dg_abs_paper_final.csv', 'ab') as csvfile:
		    fieldnames = [dgId,disease,gene,abs_id_str,abstract,title,doi]
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		    writer.writeheader()

