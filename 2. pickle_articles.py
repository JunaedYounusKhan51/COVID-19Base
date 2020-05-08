import pickle
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math




def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False


fields = ['sha','doi']

metadata=pd.read_csv('metadata.csv',encoding="utf-8",skipinitialspace=True, usecols=fields)

sha_list = metadata['sha'].values
doi_list = metadata['doi'].values

articles=[]
dois=[]

df_results = pd.read_pickle("total_corpus_pkl.pkl")
full_texts=df_results['full_text'].values
full_doc_id = df_results['doc_id'].values



jj=0

for text,doc_id in zip(full_texts,full_doc_id):
    print(jj)
    if isinstance(text,float) == False:
        text = text.encode('utf-8')
    if isinstance(doc_id,float) == False:
        doc_id = doc_id.encode('utf-8')
    text = str(text)
    doc_id = str(doc_id)
    new_df = metadata[metadata['sha'].str.contains(doc_id, na=False)]
    doi = new_df['doi'].values[0]
    if isinstance(doi,float) == False:
        doi = doi.encode('utf-8')
    doi = str(doi)
    if doi == "" or doi == " ":
        print("PROBLEM")
    if text != 'nan' or text != 'Unknown':
        articles.append(text.lower())
        dois.append(doi)
    jj+=1
        

fields = ['doi','abstract', 'has_full_text']

metadata=pd.read_csv('metadata.csv',encoding="utf-8",skipinitialspace=True, usecols=fields)

metadata=metadata.loc[metadata['has_full_text'] == False]
 

for index, row in metadata.iterrows():
    abstract = row['abstract']
    doi = row['doi']
    if isinstance(abstract,float) == False:
        abstract = abstract.encode('utf-8')
    if isinstance(doi,float) == False:
        doi = doi.encode('utf-8')
    abstract = str(abstract)
    doi=str(doi)
    if doi == "" or doi == " ":
        print("PROBLEM 2")
    if abstract != 'nan' or abstract != 'Unknown':
        articles.append(text.lower())
        dois.append(doi)


print("articles done")

with open('articles_pkl.pkl', 'wb') as f:
	pickle.dump(articles, f)


with open('dois_pkl.pkl', 'wb') as f:
    pickle.dump(dois, f)

zippedList =  list(zip(dois, articles))
clean_data = pd.DataFrame(zippedList, columns = ['doi' , 'article']) 
clean_data.to_csv('article_doi.csv', index=False)