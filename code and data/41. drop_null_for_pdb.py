import pandas as pd
import csv


drug_pdb_common_abstract_for_pdb_with_id = pd.read_csv("drug_pdb_common_abstract_for_pdb_with_id.csv")
drug_pdb_common_abstract_for_pdb_with_id = drug_pdb_common_abstract_for_pdb_with_id.dropna()
drug_pdb_common_abstract_for_pdb_with_id.to_csv("drug_pdb_common_abstract_for_pdb_with_id_dropnull.csv",index=False)

dg_abs_paper_final = pd.read_csv("drp_abs_paper_final.csv")
print(len(dg_abs_paper_final))
dg_abs_paper_final = dg_abs_paper_final.dropna(subset=['Drug Name','PdbId'])
print(len(dg_abs_paper_final))
dg_abs_paper_final.to_csv("drp_abs_paper_final_dropnull.csv",index=False)