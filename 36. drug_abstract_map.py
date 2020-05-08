import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

abstract_paper=pd.read_csv('abstract_paper_for_pdb.csv')
abstract_paper['abstract'] = abstract_paper['abstract'].str.lower()

drug_names = []
# file handle fh
fh = open('corona_related_drug_name_FINAL.txt')
while True:
    
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    if not line:
        break
    drug_names.append(line.rstrip().lower())
    # check if line is not empty
    
fh.close()

print("drug_names done")



with open('drug_abstract_map_for_pdb.csv', 'wb') as csvfile:
    fieldnames = ['Drug Name','metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for drug in drug_names:
    print(i)
    i = i + 1
    try:
        new_df = abstract_paper[abstract_paper['abstract'].str.contains(drug,na=False)]
        metaId_list = new_df['metaId'].values
        metaId_list = [str(x) for x in metaId_list]
        metaId_list_str = ', '.join(metaId_list)
        with open('drug_abstract_map_for_pdb.csv', 'ab') as csvfile:
            fieldnames = [drug,metaId_list_str]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    except:
        pass

