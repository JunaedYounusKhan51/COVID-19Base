import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

abstract_paper=pd.read_csv('abstract_paper_for_pdb.csv')
#abstract_paper['abstract'] = abstract_paper['abstract'].str.lower()

pdb_id_list = []
# file handle fh
fh = open('corona_related_pdb_from_ABSTRACT_for_pdb.txt')
while True:
    
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    if not line:
        break
    pdb_id_list.append(line.rstrip())
    # check if line is not empty
    
fh.close()

print("pdb_id_list done")



with open('pdb_abstract_map_for_pdb.csv', 'wb') as csvfile:
    fieldnames = ['PdbId','metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for pdb in pdb_id_list:
    if i % 50 == 0:
        print(i)
    i = i + 1
    pdb_space = " "+pdb
    new_df = abstract_paper[abstract_paper['abstract'].str.contains(pdb_space,na=False)]
    metaId_list = new_df['metaId'].values
    metaId_list = [str(x) for x in metaId_list]
    metaId_list_str = ', '.join(metaId_list)
    with open('pdb_abstract_map_for_pdb.csv', 'ab') as csvfile:
        fieldnames = [pdb,metaId_list_str]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

