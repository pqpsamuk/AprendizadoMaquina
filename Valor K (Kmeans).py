import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv')
data.head()
X, y = make_blobs(n_samples=150, n_features=2,centers=4, cluster_std=0.2,shuffle=True)
wcss = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters = 5)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
print(wcss)
