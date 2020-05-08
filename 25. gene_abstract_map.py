import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

abstract_paper=pd.read_csv('abstract_paper_for_gene.csv')


gene_names = []
# file handle fh
fh = open('corona_related_gene_name_from_ABSTRACT_for_gene.txt')
while True:
    
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    if not line:
        break
    gene_names.append(line.rstrip())
    # check if line is not empty
    
fh.close()

print("gene names done")



with open('gene_abstract_map_for_gene.csv', 'wb') as csvfile:
    fieldnames = ['Approved symbol','metaId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for gene in gene_names:
    if i % 50 == 0:
        print(i)
    i = i + 1
    new_df = abstract_paper[abstract_paper['abstract'].str.contains(gene,na=False)]
    metaId_list = new_df['metaId'].values
    metaId_list = [str(x) for x in metaId_list]
    metaId_list_str = ', '.join(metaId_list)
    with open('gene_abstract_map_for_gene.csv', 'ab') as csvfile:
        fieldnames = [gene,metaId_list_str]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

