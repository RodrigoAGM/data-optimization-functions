from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

def pcaFunction(data, dim):
    pca = PCA(n_components = dim)
    pca.fit(data)
    data_PCA = pca.transform(data)

    return data_PCA

def kmeans_centers(data, clu):
    kmeans = KMeans(n_clusters=clu, n_init=10, init="k-means++")
    kmeans.fit(data)

    return list(kmeans.cluster_centers_)

def kmeans_predict(data, clu, newPoint):
    kmeans = KMeans(n_clusters=clu, n_init=10, init="k-means++")
    kmeans.fit(data)

    return kmeans.predict(newPoint)

def knn_predict(data, knei, labels, newPoint):
    neigh = KNeighborsClassifier(n_neighbors = knei)
    neigh.fit(data,labels)

    return neigh.predict(newPoint)