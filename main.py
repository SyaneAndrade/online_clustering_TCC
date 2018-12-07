# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from gerenciador import Gerenciador
from helper.funcoesaux import plotGraficoClustering
from helper.funcoesaux import criaTexto
from helper.funcoesaux import convertMatCsv



def main():
    # Caminho onde se encontra o conjunto de dados
    caminho = 'dados/mock/iris-dataset.csv'
    # Numero de cluster para os algoritimos de clusterização de dados
    num_cluster = 3
    # Cria um objeto do tipo gerenciador já inicializando os parametros necessários
    gerenciador = Gerenciador(num_cluster)
    # Cria um df dos dados retirados do csv
    gerenciador.iniciaDataset(caminho, 3)
    # Aplica o algoritimo kmenas nos dados
    gerenciador.iniciar()
    plotGraficoClustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn", gerenciador.daoIO.randon_dados)
    plotGraficoClustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me", gerenciador.daoIO.randon_dados)
    plotGraficoClustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH", gerenciador.daoIO.randon_dados)
    plotGraficoClustering(gerenciador.leader.labels, gerenciador.leader.centers, "The Leader Algorithm", gerenciador.daoIO.randon_dados)
    gerenciador.criarCluster()

    while(gerenciador.executa):
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        # Aplica o algoritimo kmenas nos dados
        gerenciador.novoDataStream()
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        plotGraficoClustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn",  gerenciador.daoIO.randon_dados)
        plotGraficoClustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me", gerenciador.daoIO.randon_dados)
        plotGraficoClustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH", gerenciador.daoIO.randon_dados)
        plotGraficoClustering(gerenciador.leader.labels, gerenciador.leader.centers, "The Leader Algorithm", gerenciador.daoIO.randon_dados)
        print('\n\n')
        gerenciador.criarCluster()
    gerenciador.finalizador()
    # gerenciador.mostra_estatisticas()


def convert():
    datasets = ["constraceptive", "german", "optic", "pageblocks", "satellite", "magic", "yeast"]
    for dataset in datasets:
        convertMatCsv("dados/mat_datasets/", dataset, ".mat")


if __name__ == '__main__':
    main()
    # convert()
    


    # https://gist.github.com/yjzhang/aaf460849a4398422785c0e85932688d

    # https://github.com/Hareric/ClusterTool

    # http://hareric.com/2016/07/06/%E4%B8%80%E8%B6%9F%E8%81%9A%E7%B1%BB(One-Pass%20Cluster)%E5%8F%8Apython%E5%AE%9E%E7%8E%B0/

    # https://github.com/yz-cnsdqz/dynamic_clustering
    
    # https://stackoverflow.com/questions/36928654/leader-clustering-algorithm-explanation