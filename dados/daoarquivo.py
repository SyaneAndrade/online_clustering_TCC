# -*- coding: utf-8 -*-
import pandas as pd

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

    def __init__(self, caminho_arquivo):
        self.arquivo = caminho_arquivo


    def calcula_particao(self, num_part):
        self.batch = round(len(self.dataset) / num_part)
        self.num_part = num_part
    

    def pega_particao(self):
        # print(self.pont_inicial)
        # print(self.pont_final)
        self.pont_inicial = self.pont_final
        self.pont_final = self.pont_final + self.batch
        if(self.pont_final >= len(self.dataset)):
            self.pont_final = len(self.dataset)
        self.particao = self.dataset.iloc[self.pont_inicial:self.pont_final, 0:4].values
        if(self.pont_final == len(self.dataset)):
            return False
        return True

    def LerArquivo(self):
        self.dataset = pd.read_csv(self.arquivo, sep= '|')


    def inicia_dados(self):
        self.LerArquivo()
        self.pont_inicial = 0
        self.pont_final = self.batch
        self.dados = self.dataset.iloc[:, 0:4].values
        self.particao = self.dataset.iloc[self.pont_inicial:self.pont_final, 0:4].values
        return True
