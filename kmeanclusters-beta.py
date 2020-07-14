#Write by: Claudio Quevedo G.
#Date: 13-07-2020
#Reason: Data Mining
from sklearn.metrics import pairwise_distances_argmin
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D


def find_clusters(X, n_clusters, rseed=2):
    # 1. Randomly choose clusters
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    while True:
        # 2a. Assign labels based on closest center
        labels = pairwise_distances_argmin(X, centers)
        # 2b. Find new centers from means of points
        new_centers = np.array([X[labels == i].mean(0)
                                for i in range(n_clusters)])
        # 2c. Check for convergence
        if np.all(centers == new_centers):
            break
        centers = new_centers
    return centers, labels


# 3a. read the datasets
datasets = pd.read_csv('datasets',sep=';')
records = []
for i in range(0, 50):
    records.append([datasets.values[i,j] for j in range(0, 6)])
#3b. declare number of clusters
n_clusters = 3
#4. Transform to dataframe
df = DataFrame(records,columns=['a','b','c','d','e','f'])
#5. Transform to numpy array
X = np.array(df[['b','c','d','e']])
#6. Call find_clusters function
centroids, labels = find_clusters(X, n_clusters)
#7. Generating clusters
cluster1 = []
cluster2 = []
cluster3 = []
for cluster,state in zip(labels,records):
    #print(cluster,state[0])
    if (cluster == 0):
        cluster1.append(state[0])
    elif (cluster == 1):
        cluster2.append(state[0])
    else:
        cluster3.append(state[0])
print("Cluster 1\n")
print(cluster1)
print("\n\nCluster 2\n")
print(cluster2)
print("\n\nCluster 3\n")
print(cluster3)


#8. Graph 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1],X[:,2]+X[:,3],c=labels,s=50)
ax.scatter(centroids[:, 0], centroids[:, 1],centroids[:,2], c='black', s=200, alpha=0.5)
ax.set_xlabel('Population')
ax.set_ylabel('Infected')
ax.set_zlabel('Recovered')
plt.show()
