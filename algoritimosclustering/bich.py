# -*- coding: utf-8 -*-

from sklearn.cluster import Birch
import numpy as np

class BirchAlgo(object):

    labels = None
    clusters = []
    centers = None
    
    def __init(self):
        self.birch = Birch(n_clusters=None)
    
