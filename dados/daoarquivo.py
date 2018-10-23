# -*- coding: utf-8 -*-
import pandas as pd
import sklearn.preprocessing
from random import randint
import numpy as np

"""
    DAO do arquivo, tem como parametro o caminho do arquivo
    fazendo a leitura do csv e retornando todo o conjunto de dados
"""
class DAOarquivo(object):
    dados = None
    pont_inicial = 0
    pont_final = 0
    dados_particionado = None
    num_part = None
    dataset = None
    particao = None
    _rowAcess = []
    randon_data = []
    randon_dados = None


    def __init__(self, caminho_arquivo):
        self.arquivo = caminho_arquivo


    def calcula_particao(self, num_part):
        self.batch = round(len(self.dataset) / num_part)
        self.num_part = num_part
    

    def pega_particao(self):
        self.pont_inicial = self.pont_final
        self.pont_final = self.pont_final + self.batch
        if(self.pont_final >= len(self.dataset)):
            self.pont_final = len(self.dataset)
        self.particao = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final, 0:4].values)
        if(self.pont_final == len(self.dataset)):
            return False
        return True

    def LerArquivo(self):
        self.dataset = pd.read_csv(self.arquivo, sep= '|')


    def inicia_dados(self):
        self.LerArquivo()
        self.pont_inicial = 0
        self.pont_final = self.batch
        self.dados = self.normaliza_dados(self.dataset.iloc[:, 0:4].values)
        self.particao = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final, 0:4].values)
        self.cria_aleatorio()
        return True

    
    def normaliza_dados(self, dados):
        minmax_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
        return minmax_scaler.fit_transform(dados)
        return dados

    def cria_aleatorio(self):
        data = []
        index = 0
        while(index < self.batch):
            pos = randint(0, len(self.dataset) - 1)
            if(data == []):
                data.append(self.dados[pos,:])
                self._rowAcess.append(pos)
                # return True
            else:
                if(pos in self._rowAcess):
                    continue
                else:
                    data.append(self.dados[pos])
                    self._rowAcess.append(pos)
            index = index + 1
        self.randon_data = np.array(data)
        if(self.randon_dados is None):
            self.randon_dados = self.randon_data
        else:
            self.randon_dados = np.append(self.randon_dados, self.randon_data, axis=0)
            if(len(self.randon_dados) == len(self.dados)):
                return False
        return True
