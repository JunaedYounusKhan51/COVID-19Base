## Basic Info
This repo contains the implementation of COVID-19Base.

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

## Code
You will find the codes of this project under the 'code and data' directory. The codes are organised in a sequential manner.

You need to download the datasets from corresponding source (please follow the 'Materials Used' section for sources) and keep them in the same folder with the codes before running. You will have to rename (or format) them as mentioned in the codes.

## Resulting Database (Knowledgebase)
The latest version of the resulting database can be found in the 'resulting database (knowledgebase)' directory which contains the following files:
* Drug_disease_interaction.xlsx (contains drug disease interactions with effectiveness measure)
* Drug_SideEffects.xlsx (contains side-effects for different drugs)
* disease_hgnc_association.xlsx (contains disease gene associations with confidence level)
* disease_miRNA_association.xlsx (contains disease miRNA associations with confidence level)
* drug_pdb_association.xlsx (contains drug pdb associations)

The previous version(s) of the knowledgebase can be found in the 'previous versions' folder under the 'resulting database (knowledgebase)' directory.
