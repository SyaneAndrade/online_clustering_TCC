# -*- coding: utf-8 -*-
from copy import deepcopy

class BestOneElementsMovesOnline(object):
    
    dict_contagem_pares = {}
    agrupamento_escolhido = None
    quantidade_classes = 0

    def __init__(self, tipos_agrupamentos):
        self.tipos_agrupamentos = tipos_agrupamentos
        self.quantidade_agrupamentos = len(self.tipos_agrupamentos)

    def get_pares(self, key1, key2):
        if key1 in self.dict_contagem_pares:
            return self.dict_contagem_pares[key1]
        elif key2 in self.dict_contagem_pares:
            return self.dict_contagem_pares[key2]
        else: 
            return None

    def atualiza(self, labels, best_of_k):
        self.agrupamento_escolhido = best_of_k
        self.index_agrupamento_escolhido = self.tipos_agrupamentos.index(self.agrupamento_escolhido)
        self.quantidade_classes = max(labels) if max(labels) > self.quantidade_classes else self.quantidade_classes
        self.somas_distancias = []
        self.__somaDasDistancias(labels)

    def __somaDasDistancias(self, labels):
        for classe in range(0, self.quantidade_classes + 1):
            soma_distancia = 0
            labels[self.index_agrupamento_escolhido] = classe
            for i in range(0, self.quantidade_agrupamentos):
                if i != self.index_agrupamento_escolhido:
                    key1 = self.tipos_agrupamentos[self.index_agrupamento_escolhido] + "_" + self.tipos_agrupamentos[i]
                    key2 = self.tipos_agrupamentos[i] + "_" + self.tipos_agrupamentos[self.index_agrupamento_escolhido]
                    contagem_pares = deepcopy(self.get_pares(key1, key2))
                    if contagem_pares.alg1 == self.tipos_agrupamentos[i]:
                        contagem_pares.atualiza(labels[self.index_agrupamento_escolhido], labels[i])
                    else:
                        contagem_pares.atualiza(labels[i], labels[self.index_agrupamento_escolhido])
                    soma_distancia += contagem_pares.rand_index
            self.somas_distancias.append(soma_distancia)
    
    def getBestElementMoves(self):
        distancia_minima = min(self.somas_distancias)
        self.best_element = self.somas_distancias.index(distancia_minima)
        return self.best_element
