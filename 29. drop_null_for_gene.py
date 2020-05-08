import pandas as pd
import csv


disease_gene_common_abstract_for_gene_with_id = pd.read_csv("disease_gene_common_abstract_for_gene_with_id.csv")
disease_gene_common_abstract_for_gene_with_id = disease_gene_common_abstract_for_gene_with_id.dropna()
disease_gene_common_abstract_for_gene_with_id.to_csv("disease_gene_common_abstract_for_gene_with_id_dropnull.csv",index=False)

dg_abs_paper_final = pd.read_csv("dg_abs_paper_final.csv")
dg_abs_paper_final = dg_abs_paper_final.dropna(subset=['Disease Name','Approved symbol'])
dg_abs_paper_final.to_csv("dg_abs_paper_final_dropnull.csv",index=False)