import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import py_aho_corasick as ahoc

def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False


##full_text
all_full_text = ""
df_results = pd.read_pickle("total_corpus_pkl.pkl")


for index, row in df_results.iterrows():
    full_text = row['full_text']
    if isinstance(full_text,float) == False:
        full_text = full_text.encode('utf-8')
    full_text = str(full_text)
    if full_text != 'nan' or full_text != 'Unknown':
        all_full_text = all_full_text + " " + full_text


##abstract
fields = ['abstract', 'has_full_text']

metadata=pd.read_csv('metadata.csv',encoding="utf-8",skipinitialspace=True, usecols=fields)

metadata=metadata.loc[metadata['has_full_text'] == False]

all_abstract = "" 

for index, row in metadata.iterrows():
    abstract = row['abstract']
    if isinstance(abstract,float) == False:
        abstract = abstract.encode('utf-8')
    abstract = str(abstract)
    if abstract != 'nan' or abstract != 'Unknown':
        all_abstract = all_abstract + " " + abstract

#print(all_abstract)
print("all abstract done")


total_corpus = all_full_text + " " + all_abstract

drug_fields = ['Common name', 'Synonyms']
drug_data =pd.read_csv('Drugs.csv',encoding="utf-8",skipinitialspace=True, usecols=drug_fields)

drug_names = [str(i.encode('utf-8')) for i in drug_data["Common name"].tolist()]
#drug_names = drug_data["Common name"].tolist()
#print(len(drug_names))

print("search start")

A = ahoc.Automaton(drug_names, lowercase = True)

found_list =  A.get_keywords_found(total_corpus)
found_list = set(found_list)
found_list = list(found_list)

print("search complete")


with open('corona_related_drug_name_FINAL.txt', 'w') as filehandle:
    for listitem in found_list:
        filehandle.write('%s\n' % listitem)