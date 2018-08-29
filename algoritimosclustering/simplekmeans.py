# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans

class SimpleKmeans(object):
    clusters  = []
    centers = []
    labels = []


    def __init__(self, num_cluster):
        self.kmeans = KMeans(n_clusters=num_cluster, init='random', max_iter=1000)
        self.n_cluster = num_cluster

    def aplica_kmeans(self, dados):
        self.kmeans.fit(dados)
        self.centers = self.kmeans.cluster_centers_
        self.labels = self.kmeans.labels_


    def atualiza_kmeans(self, dados):
        self.kmeans = KMeans(n_clusters=len(self.clusters), init=self.centers, max_iter=1000)
        self.aplica_kmeans(dados)

        
