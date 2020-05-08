#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
from textblob import TextBlob 
from sklearn.feature_extraction.text import TfidfVectorizer
'''
s = TextBlob("antiviral agents include amantadine and rimantidine, which are used for the treatment of the common cold (rhinoviral disease), and interferon for hepatitis c infection ")
print(s.sentiment)
'''
def distance(s, w1, w2):  
      
    if w1 == w2 : 
       return 0
  
    # get individual words in a list 
    words = s.split(" ") 
  
    # assume total length of the string as 
    # minimum distance 
    min_dist = len(words)+1 
  
    # traverse through the entire string 
    for index in range(len(words)): 
  
        if w1 in words[index]: 
            for search in range(len(words)): 
  
                if w2 in words[search]:  
  
                    # the distance between the words is 
                    # the index of the first word - the  
                    # current word index  
                    curr = abs(index - search) - 1; 
  
                    # comparing current distance with  
                    # the previously assumed distance 
                    if curr < min_dist: 
                       min_dist = curr 
  
    # w1 and w2 are same and adjacent 
    return min_dist





final_output=pd.read_csv('final_output.csv')


corrected_min_dis = []

i=1

for index, row in final_output.iterrows():
	print(i)
	i+=1
	disease = row['Disease Name']
	disease = disease.split(' ')
	disease = str(disease[0])
	drug = row['Drug Name']
	drug = drug.split(' ')
	drug = str(drug[0])	
 	article = row['Common Sentence']
	sentences = article.split('.')
	sentences = list(set(sentences))
	new_article = ""
	min_dis = 999999
	for sentence in sentences:
		if sentence == '' or sentence == " ":
			continue
		current_dis = distance(sentence, disease, drug)
		if current_dis < min_dis:
			min_dis = current_dis
	corrected_min_dis.append(min_dis)


final_output['Minimum Distance Between Disease and Drug'] = corrected_min_dis

final_output.to_csv('final_output_corrected_min_dis.csv', index= False)