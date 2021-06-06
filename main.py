# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from gerenciador import Gerenciador
from helper.funcoesaux import convertMatCsv
from config.metainf import *


def main():
    # Caminho onde se encontra o conjunto de dados
    caminho = "dados/mock/" + dataset +"/"+ dataset + dados + ".csv"
    print(dataset)
    print("Carregando os dados no caminho: {}". format(caminho))
    # Cria um objeto do tipo gerenciador já inicializando os parametros necessários
    gerenciador = Gerenciador(caminho)
    # Numero de cluster para os algoritimos de clusterização de dados
    num_cluster = numCluster
    tsbirch = threshholdBirch
    tsLeader = threshholdLeader
    # Cria um df dos dados retirados do csv
    gerenciador.inicia(num_cluster, tsbirch, tsLeader)
    gerenciador.iniciaDataset(numPart)
    gerenciador.iniciar(False)
    while(gerenciador.executa):
        gerenciador.novoDataStream(False)
    # Salva os resultados
    gerenciador.finalizador(dataset)
    print("Labels MV")
    print(gerenciador.marjorityvoting.labels)
    print("Labels BoK")
    print(gerenciador.bok.labels)
    print("Labels BOEM")
    print(gerenciador.boem.labels)
    print("Labels BIRCH")
    print(len(list(gerenciador.birch.labels)))
    print("Labels K-Means")
    print(list(gerenciador.simple_kmeans.labels))
    print("Labels Leader")
    print(gerenciador.leader.labels)

def convert():
    convertMatCsv("dados/mat_datasets/", dataset, ".mat")


if __name__ == '__main__':
    main()
