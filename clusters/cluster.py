# -*- coding: utf-8 -*-

from clusters.clusterfeatures import ClusterFeatures
import numpy as np

class Cluster(object):
    """
        Estrutura para acesso, leitura e atualizações dos dados do conjunto,
        assim como também suas características estatísticas
    """
    # centroide = None
    
    def __init__(self, dataset, centroide):
        self.dataset = dataset
        self.centroide = centroide
        self.clusterFeat = ClusterFeatures()
    

    def InicializaEstatisticas(self):
        self.clusterFeat.CalSomaLinear(self.dataset)
        self.clusterFeat.CalSquare(self.dataset)

    def AtualizaEstatisticas(self):
        self.clusterFeat.AtualizaEstatistica(self.dataset)
    

    def PrintDataSet(self):
        for item in self.dataset:
            print (item) 
    

    def AtualizaDados(self, new_item):
        # if(new_item not in self.dataset):
        self.dataset = np.append(self.dataset, new_item,  axis=0)
    

    def AcessaDado(self, posicao):
        return self.dataset[posicao]
