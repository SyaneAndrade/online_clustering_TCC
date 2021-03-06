# -*- coding: utf-8 -*-
import numpy as np

"""Classes responsável pela contagem de pares, método utilizado para calcular umas 
das as medidas de similaridade mais utilizadas em trabalhos correlatos"""
class ContagemParesOnline(object):

    def __init__(self, alg1, alg2):
        self.alg1 = alg1
        self.alg2 = alg2
        self.tamanho_dataset = 0
        self.cluster = np.array([])
        self.cluster_index = 0
        self.classes_index = 0
        self.classes = np.array([])
        self.__index_part1 = None
        self.__index_part2 = None
        self.matriz_confusao = None
        self.matriz_confusao_pares = np.zeros((2, 2))
        self.rand_index = None
        self.rand_index_ajustado = None
    
    # Chamada de todas as funções para atualização de variaveis/matriz e calculo da matriz de confusão de pares
    def atualiza(self, val_particao1, val_particao2):
        self.__atualizaValores(val_particao1, val_particao2)
        self.__matrizConfusao()
        self.__matrizConfusaoParesOnline()
        self.__randIndex()
        self.__adjustedRandIndex()
    
    # Mantém valores atualizados para a contagem de pares e matriz de confusão
    def __atualizaValores(self, val_particao1, val_particao2):
        self.tamanho_dataset += 1
        if(self.classes_index < (val_particao1 + 1)):
           acrescimo = (val_particao1 + 1) - self.classes_index
           self.classes_index += acrescimo
        if(self.cluster_index < (val_particao2 + 1)):
            acrescimo = (val_particao2 + 1) - self.cluster_index
            self.cluster_index += acrescimo
        # index para atualização na matriz de confusão
        self.__index_part1 =val_particao1
        self.__index_part2 =val_particao2
    
    def __redimensionaMatriz(self):
        nova_matriz = np.zeros((self.classes_index, self.cluster_index))
        linhas, colunas = self.matriz_confusao.shape
        for i in range(linhas):
            for j in range(colunas):
                nova_matriz[i][j] = self.matriz_confusao[i][j]
        return nova_matriz

    # Mantém a a matriz de confusão atualizada        
    def __matrizConfusao(self):
        if self.matriz_confusao is None:
            self.matriz_confusao = np.zeros((self.classes_index, self.cluster_index))
        # Caso exista uma nova classe ele da um resize na matriz
        elif self.matriz_confusao.shape != (self.classes_index, self.cluster_index):
            self.matriz_confusao = self.__redimensionaMatriz()
        # Soma +1 na posição dos index das classes 
        self.matriz_confusao[self.__index_part1][self.__index_part2] += 1

    # Calcula a matriz de confusão de pares conforme a matriz de confusão atualizada
    # Função baseada pair_confusion_matrix do sklearn
    def __matrizConfusaoParesOnline(self):
        soma_linhas = np.ravel(self.matriz_confusao.sum(axis=1))
        soma_colunas = np.ravel(self.matriz_confusao.sum(axis=0))
        soma_quadrados = np.square(self.matriz_confusao.data).sum()
        transposta_matriz_confusao = self.matriz_confusao.transpose()
        self.matriz_confusao_pares[1, 1] = soma_quadrados - self.tamanho_dataset
        self.matriz_confusao_pares[0, 1] = self.matriz_confusao.dot(soma_colunas).sum() - soma_quadrados
        self.matriz_confusao_pares[1, 0] = transposta_matriz_confusao.dot(soma_linhas).sum() - soma_quadrados
        self.matriz_confusao_pares[0, 0] = self.tamanho_dataset ** 2 -  self.matriz_confusao_pares[0, 1] - self.matriz_confusao_pares[1, 0] - soma_quadrados

    # Calcula o rand index conforme a matriz de confusão de pares
    # Função baseada rand_index do sklearn    
    def __randIndex(self):
        numerador = self.matriz_confusao_pares.diagonal().sum() 
        denominador = self.matriz_confusao_pares.sum()
        if numerador == denominador or denominador == 0:
            self.rand_index = 1.0
            return self.rand_index   
        self.rand_index = numerador / denominador
        return self.rand_index 
    
    # Calcula o adjusted rand index conforme a matriz de confusão de pares
    # Função baseada adjusted_rand_index do sklearn 
    def __adjustedRandIndex(self):
        (verdadeiro_negativo, falso_positivo), (falso_negativo, verdadeiro_positivo) = self.matriz_confusao_pares
        if falso_negativo == 0 and falso_positivo == 0:
            self.rand_index_ajustado = 1.0
            return self.rand_index_ajustado
        self.rand_index_ajustado = 2. * (verdadeiro_positivo * verdadeiro_negativo - 
                    falso_negativo * falso_positivo) / ((verdadeiro_positivo + falso_negativo) *
                                                        (falso_negativo + verdadeiro_negativo) +
                                                        (verdadeiro_positivo + falso_positivo) *
                                                        (falso_positivo + verdadeiro_negativo))
        return self.rand_index_ajustado
        
        
