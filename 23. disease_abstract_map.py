import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

abstract_paper=pd.read_csv('abstract_paper_for_gene.csv')
abstract_paper['abstract'] = abstract_paper['abstract'].str.lower()

disease_names = []
# file handle fh
fh = open('corona_related_disease_name_FINAL.txt')
while True:
    
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    if not line:
        break
    disease_names.append(line.rstrip().lower())
    # check if line is not empty
    
fh.close()

print("disease_names done")



with open('disease_abstract_map_for_gene.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for disease in disease_names:
    if i % 50 == 0:
        print(i)
    i = i + 1
    new_df = abstract_paper[abstract_paper['abstract'].str.contains(disease,na=False)]
    metaId_list = new_df['metaId'].values
    metaId_list = [str(x) for x in metaId_list]
    metaId_list_str = ', '.join(metaId_list)
    with open('disease_abstract_map_for_gene.csv', 'ab') as csvfile:
        fieldnames = [disease,metaId_list_str]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

