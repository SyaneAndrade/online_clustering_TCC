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
    

    def AtualizaEstatisticas(self):
        self.clusterFeat.CalSomaLinear(self.dataset)
        self.clusterFeat.CalSquare(self.dataset)
        self.clusterFeat.tamanho(self.dataset)
    

    def PrintDataSet(self):
        for item in self.dataset:
            print (item) 
    

    def AtualizaDados(self, new_item):
        # if(new_item not in self.dataset):
        if(len(self.dataset) > 0):
            self.dataset = np.append(self.dataset, new_item,  axis=0)
        else:
            self.dataset = new_item
    

    def AcessaDado(self, posicao):
        return self.dataset[posicao]
