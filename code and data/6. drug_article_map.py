import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

with open('articles_pkl.pkl', 'rb') as f:
    articles = pickle.load(f)

print("articles done")


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



with open('drug_article_map.csv', 'wb') as csvfile:
    fieldnames = ['Drug Name','Article No.']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for drug in drug_names:
    if i % 50 == 0:
        print(i)
    i = i + 1
    article_id = 0
    found_article_list = []
    for article in articles:
        if drug in article:
            found_article_list.append(str(article_id))
        article_id = article_id + 1
    found_article_list_str = ', '.join(found_article_list)
    with open('drug_article_map.csv', 'ab') as csvfile:
        fieldnames = [drug,found_article_list_str]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

