# -*- coding: utf-8 -*-

from clusters.clusterfeatures import ClusterFeatures
import numpy as np

class Cluster(object):
    """
        Estrutura para acesso, leitura e atualizações dos dados do conjunto,
        assim como também suas características estatísticas
    """
    centroide = None
    
    def __init__(self, dataset, centroide):
        self.buffering = dataset
        self.centroide = centroide
        self.clusterFeat = ClusterFeatures()
    

    def InicializaEstatisticas(self):
        self.clusterFeat.CalSomaLinear(self.buffering)
        self.clusterFeat.CalSquare(self.buffering)

    def AtualizaEstatisticas(self):
        self.clusterFeat.AtualizaEstatistica(self.buffering)
    

    def PrintDataSet(self):
        for item in self.buffering:
            print (item) 
    

    def AtualizaDados(self, new_item):
        if(new_item not in self.buffering):
            self.dataset.np.append(new_item)
    

    def AcessaDado(self, posicao):
        return self.dataset[posicao]
