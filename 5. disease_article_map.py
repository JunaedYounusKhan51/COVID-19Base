import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle

with open('articles_pkl.pkl', 'rb') as f:
    articles = pickle.load(f)

print("articles done")


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



with open('disease_article_map.csv', 'wb') as csvfile:
    fieldnames = ['Disease Name','Article No.']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
print("csv create done")


i = 1


for disease in disease_names:
    if i % 50 == 0:
        print(i)
    i = i + 1
    article_id = 0
    found_article_list = []
    for article in articles:
        if disease in article:
            found_article_list.append(str(article_id))
        article_id = article_id + 1
    found_article_list_str = ', '.join(found_article_list)
    with open('disease_article_map.csv', 'ab') as csvfile:
        fieldnames = [disease,found_article_list_str]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

