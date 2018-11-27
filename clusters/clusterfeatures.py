# -*- coding: utf-8 -*-
import math
import numpy as np

class ClusterFeatures(object):
    """
    Representação compacta do conjunto de dados, contendo
    estatísticas suficientes, composta por:
    N -> quantidade de itens no conjunto de dados
    SS -> vetor de mesma dimensão dos dados contendo a soma dos quadrados dos N itens
    LS -> vetor de mesma dimensão dos dados contendo a soma linear dos N itens
    """
    
    SS = None
    LS = None
    N = 0
    Raio = 0
    Centroide = None

    # Método responsável por calcular a soma dos quadrados de todos os itens no vetor SS
    def CalSquare(self, data):
       self.SS = np.sum(np.square(data), axis=0)

    #Método responsável por calcular a soma dos quadrados de todos os itens no vetor LS
    def CalSomaLinear(self, data):
       self.LS = np.sum(data, axis=0)
    
    def tamanho(self, data):
        self.N = len(data)

    """
    Se um novo item x é adcionado ao conjunto de dados
    as estatísticas sobre o mesmo é atualizado como:
    N = N + 1
    LSi = LSi + x
    SSi = SSi + x^2
    """
    def AtualizaEstatistica(self, data):
        if(len(data) > self.N):
            self.SS.append(self.SS[self.N - 1] + pow(data[self.N], 2))
            self.LS.append(self.LS[self.N - 1] + data[self.N])
            self.N = len(data)
            return True
        return False
