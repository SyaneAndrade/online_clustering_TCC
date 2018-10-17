# -*- coding: utf-8 -*-

from sklearn.cluster import Birch
import numpy as np

class BirchAlgo(object):

    labels = None
    clusters = []
    centers = None
    
    def __init(self):
        self.birch = Birch(n_clusters=None)
        self.n_cluster = None
    

    def aplica_birch(self, dados):
        self.birch.partial_fit(dados)
        if (self.labels is None):
            self.labels = self.birch.labels_
        else:
            self.labels = np.append(self.labels, self.birch.labels_)
        self.centers = self.birch.subcluster_centers_
        self.T = self.birch.subcluster_labels_

    def atualiza_kmeans(self, dados):
        self.birch = Birch(n_clusters=self.n_cluster)
        self.aplica_birch(dados)


"""
    Examples :
        https://github.com/scikit-learn/scikit-learn/issues/6794
        https://programtalk.com/python-examples/sklearn.cluster.birch.Birch/
"""
    
