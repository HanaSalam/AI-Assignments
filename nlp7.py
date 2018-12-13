"""
1. Create a few sentences . Find the frequency count of the words in the vocabulary.
2. Cluster the words in the sentences  based on the count.
3. Modify the program to cluster sentences based on cosine similarity.
4. Visualise the results.
"""
from sklearn.cluster import KMeans
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np
fobj = plt.figure(figsize=(8,8))
plt1 = fobj.add_subplot(1,1,1)
doc = ["The game of life is a game of an everlasting learning. The unexamined life is not worth living. So never stop learning.",
       "Life is a like a game of chess changing with every move.",
       "Artificial intelligence (AI) is the ability of a computer program or a machine to think and learn."]
q2 = "The game of life"

dataset = [q2,doc]

"""
d1=TextBlob(doc)
for w in d1:
    print doc.words.count(w)
"""
tf = CountVectorizer(stop_words='english')
X = tf.fit_transform(doc)
print tf.vocabulary_
print tf.get_feature_names()
print X
print len(tf.get_feature_names())
print X.toarray()
X=X.toarray()
count = ([sum(X) for X in zip(*X)])
print count,tf.get_feature_names()
l1 = list(zip(count,tf.get_feature_names()))
for x,y in l1:
 print x,'-',y

dict1=tf.vocabulary_
Y = list(zip(dict1.values(),count))
model = KMeans(n_clusters=3)
model.fit_transform(Y)
"""

plt1.scatter(dict1.values(),count,c=model.labels_)
plt1.set_xlabel('values')
plt1.set_ylabel('count')
plt1.set_xticks(np.arange(len(dict1.values())))
plt1.set_xticklabels(dict1.keys(),rotation=30,fontsize='small')
plt.show()

"""

#3. Modify the program to cluster sentences based on cosine similarity.

tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(dataset)

cos1=cosine_similarity(matrix[0:1],matrix)

label = np.arange(len(dataset))
Z = list(zip(label,cos1.flatten()))
models=KMeans(Z)
models.fit(Z)
plt1.scatter(label,cos1,c=models.labels_)
plt.show()


