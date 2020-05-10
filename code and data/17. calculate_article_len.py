#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
'''
s = TextBlob("antiviral agents include amantadine and rimantidine, which are used for the treatment of the common cold (rhinoviral disease), and interferon for hepatitis c infection ")
print(s.sentiment)
'''
final_output_labeled_only=pd.read_csv('final_output_labeled_only.csv')
final_output_normal = pd.read_csv('final_output_corrected_min_dis.csv')


article_len = []



'''
ref_id = row['Id']
    ref_row = final_output_normal.loc[final_output_normal['Id'] == ref_id]
    ref_article = ref_row['Common Sentence']
    article = row['Common Sentence']
    if len(ref_article) == len(article):
        print("TRUE")'''
for index, row in final_output_normal.iterrows():
    article_len.append(len(row['Common Sentence']))



final_output_normal['Article Len'] = article_len
final_output_normal.to_csv('final_output_with_len.csv', index= False)



article_len = []



'''
ref_id = row['Id']
    ref_row = final_output_normal.loc[final_output_normal['Id'] == ref_id]
    ref_article = ref_row['Common Sentence']
    article = row['Common Sentence']
    if len(ref_article) == len(article):
        print("TRUE")'''
for index, row in final_output_labeled_only.iterrows():
    ref_id = row['Id']
    ref_row = final_output_normal.loc[final_output_normal['Id'] == ref_id]
    ref_article = ref_row['Common Sentence'].values[0]
    article_len.append(len(ref_article))



final_output_labeled_only['Article Len'] = article_len
final_output_labeled_only.to_csv('final_output_labeled_only_with_len.csv', index= False)