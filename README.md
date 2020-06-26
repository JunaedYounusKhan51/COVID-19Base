# COVID-19Base: A knowledgebase to explore biomedical entities related to COVID-19
## Basic Info
This repo contains the implementation of COVID-19Base.

## COVID-19Base
It is the first comprehensive knowledgebase to find the associations of seven different thematic areas related to COVID-19/SARS-CoV-2 and other coronavirus-related diseases in humans. While careful manual curation of the identified associations is the ultimate goal, in COVID-19Base, we implement a novel approach to estimate the effectiveness of drug for diseases based on natural language processing, sentiment analysis, and deep learning. We also apply the concept of cosine similarity to confidently infer the associations between diseases and genes, lncRNAs, miRNAs. It will support the researcher around the world to discover the existing knowledge and find a solution for this pandemic.

## Requirements
* Python
* Numpy
* Pandas
* Keras
* tqdm

## Materials Used
* CORD-19 Dataset (https://pages.semanticscholar.org/coronavirus-research)
* Disease Onotology (https://disease-ontology.org/)
* DrugBank (https://www.drugbank.ca/)
* HGNC (https://www.genenames.org/)
* LNCipedia (https://lncipedia.org/)
* miRBase (http://www.mirbase.org/)
* DisGeNET (https://www.disgenet.org/)
* Protein Data Bank (https://www.rcsb.org/)
* SIDER (http://sideeffects.embl.de/)

## Techniques/Algorithms Used
* String Matching Algorithm (Aho-corasick)
* Natural Language Processing
* Sentiment Analysis
* Deep Learning
* Cosine Similarity

## Methods
* Extracting entity names in dictionary-based approach using Aho-corasick algorithm
* Extracting pairs(associations) using co-occurance based approach
* Measuring effectiveness of drug-disease interaction using TextBlob, unsupervised sentiment analysis and Neural Network Model
* Measuring confidence level of disease-gene,miRNA,lncRNA associations using cosine similarity concept
* Extracting drug-pdb associations on abstract level
* Extracting side-effects associated with drugs from SIDER

## Code
You will find the codes of this project under the 'code and data' directory. The codes are organised in a sequential manner.

You will need to download the datasets from corresponding source (please follow the 'Materials Used' section for sources) and keep them in the same folder with the codes before running. You will have to rename (or format) them as mentioned in the codes.

## Resulting Database (Knowledgebase)
The resulting database can be found in the 'resulting database (knowledgebase)' directory which contains the following files:
* Drug_disease_interaction.xlsx (contains drug disease interactions with effectiveness measure)
* Drug_SideEffects.xlsx (contains side-effects for different drugs)
* disease_hgnc_association.xlsx (contains disease gene associations with confidence level)
* disease_miRNA_association.xlsx (contains disease miRNA associations with confidence level)
* drug_pdb_association.xlsx (contaions drug pdb associations)
