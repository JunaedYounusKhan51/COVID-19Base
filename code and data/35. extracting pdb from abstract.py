import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import py_aho_corasick as ahoc

def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False




pdb_id = []
# file handle fh
fh = open('All_PDBid.txt')
while True:
    
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    if not line:
        break
    pdb_id.append(line.rstrip().upper())
    # check if line is not empty
    
fh.close()

print("pdb_id names done")





abstract_paper_for_pdb=pd.read_csv('abstract_paper_for_pdb.csv')
abstract_list = abstract_paper_for_pdb['abstract'].tolist()
abstract_list = [a for a in abstract_list if str(a) != 'nan']


print("abstract list done")
all_abstract = ' '.join(abstract_list) 


print("all abstract done")






print("search start")

A = ahoc.Automaton(pdb_id)

found_list =  A.get_keywords_found(all_abstract)
found_list = set(found_list)
found_list = list(found_list)

print("search complete")


with open('corona_related_pdb_from_ABSTRACT_for_pdb.txt', 'w') as filehandle:
    for listitem in found_list:
        filehandle.write('%s\n' % listitem)








