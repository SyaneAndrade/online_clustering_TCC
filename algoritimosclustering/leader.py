# -*- coding: utf-8 -*-
import numpy as np
from clusters.cluster import Cluster

class TheLeaderAlgorithm(object):
    clusters  = []
    labels = []
    labels_temporary = None
    data = None
    _centers = []
    centers = None
    cluster_counts = []


    def __init__(self, threshold = 0.5, num  = 0):
        self.num_clusters = num
        self.threshold = threshold

    def inicia_leader(self, dados):
        n = np.size(dados, 0)

    
    def aplica_leader(self, dados):
        self.labels_temporary = []
        for item in dados:
            cluster = self.leader_update(item)
            self.labels.append(cluster)
            self.labels_temporary.append(cluster)
        self.centers = np.array(self._centers)
        
        
    def leader_update(self, point, cluster_counts = None):
        cluster_distances = np.zeros(self.num_clusters)
        cluster = 0
        if(self.num_clusters == 0):
            self._centers.append(point)
            self.cluster_counts.append(1)
            self.num_clusters += 1
            return cluster
        else:
            for clu in range(self.num_clusters):
                cluster_distances[clu] = sum(np.sqrt((point - self._centers[clu])**2))
            cluster = np.argmin(cluster_distances)
            if(cluster_distances[cluster] > self.threshold):
                self._centers.append(point)
                self.cluster_counts.append(1)
                self.num_clusters += 1
            else:
                self.cluster_counts[cluster] += 1
                if(point.dtype =='int64'):
                    adcionar = 1/self.cluster_counts[cluster]*(point - self._centers[cluster])
                    adcionar = adcionar.astype('int')
                    self._centers[cluster] += adcionar
                else:
                   self._centers[cluster] +=  1/self.cluster_counts[cluster]*(point - self._centers[cluster])
        return cluster
