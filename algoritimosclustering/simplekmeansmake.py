# -*- coding: utf-8 -*-
import numpy as np
from clusters.cluster import Cluster

class SimplePassKmeans(object):
    clusters  = []
    labels = []
    labels_temporary = None
    data = None
    centers = None
    cluster_counts = None


    def __init__(self, num):
        self.num_clusters = num

    def inicia_kmeans(self, dados):
        n = np.size(dados, 0)
        randon_centers =np.random.choice((0, n - 1), self.num_clusters)
        self.centers = dados[randon_centers]
        self.cluster_counts = np.zeros(self.num_clusters)

    
    def aplica_kmeans(self, dados):
        labels_temporary  = []
        for item in dados:
            cluster = self.k_means_update(item)
            self.labels.append(cluster)
            self.labels_temporary.append(cluster)
        
        
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
        for cluster in range(self.num_clusters):
            cluster_distances[cluster] = sum(np.sqrt((point - self.centers[cluster])**2))
        c = np.argmin(cluster_distances)
        self.cluster_counts[c] += 1
        self.centers[c] += 1.0/self.cluster_counts[c]*(point - self.centers[c])
        return c