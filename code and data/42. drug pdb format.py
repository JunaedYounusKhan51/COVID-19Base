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


pdb_drug_association = pd.read_csv('drug_pdb_common_abstract_for_pdb_with_id_dropnull.csv',encoding='utf-8')
drp_abs_paper_final = pd.read_csv('drp_abs_paper_final_dropnull.csv',encoding='utf-8')

pdb_drug_association = pdb_drug_association[['DrugPdbId','Drug Name','PdbId']]
drp_abs_paper_final=drp_abs_paper_final[['DrugPdbId','AbstractId','Abstract','Paper Title','Paper Doi']]



pdb_drug_association.to_csv("drug_pdb_association.csv", index=False,encoding='utf-8')
drp_abs_paper_final.to_csv("drug_pdb_abstract_paper.csv",index=False,encoding='utf-8')


