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

## Materials Used
* CORD-19 Dataset
* Disease Onotology
* DrugBank
* HGNC
* LNCipedia
* miRBase
* DisGeNET
* SIDER

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

