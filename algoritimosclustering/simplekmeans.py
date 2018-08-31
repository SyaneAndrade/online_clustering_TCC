# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np
import pdb

class SimpleKmeans(object):
    clusters  = []
    centers = None
    labels = []
    T = None


    def __init__(self, num_cluster):
        self.kmeans = KMeans(n_clusters=num_cluster, init='random', max_iter=1000)
        self.n_cluster = num_cluster

    def aplica_kmeans(self, dados):
        self.kmeans.fit(dados)
        if (self.labels is None):
            self.labels = self.kmeans.labels_
        else:
            print("criacao labels")
            print(self.labels)
            print(self.kmeans.labels_)
            print("\n")
            print("label apos append")
            self.labels = np.append(self.labels, self.kmeans.labels_)
            print(self.labels)
            print("\n\n")
            pdb.set_trace()
        self.centers = self.kmeans.cluster_centers_
        self.T = self.kmeans.cluster_centers_.T

    def atualiza_kmeans(self, dados):
        # self.kmeans = KMeans(n_clusters=self.n_cluster, init=self.centers)
        self.kmeans = KMeans(n_clusters=self.n_cluster, init=self.centers, max_iter=1000, n_init=1)
        self.aplica_kmeans(dados)

        
