# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np

class SimpleKmeans(object):
    clusters  = []
    centers = None
    labels = []


    def __init__(self, num_cluster):
        self.kmeans = KMeans(n_clusters=num_cluster, init='random')
        self.n_cluster = num_cluster

    def aplica_kmeans(self, dados):
        self.kmeans.fit(dados)
        if (self.labels is None):
            self.labels = self.kmeans.labels_
        else:
            self.labels = np.append(self.kmeans.labels_, self.labels)
        self.centers = self.kmeans.cluster_centers_

    def atualiza_kmeans(self, dados):
        self.kmeans = KMeans(n_clusters=self.n_cluster, init=self.centers)
        self.aplica_kmeans(dados)

        
