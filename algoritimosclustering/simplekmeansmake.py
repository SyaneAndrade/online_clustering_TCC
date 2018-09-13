# -*- coding: utf-8 -*-
import numpy as np
from clusters.cluster import Cluster

class SimplePassKmeans(object):
    clusters  = []
    labels = []
    data = None


    def __init__(self, randon_centers, num):
        self.centers = randon_centers
        self.num_clusters = num
        for num_cluster in range(0, self.num_clusters):
            cluster = Cluster([])
            self.clusters.append(cluster)

    
    def aplica_kmeans(self, dados):
        for item in dados:
            cluster = self.k_means_update(item, self.num_clusters, self.clusters)
            self.labels.append(c)
        
        
    def k_means_update(self, point, k, cluster_means, cluster_counts = None):
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
        cluster_distances = np.zeros(k)
        for cluster in range(k):
            cluster_distances[cluster] = sum(np.sqrt((point - cluster_means[cluster])**2))
        c = np.argmin(cluster_distances)
        if cluster_counts:
            cluster_counts[c] += 1
        cluster_means[c] += 1.0/cluster_counts[c]*(point - cluster_means[c])
        return c
