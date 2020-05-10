import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv
import pickle
import math


def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False




drug_pdb_common_abstract=pd.read_csv('drug_pdb_common_abstract_for_pdb.csv')
serial_list = range(1,len(drug_pdb_common_abstract)+1)
drug_pdb_id_list = ["DRP"+str(s) for s in serial_list]

drug_pdb_common_abstract['DrugPdbId'] = drug_pdb_id_list


#correcting column order (just to make look good)
drug_pdb_common_abstract = drug_pdb_common_abstract[['DrugPdbId', 'Drug Name','PdbId','Common metaId']]
print("drug and pdb done")


drug_pdb_common_abstract.to_csv("drug_pdb_common_abstract_for_pdb_with_id.csv",index=False)