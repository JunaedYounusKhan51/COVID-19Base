import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from glob import glob
import json
from nltk.corpus import stopwords
from tqdm.notebook import tqdm
import os


dir_list = [
    'biorxiv_medrxiv/biorxiv_medrxiv',
    'comm_use_subset/comm_use_subset',
    'custom_license/custom_license',
    'noncomm_use_subset/noncomm_use_subset'
]
results_list = list()
for target_dir in dir_list:
    
    print(target_dir)
    
    for json_fp in tqdm(glob(target_dir + '/*.json')):

        with open(json_fp) as json_file:
            target_json = json.load(json_file)

        data_dict = dict()
        data_dict['doc_id'] = target_json['paper_id']
        data_dict['title'] = target_json['metadata']['title']

        abstract_section = str()
        for element in target_json['abstract']:
            abstract_section += element['text'] + ' '
        data_dict['abstract'] = abstract_section

        full_text_section = str()
        for element in target_json['body_text']:
            full_text_section += element['text'] + ' '
        data_dict['full_text'] = full_text_section
        
        results_list.append(data_dict)
        
    
df_results = pd.DataFrame(results_list)
df_results.to_pickle("total_corpus_pkl.pkl")
df_results.to_csv('total_corpus_csv.csv', encoding='utf-8', index=False)
unpickled_df = pd.read_pickle("total_corpus_pkl.pkl")
print(unpickled_df.head())

#print(df_results.head())
'''
articles=df_results['full_text'].values
for text in articles:
    for sentences in text.split('.'):
        if 'hydroxychloroquine' in sentences:
            print(sentences.encode("utf-8"))
'''
