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




disease_gene_common_abstract=pd.read_csv('disease_gene_common_abstract_for_gene.csv')
serial_list = range(1,len(disease_gene_common_abstract)+1)
disease_gene_id_list = ["DG"+str(s) for s in serial_list]

disease_gene_common_abstract['DiseaseGeneId'] = disease_gene_id_list

#correcting column order (just to make look good)
disease_gene_common_abstract = disease_gene_common_abstract[['DiseaseGeneId', 'Disease Name','Approved symbol','Common metaId']]
print("disease and gene done")


disease_gene_common_abstract.to_csv("disease_gene_common_abstract_for_gene_with_id.csv",index=False)