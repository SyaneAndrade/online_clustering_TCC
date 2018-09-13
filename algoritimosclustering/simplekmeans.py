# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import sklearn.metrics as smetrics
import numpy as np
import pdb

class SimpleKmeansPython(object):
    clusters  = []
    centers = None
    labels = None
    T = None
    predict = None
    predict_centers = None
    predict_inertia = None


    def __init__(self, num_cluster):
        self.kmeans = KMeans(n_clusters=num_cluster, init='random')
        self.n_cluster = num_cluster

    def aplica_kmeans(self, dados):
        self.kmeans.fit(dados)
        if (self.labels is None):
            self.labels = self.kmeans.labels_
        else:
            # print("criacao labels")
            # print(self.labels)
            # print(self.kmeans.labels_)
            # print("\n")
            # print("label apos append")
            self.labels = np.append(self.labels, self.kmeans.labels_)
            # print(self.labels)
            # print("\n\n")
            # pdb.set_trace()
        self.centers = self.kmeans.cluster_centers_
        self.T = self.kmeans.cluster_centers_.T

    def atualiza_kmeans(self, dados):
        # self.kmeans = KMeans(n_clusters=self.n_cluster, init=self.centers)
        self.kmeans = KMeans(n_clusters=self.n_cluster, init=self.centers, n_init=10)
        self.aplica_kmeans(dados)
    
    def verdadeira_estatistica(self, dados):
        predict = self.kmeans.fit(dados)
        self.predict = predict.labels_
        self.predict_centers = predict.cluster_centers_
        self.predict_inertia = predict.inertia_


    def estatisticas(self):
        print("Centroides")
        print(self.centers)
        print("\nInertia")
        print(self.kmeans.inertia_)
        print("\nLabels")
        print(self.labels)
        print("\nAccuracy")
        print(smetrics.accuracy_score(self.predict, self.labels))
        print("\n\nDados Predict")
        print("\nCentroides")
        print(self.predict_centers)
        print("\nlabels")
        print(self.predict)
        print("\nInertia")
        print(self.predict_inertia)


        

        
