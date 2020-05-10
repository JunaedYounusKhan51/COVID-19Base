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


abstract_data = pd.read_csv('abstract_paper_for_pdb.csv')

drug_pdb_common_abstract=pd.read_csv('drug_pdb_common_abstract_for_pdb_with_id.csv')
print("drug and pdb done")


with open('drp_abs_paper_final.csv', 'wb') as csvfile:
    fieldnames = ['DrugPdbId','Drug Name','PdbId','AbstractId','Abstract','Paper Title','Paper Doi']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1
abs_id = 0

for index, row in drug_pdb_common_abstract.iterrows():
	print(i)
	i = i + 1
	drpId = row['DrugPdbId']
	drug = row['Drug Name']
	pdb=row['PdbId']
	common_abs_id_list = row['Common metaId'].split(", ")
	for common_abs_id in common_abs_id_list:
		abs_id += 1
		abs_id_str = "drpABS"+str(abs_id)
		common_abs_id = int(common_abs_id)
		new_df = abstract_data.loc[abstract_data['metaId'] == common_abs_id]
		new_row = new_df.iloc[0]
		abstract = new_row['abstract']
		title = new_row['title']
		doi = new_row['doi']
		with open('drp_abs_paper_final.csv', 'ab') as csvfile:
		    fieldnames = [drpId,drug,pdb,abs_id_str,abstract,title,doi]
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		    writer.writeheader()

