from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

def pcaFunction(data, dim):
    pca = PCA(n_components = dim)
    pca.fit(data)
    data_PCA = pca.transform(data)

    return data_PCA

def kmeans(data, clu):
    kmeans = KMeans(n_clusters=clu, n_init=10, init="k-means++")
    kmeans.fit(data)

    return kmeans, [kmeans.cluster_centers_]

def knn(data, knei, labels):
    neigh = KNeighborsClassifier(n_neighbors = knei)
    neigh.fit(data,labels)

    return neigh