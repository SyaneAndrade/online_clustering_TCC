# -*- coding: utf-8 -*-
from clusters.cluster import Cluster
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scp
import pandas as pd


def preencherClusters(dadosOrganizados, algoritmoCluster):
    if(algoritmoCluster.clusters == []):
        for cluster in dadosOrganizados:
            novoCluster = Cluster(np.array(dadosOrganizados[cluster]['dados']), dadosOrganizados[cluster]['centroid'])
            novoCluster.AtualizaEstatisticas()
            algoritmoCluster.clusters.append(novoCluster)
    elif(len(algoritmoCluster.clusters) < len(algoritmoCluster.centers)):
        for cluster in range(0, len(algoritmoCluster.centers)):
            if(cluster < len(algoritmoCluster.clusters)):
                if(len(dadosOrganizados[cluster]['dados']) > 0):
                    algoritmoCluster.clusters[cluster].AtualizaDados(np.array(dadosOrganizados[cluster]['dados']))
                algoritmoCluster.clusters[cluster].centroide = dadosOrganizados[cluster]['centroid']
                algoritmoCluster.clusters[cluster].AtualizaEstatisticas()
            else:
                novoCluster = Cluster(np.array(dadosOrganizados[cluster]['dados']), dadosOrganizados[cluster]['centroid'])
                novoCluster.AtualizaEstatisticas()
                algoritmoCluster.clusters.append(novoCluster)
    else:
        for index in  range(0, len(algoritmoCluster.clusters)):
            if(len(dadosOrganizados[index]['dados']) > 0):
                algoritmoCluster.clusters[index].AtualizaDados(np.array(dadosOrganizados[index]['dados']))
            algoritmoCluster.clusters[index].centroide = dadosOrganizados[index]['centroid']
            algoritmoCluster.clusters[index].AtualizaEstatisticas()

    
def pegaClustersOrganizados(dadosRecebidos, labels, centroids):
    qtdClusters = len(centroids)
    dadosAgregados = {}
    #instanciando o objeto
    for i in range(qtdClusters):
        dadosAgregados[i] = {
            'dados': [],
            'centroid': centroids[i]
        }
        # Colocando os dados
    for index in range(len(dadosRecebidos)):
        dadosAgregados[labels[index]]['dados'].append(dadosRecebidos[index,:])
    return dadosAgregados


def plotGraficoClustering(labels, centers, name, data):
    plt.scatter(data[:, 0],data[:,1], s = 100, c = labels)
    plt.scatter(centers[:, 0], centers[:, 1], s = 300, marker='*', c= 'red', label='Centroids')
    plt.title('Iris ' + name + ' Clustering Algorithm')
    plt.xlabel('petal length in cm')
    plt.ylabel('petal width in cm')
    plt.legend()
    plt.show()

def criaTexto(cluster, nomeAlgoritimo, daoIO, caminho, isCluster):
    texto = ""
    print(isCluster)
    if isCluster:
        for index in range(len(cluster.clusters)):
            texto += "\n\n\n\nCluster " + str(index) + "\n"
            texto += "\n\n\nCentroide" + str(cluster.clusters[index].centroide) + "\n\n"
            texto += "\n\nCluster Features " + str(index) + "\n"
            texto += "SS = " + str(cluster.clusters[index].clusterFeat.SS) + "\n"
            texto += "LS = " + str(cluster.clusters[index].clusterFeat.LS) + "\n"
            texto += "N = " + str(cluster.clusters[index].clusterFeat.N) + "\n"
            daoIO.salvaArquivo(texto, nomeAlgoritimo + "_cluster_features_" + str(index), caminho + nomeAlgoritimo + "/")
            dados_cluster = pd.DataFrame(list(map(np.ravel, cluster.clusters[index].dataset)))
            daoIO.salvaCSV(dados_cluster, nomeAlgoritimo + "_cluster_" + str(index), caminho + nomeAlgoritimo + "/")
            texto = ""
    dados_label = pd.DataFrame(list(map(np.ravel, cluster.labels)))
    daoIO.salvaCSV(dados_label, nomeAlgoritimo + "_labels", caminho + nomeAlgoritimo + "/")

    # print(texto)
    return texto

def convertMatCsv(path, nomearquivo, extensao):
    data = scp.loadmat(path + nomearquivo + extensao)

    for i in data:
        if '__' not in i and 'readme' not in i:
            np.savetxt(("dados/mock/"+nomearquivo+"/"+nomearquivo+i+".csv"),data[i], fmt='%s',delimiter='|')

