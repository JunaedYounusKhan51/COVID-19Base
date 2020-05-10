import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import py_aho_corasick as ahoc

def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False




full_gene_df = pd.read_csv('full_gene_df.csv')
gene_names = full_gene_df['Approved symbol'].tolist()
gene_names = [str(g) for g in gene_names]



abstract_paper_for_gene=pd.read_csv('abstract_paper_for_gene.csv')
abstract_list = abstract_paper_for_gene['abstract'].tolist()
abstract_list = [a for a in abstract_list if str(a) != 'nan']


print("abstract list done")
all_abstract = ' '.join(abstract_list) 


print("all abstract done")






print("search start")

A = ahoc.Automaton(gene_names)

found_list =  A.get_keywords_found(all_abstract)
found_list = set(found_list)
found_list = list(found_list)

print("search complete")


with open('corona_related_gene_name_from_ABSTRACT_for_gene.txt', 'w') as filehandle:
    for listitem in found_list:
        filehandle.write('%s\n' % listitem)








