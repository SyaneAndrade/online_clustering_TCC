# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from gerenciador import Gerenciador
from helper.funcoesaux import plotGraficoClustering
from helper.funcoesaux import criaTexto
from helper.funcoesaux import convertMatCsv
from config.metainf import *
import copy


def bateuMetaClusters (gerenciador, metaDeCluster):
    # simple_kmeans_clusters = gerenciador.simple_kmeans.centers
    # sp_kmeans_clusters = gerenciador.sp_kmeans.centers
    birch_clusters = gerenciador.birch.centers
    leader_clusters = gerenciador.leader.centers
    return (
        # simple_kmeans_clusters == metaDeCluster and
        # sp_kmeans_clusters == metaDeCluster and
        birch_clusters == metaDeCluster and
        leader_clusters == metaDeCluster
    )

def maiorQueMeta (gerenciador, metaDeCluster):
    birch_clusters = gerenciador.birch.centers
    leader_clusters = gerenciador.leader.centers
    return (birch_clusters > metaDeCluster or leader_clusters > metaDeCluster)

def menorQueMeta (gerenciador, metaDeCluster):
    return not maiorQueMeta(gerenciador, metaDeCluster)

def iniciaGerenciador(dataset, num_cluster, tsbirch, tsLeader, numPart):
    gerenciador = instanciarGerenciador(dataset)
    random = False
    gerenciador.inicia(num_cluster, tsbirch, tsLeader)
    gerenciador.iniciaDataset(numPart)
    gerenciador.criarCluster(random)
    gerenciador.iniciar(random)
    return gerenciador

def instanciarGerenciador(dataset):
    caminho = "dados/mock/" + dataset.name + "/" + dataset.name + dados + ".csv"
    print(dataset.name)
    gerenciador = Gerenciador(caminho)
    return gerenciador

def encontraValoresDasVariaveis (dataset, passoBirch = 0.1, passoLeader = 0.1):
    if (not dataset):
        print('Dataset não encontrado na estrutura que contem as informações dos mesmos')
    tsBirch = dataset.threshholdBirch
    tsLeader = dataset.threshholdBirch
    gerenciador = iniciaGerenciador(dataset, dataset.numCluster, tsBirch, tsLeader, numPart)
    metaCentroides = dataset.numCluster
    random = False
    gerenciador.novoDataStream(random)

    while(not bateuMetaClusters(gerenciador, metaCentroides)):
        if (maiorQueMeta(gerenciador, metaCentroides)):
            tsBirch += passoBirch
            tsLeader += passoLeader
        else:
            tsBirch -= passoBirch
            tsLeader -= passoLeader
        gerenciador = iniciaGerenciador(dataset, dataset.numCluster, tsBirch, tsLeader, numPart)
        gerenciador.novoDataStream(random)
    print(f'{tsBirch} {tsLeader}')




def main():
    # for key in valoresParaAlgoritmos:
    #     print(f'DATASET: {key}')
    #     caminhoDoDataset = "dados/mock/" + key + "/" + key + dados + ".csv"
    #     encontraValoresDasVariaveis(valoresParaAlgoritmos[key])
    for index in range(len(lista)):
        # Caminho onde se encontra o conjunto de dados
        caminho = "dados/mock/" + lista[index] +"/"+ lista[index] + dados + ".csv"
        print(lista[index])
        # Cria um objeto do tipo gerenciador já inicializando os parametros necessários
        gerenciador = Gerenciador(caminho)
        # Numero de cluster para os algoritimos de clusterização de dados
        num_cluster = numCluster[index]
        tsbirch = threshholdBirch[index]
        tsLeader = threshholdLeader[index]
        # Cria um df dos dados retirados do csv
        gerenciador.inicia(num_cluster, tsbirch, tsLeader)
        gerenciador.iniciaDataset(numPart)
        # Aplica o algoritimo kmenas nos dados
        # plotGraficoClustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn", gerenciador.daoIO.randon_dados)
        # plotGraficoClustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me", gerenciador.daoIO.randon_dados)
        # plotGraficoClustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH", gerenciador.daoIO.randon_dados)
        # plotGraficoClustering(gerenciador.leader.labels, gerenciador.leader.centers, "The Leader Algorithm", gerenciador.daoIO.randon_dados)
        gerenciador.iniciar(False)
        count = 1
        while(gerenciador.executa):
            #Plota o grafico mostrando a distribuição dos dados nos clusters
            # Aplica o algoritimo kmenas nos dados
            gerenciador.novoDataStream(False)
            #Plota o grafico mostrando a distribuição dos dados nos clusters
            count += 1
            print(str(count) + '\n\n')
        gerenciador.finalizador(lista[index])
        plotGraficoClustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH", gerenciador.daoIO.dados)
        plotGraficoClustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me", gerenciador.daoIO.dados)
        plotGraficoClustering(gerenciador.leader.labels, gerenciador.leader.centers, "The Leader Algorithm", gerenciador.daoIO.dados)
        plotGraficoClustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn",  gerenciador.daoIO.dados)
        # gerenciador.mostra_estatisticas()


def convert():
    for dataset in lista:
        convertMatCsv("dados/mat_datasets/", dataset, ".mat")


if __name__ == '__main__':
    main()
    # convert()



    # https://gist.github.com/yjzhang/aaf460849a4398422785c0e85932688d

    # https://github.com/Hareric/ClusterTool

    # http://hareric.com/2016/07/06/%E4%B8%80%E8%B6%9F%E8%81%9A%E7%B1%BB(One-Pass%20Cluster)%E5%8F%8Apython%E5%AE%9E%E7%8E%B0/

    # https://github.com/yz-cnsdqz/dynamic_clustering

    # https://stackoverflow.com/questions/36928654/leader-clustering-algorithm-explanation
