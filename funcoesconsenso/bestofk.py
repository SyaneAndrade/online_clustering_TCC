# -*- coding: utf-8 -*-

from medidassimilaridade.contagempares import ContagemParesOnline
import numpy as np

class BestOfKOnline(object):
    dict_contagem_pares = {}
    matriz_distancia = None
    soma_distancia = None
    __labels = None
    best_algo = None

    def __init__(self, tipos_agrupamentos):
        self.tipos_agrupamentos = tipos_agrupamentos
        self.quantidade_algo = len(tipos_agrupamentos)
        self.matriz_distancia = np.zeros((self.quantidade_algo, self.quantidade_algo))
        for i in range(0, len(tipos_agrupamentos)):
            for j in range (0, len(tipos_agrupamentos)):
                if i < j:
                    break
                if self.tipos_agrupamentos[i] != self.tipos_agrupamentos[j]:
                    key1 = self.tipos_agrupamentos[i] + "_" + self.tipos_agrupamentos[j]
                    key2 = self.tipos_agrupamentos[j] + "_" + self.tipos_agrupamentos[i]
                    if not self.get_pares(key1, key2):
                        self.dict_contagem_pares[key1] = ContagemParesOnline(self.tipos_agrupamentos[i], self.tipos_agrupamentos[j])

    def get_pares(self, key1, key2):
        if key1 in self.dict_contagem_pares:
            return self.dict_contagem_pares[key1]
        elif key2 in self.dict_contagem_pares:
            return self.dict_contagem_pares[key2]
        else: 
            return None

    def __atualizaContagemPares(self, labels):
        for i in range(0, self.quantidade_algo):
            for j in range (0, self.quantidade_algo):
                if i < j:
                    break
                if self.tipos_agrupamentos[i] != self.tipos_agrupamentos[j]:
                    key1 = self.tipos_agrupamentos[i] + "_" + self.tipos_agrupamentos[j]
                    key2 = self.tipos_agrupamentos[j] + "_" + self.tipos_agrupamentos[i]
                    contagem_pares = self.get_pares(key1, key2)
                    if contagem_pares.alg1 == self.tipos_agrupamentos[i]:
                        contagem_pares.atualiza(labels[i], labels[j])
                    else:
                        contagem_pares.atualiza(label[j], labels[i])

    def __atualizaMatrizDistancia(self):
        for i in range(0,self.quantidade_algo):
            for j in range (0, self.quantidade_algo):
                if i < j:
                    break
                if self.tipos_agrupamentos[i] != self.tipos_agrupamentos[j]:
                    key1 = self.tipos_agrupamentos[i] + "_" + self.tipos_agrupamentos[j]
                    key2 = self.tipos_agrupamentos[j] + "_" + self.tipos_agrupamentos[i]
                    distancia = self.get_pares(key1, key2).rand_index
                    self.matriz_distancia[i, j] = self.matriz_distancia[j, i] = distancia
    
    def __somaDistancia(self):
        self.soma_distancia = np.ravel(self.matriz_distancia.sum(axis=1))

    def atualiza(self, labels):
        self.__atualizaContagemPares(labels)
        self.__atualizaMatrizDistancia()
        self.__somaDistancia()
        self.__labels = labels

    def getBestK(self):
        distancia_minima = min(self.soma_distancia)
        index_algo = np.where(self.soma_distancia == distancia_minima)[0][0]
        self.best_algo = self.tipos_agrupamentos[index_algo]
        return self.__labels[index_algo]
