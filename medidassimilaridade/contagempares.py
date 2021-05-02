# -*- coding: utf-8 -*-
import numpy as np

class ContagemParesOnline(object):

    def __init__(self, alg1, alg2):
        self.alg1 = alg1
        self.alg2 = alg2
        self.val_particao1 = None
        self.val_particao2 = None
        self.tamanho_dataset = 0
        self.cluster = np.array([])
        self.cluster_index = 0
        self.classes_index = 0
        self.classes = np.array([])
        self.index_part1 = None
        self.index_part2 = None
        self.matriz_confusao = None
        self.matriz_confusao_pares = np.zeros((2, 2))
    
    def atualizaValores(self, val_particao1, val_particao2):
        self.tamanho_dataset += 1
        self.particao1 = val_particao1
        self.particao2 = val_particao2
        index_part1 = list(zip(np.where(self.classes == self.particao1)[0]))
        index_part2 = list(zip(np.where(self.cluster == self.particao2)[0]))
        if(index_part1 == []):
           self.classes = np.append(self.classes, self.particao1)
           self.classes_index += 1
        if(index_part2 == []):
            self.cluster = np.append( self.cluster, self.particao2)
            self.cluster_index += 1
            
        self.index_part1 = np.where(self.cluster == self.particao1)[0][0]
        self.index_part2 = np.where(self.cluster == self.particao2)[0][0]

    def matrizConfusao(self):
        if self.matriz_confusao is None:
            self.matriz_confusao = np.zeros((self.classes_index, self.cluster_index))
        elif self.matriz_confusao.shape != (self.classes_index, self.cluster_index):
            self.matriz_confusao.resize((self.classes_index, self.cluster_index), refcheck=False)
        self.matriz_confusao[self.index_part1][self.index_part2] += 1

