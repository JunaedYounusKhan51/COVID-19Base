import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial

def containsDigit(inputString):
	return any(char.isdigit() for char in inputString)

word_vectors = Word2Vec.load("word2vec_for_gene.model").wv

'''
temp1 = word_vectors['pulmonary_edema']
temp2 =word_vectors['hmgb1']
#print(word_vectors['cancer'])
print(cosine_similarity([temp1], [temp2]))
result = 1 - spatial.distance.cosine(temp1, temp2)
print(result)

print(word_vectors.similarity('pulmonary_edema', 'TES'))
'''


disease_gene_common_abstract_for_gene_with_id_dropnull = pd.read_csv("disease_gene_common_abstract_for_gene_with_id_dropnull.csv")

cosine_similarity_list = []

un = 0
lo=0
i = 0
for index, row in disease_gene_common_abstract_for_gene_with_id_dropnull.iterrows():
	i+=1
	print(i)
	disease= row['Disease Name']
	disease = disease.replace(' ','_')
	gene = row['Approved symbol']
	gene = gene.replace(' ','_')
	gene = gene.replace('-','_')
	gene= gene.replace('.','_')
	try:
		cosine_similarity = word_vectors.similarity(disease,gene)
	except:
		try:
			cosine_similarity = word_vectors.similarity(disease,gene.lower())
			lo+=1
		except:
			un+=1
			cosine_similarity = "UNKNOWN"
	cosine_similarity_list.append(cosine_similarity)

print("")
print(un)
print(lo)
disease_gene_common_abstract_for_gene_with_id_dropnull['Cosine Similarity'] = cosine_similarity_list
disease_gene_common_abstract_for_gene_with_id_dropnull.to_csv("disease_gene_interaction_cosine_sim.csv",index=False)
