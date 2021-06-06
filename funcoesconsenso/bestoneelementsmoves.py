# -*- coding: utf-8 -*-
from copy import deepcopy
from medidassimilaridade.contagempares import ContagemParesOnline

class BestOneElementsMovesOnline(object):
    dict_contagem_pares = {}
    agrupamento_escolhido = None
    quantidade_classes = 0
    labels = []
    __labels = None

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
        self.dict_contagem_pares_list = []
        self.__labels = labels
        for classe in range(0, self.quantidade_classes + 1):
            soma_distancia = 0
            labels[self.index_agrupamento_escolhido] = classe
            dict_pares = {}
            for i in range(0, self.quantidade_agrupamentos):
                if i != self.index_agrupamento_escolhido:
                    key1 = self.tipos_agrupamentos[self.index_agrupamento_escolhido] + "_" + self.tipos_agrupamentos[i]
                    key2 = self.tipos_agrupamentos[i] + "_" + self.tipos_agrupamentos[self.index_agrupamento_escolhido]
                    get_pares = self.get_pares(key1, key2)
                    if get_pares:
                        dict_pares[key1] = deepcopy(self.get_pares(key1, key2))
                        contagem_pares = dict_pares[key1]
                    else:
                        dict_pares[key1] = ContagemParesOnline(self.tipos_agrupamentos[self.index_agrupamento_escolhido], self.tipos_agrupamentos[i])
                        contagem_pares = dict_pares[key1]
                    if contagem_pares.alg1 == self.tipos_agrupamentos[i]:
                        contagem_pares.atualiza(labels[self.index_agrupamento_escolhido], labels[i])
                    else:
                        contagem_pares.atualiza(labels[i], labels[self.index_agrupamento_escolhido])
                    soma_distancia += contagem_pares.rand_index_ajustado
            self.somas_distancias.append(soma_distancia)
            self.dict_contagem_pares_list.append(deepcopy(dict_pares))
    
    def __atualizaAlgoEscolhido(self):
        dict_contagem_pares = deepcopy(self.dict_contagem_pares_list[self.best_element])
        for key1 in dict_contagem_pares:
            vector_key = key1.split("_")
            key2 = vector_key[1] + "_" + vector_key[0]
            contagem_pares = self.get_pares(key1, key2)
            if contagem_pares:
               contagem_pares = dict_contagem_pares[key1]
            else:
                self.dict_contagem_pares[key1] = dict_contagem_pares[key1]

    def __atualizaContagemPares(self):
        self.__atualizaAlgoEscolhido()
        list_algo = deepcopy(self.tipos_agrupamentos)
        list_algo.pop(self.index_agrupamento_escolhido)
        self.__labels.pop(self.index_agrupamento_escolhido)
        for i in range(0, len(list_algo)):
            for j in range (0, len(list_algo)):
                if i < j:
                    break
                if (list_algo[i] != list_algo[j]):
                    key1 = list_algo[i] + "_" + list_algo[j]
                    key2 = list_algo[j] + "_" + list_algo[i]
                    get_pares = self.get_pares(key1, key2)
                    if get_pares:
                        contagem_pares = get_pares
                    else:
                        self.dict_contagem_pares[key1] = ContagemParesOnline(self.tipos_agrupamentos[i], self.tipos_agrupamentos[j])
                        contagem_pares = self.dict_contagem_pares[key1]
                    if contagem_pares.alg1 == self.tipos_agrupamentos[i]:
                        contagem_pares.atualiza(self.__labels[i], self.__labels[j])
                    else:
                        contagem_pares.atualiza(self.__labels[j], self.__labels[i])

    def getBestElementMoves(self):
        distancia_minima = min(self.somas_distancias)
        self.best_element = self.somas_distancias.index(distancia_minima)
        self.labels.append(self.best_element)
        self.__atualizaContagemPares()
        return self.best_element
