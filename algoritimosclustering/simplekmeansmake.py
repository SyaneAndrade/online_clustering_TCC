# -*- coding: utf-8 -*-
import numpy as np
from clusters.cluster import Cluster

class SimplePassKmeans(object):
    clusters  = None
    labels = []
    data = None
    _centers = []
    centers = None
    cluster_counts = []


    def __init__(self, threshold = 0.5, num  = 0):
        # self.centers = randon_centers
        self.num_clusters = num
        self.threshold = threshold
        # for num_cluster in range(0, self.num_clusters):
        #     cluster = Cluster([])
        #     self.clusters.append(cluster)

    def inicia_kmeans(self, dados):
        n = np.size(dados, 0)
        # randon_centers =np.random.choice((0, n - 1), self.num_clusters)
        # self.centers = dados[randon_centers]
        # self.cluster_counts = np.zeros(self.num_clusters)

    
    def aplica_kmeans(self, dados):
        for item in dados:
            cluster = self.k_means_update(item)
            self.labels.append(cluster)
        self.centers = np.array(self._centers)
        
        
    def k_means_update(self, point, cluster_counts = None):
        """
    Does an online k-means update on a single data point.

    Args:
        point - a 1 x d array
        k - integer > 1 - number of clusters
        cluster_means - a k x d array of the means of each cluster
        cluster_counts - a 1 x k array of the number of points in each cluster
    Returns:
        An integer in [0, k-1] indicating the assigned cluster.

    Updates cluster_means and cluster_counts in place.

    For initialization, random cluster means are needed.
    """
        cluster_distances = np.zeros(self.num_clusters)
        c = 0
        if(self.num_clusters == 0):
            self._centers.append(point)
            self.cluster_counts.append(1)
            self.num_clusters += 1
            return c
        else:
            for cluster in range(self.num_clusters):
                cluster_distances[cluster] = sum(np.sqrt((point - self._centers[cluster])**2))
            c = np.argmin(cluster_distances)
            if(cluster_distances[c] > self.threshold):
                self._centers.append(point)
                self.cluster_counts.append(1)
                self.num_clusters += 1
            else:
                self.cluster_counts[c] += 1
                self._centers[c] += 1.0/self.cluster_counts[c]*(point - self._centers[c])
        return c
