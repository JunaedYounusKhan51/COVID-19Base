#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv




metadata=pd.read_csv('metadata.csv')
metadata=metadata[['title','doi','abstract']].copy()
serial_list = range(1,len(metadata)+1)
metadata['metaId'] = serial_list
metadata.to_csv('abstract_paper_for_pdb.csv',index=False)





'''
corrected_min_dis = []

i=1

disease_substring_list = []
drug_substring_list = []

print('Disease Name', 'Drug Name')
for index, row in final_output_prediction_and_confidence.iterrows():
    disease = row['Disease Name']
    disease = disease.lstrip()
    disease = disease.rstrip()
    drug = row['Drug Name']
    drug = drug.lstrip()
    drug = drug.rstrip()
    if drug in disease:
        print(disease, drug)
        disease_substring = disease.replace(drug, '')
        disease_substring = disease_substring.lstrip()
        disease_substring = disease_substring.rstrip()
        disease_substring_list.append(disease_substring)
    elif disease in drug:
        print(disease, drug)
        drug_substring = drug.replace(disease, '')
        drug_substring = drug_substring.lstrip()
        drug_substring = drug_substring.rstrip()
        drug_substring_list.append(drug_substring)


print("")
print("")
print("-------------------------------------------------------------")
print("")
print("")

drug_substring_list = list(set(drug_substring_list))
disease_substring_list = list(set(disease_substring_list))



print("Disease Subtring:")
for disease_sub in disease_substring_list:
    print(disease_sub)



print("")
print("")
print("-------------------------------------------------------------")
print("")
print("")
print("Drug Subtring: ")
for drug_sub in drug_substring_list:
    print(drug_sub)'''



        