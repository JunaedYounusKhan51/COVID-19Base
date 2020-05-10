import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans

word_vectors = Word2Vec.load("word2vec.model").wv

model = KMeans(n_clusters=2, max_iter=1000, random_state=True, n_init=50).fit(X=word_vectors.vectors)

word_vectors.similar_by_vector(model.cluster_centers_[0], topn=10, restrict_vocab=None)

positive_cluster_center = model.cluster_centers_[0]
negative_cluster_center = model.cluster_centers_[1]


words = pd.DataFrame(np.array([list(word_vectors.vocab.keys())]).T)
print("words df done!")
words.columns = ['words']
words['vectors'] = words.words.apply(lambda x: word_vectors.wv[f'{x}'])
words['cluster'] = words.vectors.apply(lambda x: model.predict([np.array(x)]))
words.cluster = words.cluster.apply(lambda x: x[0])

words['cluster_value'] = [1 if i==0 else -1 for i in words.cluster]
words['closeness_score'] = words.apply(lambda x: 1/(model.transform([x.vectors]).min()), axis=1)
words['sentiment_coeff'] = words.closeness_score * words.cluster_value

words[['words', 'sentiment_coeff']].to_csv('sentiment_dictionary.csv', index=False)