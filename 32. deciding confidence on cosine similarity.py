import pandas as pd
import csv
from statistics import mode

dg_ext = pd.read_csv("Disease_Gene_Ext.csv",index_col=False)
dg_ext=dg_ext.drop_duplicates()

dg_cosine = pd.read_csv("disease_gene_interaction_cosine_sim.csv",index_col=False)
dg_cosine = dg_cosine[['DiseaseGeneId','Disease Name','Approved symbol','Cosine Similarity']].copy()




dg_ext['Disease Name'] = dg_ext['Disease Name'].str.lower()


merged_df=pd.merge(dg_cosine,dg_ext,on=['Disease Name','Approved symbol'])

merged_df = merged_df[['DiseaseGeneId','Disease Name','Approved symbol','Cosine Similarity']].copy()
merged_df=merged_df.drop_duplicates(subset=['Disease Name','Approved symbol'])
merged_df=merged_df.dropna()

dg_cosine['Found Flag'] = 0
merged_df['Found Flag'] =1

merged_df_known=merged_df[merged_df['Cosine Similarity'] != "UNKNOWN"]
cosine_similarity_known_list = merged_df_known['Cosine Similarity']
cosine_similarity_known_list = [float(x) for x in cosine_similarity_known_list] 

avg_cosine_known = sum(cosine_similarity_known_list) / len(cosine_similarity_known_list)
max_cosine_known=max(cosine_similarity_known_list)
min_cosine_known=min(cosine_similarity_known_list)


print("min known cosine:")
print(min_cosine_known)
print("avg known cosine:")
print(avg_cosine_known)
print("max known cosine:")
print(max_cosine_known)


main_df = dg_cosine.append(merged_df,ignore_index=True)
main_df = main_df.sort_values('Found Flag', ascending=False).drop_duplicates(subset=['Disease Name','Approved symbol'])

association_confidence_type_list = [] #A,B,C


for index,row in main_df.iterrows():
	association_confidence_type = "ERROR"
	found_flag = row['Found Flag']
	if found_flag == 1:
		association_confidence_type = 'Verified'
	else:
		this_cosine_similarity = row['Cosine Similarity']
		if this_cosine_similarity ==  "UNKNOWN":
			association_confidence_type = 'Low'
		else:
			this_cosine_similarity = float(this_cosine_similarity)
			distance_from_max_known = abs(max_cosine_known-this_cosine_similarity)
			distance_from_avg_known = abs(avg_cosine_known-this_cosine_similarity)
			distance_from_min_known = abs(min_cosine_known-this_cosine_similarity)
			min_distance=min(distance_from_max_known,distance_from_avg_known,distance_from_min_known)
			if  min_distance==distance_from_max_known:
				association_confidence_type = 'High'
			elif min_distance==distance_from_avg_known:
				association_confidence_type = 'Medium'
			elif min_distance==distance_from_min_known:
				association_confidence_type = 'Low'
	association_confidence_type_list.append(association_confidence_type)



main_df['Association Confidence Type'] = association_confidence_type_list

main_df.to_csv("gene_disease_association_with_confidence.csv",index=False)


