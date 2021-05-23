# -*- coding: utf-8 -*-
import pandas as pd
import sklearn.preprocessing
from random import randint
import numpy as np
import os

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
    particao_cluster = None
    _rowAcess = []
    randon_data = []
    randon_dados = None
    cluster = 0
    pont_final_cluster = 0


    def __init__(self, caminho_arquivo):
        self.arquivo = caminho_arquivo


    def calcula_particao(self, num_part):
        if num_part == 0:
            self.batch = 1
            self.num_part = num_part
        else:
            self.batch = round(len(self.dataset) / num_part)
            self.num_part = num_part

    def pega_particao(self):
        self.pont_inicial = self.pont_final
        self.pont_final = self.pont_final + self.batch
        self.pont_final_cluster = self.pont_final_cluster + self.batch
        if(self.pont_final >= len(self.dataset)):
            self.pont_final = len(self.dataset)
        self.particao = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final, 0:len(self.dataset[0])].values)
        if(self.pont_final_cluster <= len(self.dataset)):
            if self.particao_cluster is None:
                if((len(self.dataset) - (self.pont_final + 1)) < (self.cluster*2)):
                    self.pont_final_cluster = len(self.dataset)
                    self.particao_cluster = np.append(self.particao_cluster, self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster,  0:len(self.dataset[0])].values), axis=0)
                else:
                    self.particao_cluster = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster,  0:len(self.dataset[0])].values)
            else:
                if((len(self.dataset) - (self.pont_final + 1)) < (self.cluster*2)):
                    self.pont_final_cluster = len(self.dataset)
                    self.particao_cluster = np.append(self.particao_cluster, self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster,  0:len(self.dataset[0])].values), axis=0)
                else:
                    self.particao_cluster = np.append(self.particao_cluster, self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster,  0:len(self.dataset[0])].values), axis=0)
        if(self.pont_final == len(self.dataset)):
            return False
        return True

    def LerArquivo(self, caminho = None):
        if caminho == None:
            caminho = self.arquivo
            self.dataset = pd.read_csv(caminho, sep= '|', header= None)
        else:
            return pd.read_csv(caminho, sep='|', header = None)


    def inicia_dados(self):
        self.LerArquivo()
        self.pont_inicial = 0
        self.pont_final = self.batch
        self.pont_final_cluster = self.batch
        self.dados = self.normaliza_dados(self.dataset.iloc[:, 0:len(self.dataset[0])].values)
        self.particao = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final, 0:len(self.dataset[0])].values)
        if self.particao_cluster == None:
            self.particao_cluster = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster, 0:len(self.dataset[0])].values)
        else:
            self.particao_cluster.append(self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final_cluster, 0:len(self.dataset[0])].values))
        self.cria_aleatorio()
        return True

    
    def normaliza_dados(self, dados):
        minmax_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
        # return minmax_scaler.fit_transform(dados)
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


    def salvaArquivo(self, texto, nomeArquivo, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path + nomeArquivo + ".txt", "w") as arquivo:
            arquivo.write(texto)
            arquivo.close()
    
    def salvaCSV(self, dataframe, nomeArquivo, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        dataframe.to_csv(path + nomeArquivo + '.csv', index=False, header=False)
