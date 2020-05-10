#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
'''
s = TextBlob("antiviral agents include amantadine and rimantidine, which are used for the treatment of the common cold (rhinoviral disease), and interferon for hepatitis c infection ")
print(s.sentiment)
'''
data=pd.read_csv('final_output_prediction_and_confidence_with_force_confidence.csv')
print(len(data))
data=data[data['Outlier Flag'] != 1]
print(len(data))
data=data.sort_values('Id').drop_duplicates(subset=['Disease Name','Drug Name'],keep='first')
print(len(data))

#Id,Disease Name,Drug Name,Force Label,Forced Confidence Score


delivery_col_list = ['Id','Disease Name','Drug Name','Force Label','Forced Confidence Score']
final_output_for_delivery = data[delivery_col_list].copy()
final_output_for_delivery['Status']='Automatically Labeled'

label_list = []


for index, row in final_output_for_delivery.iterrows():
	label_int = row['Force Label']
	label_str = "NONE"
	if label_int == 1:
		label_str = "Positive"
	elif label_int == 0:
		label_str = "Negative"
	label_list.append(label_str)

final_output_for_delivery['Force Label']=label_list
final_output_for_delivery.to_csv("final_output_for_delivery.csv", index=False)

        