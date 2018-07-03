# -*- coding: utf-8 -*-
import pandas as pd

"""
    DAO do arquivo, tem como parametro o caminho do arquivo
    fazendo a leitura do csv e retornando todo o conjunto de dados
"""
class DAOarquivo(object):
    def __init__(self, caminho_arquivo):
        self.arquivo = caminho_arquivo


    def LerArquivo(self):
        dataset = pd.read_csv(self.arquivo, sep= '|')
        return dataset