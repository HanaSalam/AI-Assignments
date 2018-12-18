"""
1.Apply K-Means clustering for the following dataset for two clusters and plot the result.
   dataset:{2,4,10,12,3,20,30,11,25}
"""

import scipy as sp
import numpy as np
from scipy.cluster.vq import vq,kmeans
import matplotlib.pyplot as plt

dataset = np.array([2,4,10,12,3,20,30,11,25])
dataset = sp.cast['f'](dataset)
center1,distance1 = kmeans(dataset,2)
print center1, distance1

cluster1,distance1 = vq(dataset,center1)
print cluster1
print dataset[cluster1==0]
print dataset[cluster1==1]
cx = np.arange(1,dataset.size+1)

c1 = dataset[cluster1==0]
c2 = dataset[cluster1==1]

plt.scatter(cx[cluster1==0],c1,color='r',label='cluster1')
plt.scatter(cx[cluster1==1],c2,color='b',label='cluster2')
plt.legend(loc='best')
plt.show()

