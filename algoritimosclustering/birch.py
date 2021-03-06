# -*- coding: utf-8 -*-

from sklearn.cluster import Birch
import numpy as np

class BirchAlgo(object):

    labels = None
    clusters = []
    centers = None
    labels_temporary = None
    
    def __init__(self, threshold = 0.2):
        self.birch = Birch(threshold=threshold, n_clusters=None, compute_labels=True)
        self.n_cluster = None
    

    def aplica_birch(self, dados):
        self.birch.partial_fit(dados)
        if (self.labels is None):
            self.labels = self.birch.labels_
            self.labels_temporary = self.birch.labels_
        else:
            self.labels = np.append(self.labels, self.birch.labels_)
            self.labels_temporary = self.birch.labels_
        self.centers = self.birch.subcluster_centers_
        return self.labels_temporary

    def atualiza_kmeans(self, dados):
        self.aplica_birch(dados)


"""
    Examples :
        https://github.com/scikit-learn/scikit-learn/issues/6794
        https://programtalk.com/python-examples/sklearn.cluster.birch.Birch/
"""
    
