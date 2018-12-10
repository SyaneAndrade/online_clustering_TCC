# -*- coding: utf-8 -*-
from clusters.cluster import Cluster
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scp


def preencherClusters(dadosOrganizados, algoritmoCluster):
    if(algoritmoCluster.clusters == []):
        for cluster in dadosOrganizados:
            novoCluster = Cluster(np.array(dadosOrganizados[cluster]['dados']), dadosOrganizados[cluster]['centroid'])
            novoCluster.AtualizaEstatisticas()
            algoritmoCluster.clusters.append(novoCluster)
    else:
        for index in  range(0, len(algoritmoCluster.clusters)):
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

def criaTexto(cluster, nomeAlgoritimo):
    texto = nomeAlgoritimo + "\n"
    for index in range(len(cluster)):
        texto += "\n\n\n\nCluster " + str(index) + "\n"
        texto += "DATASET\n" + str(cluster[index].dataset) + "\n"
        texto += "\n\nCluster Features " + str(index) + "\n"
        texto += "SS = " + str(cluster[index].clusterFeat.SS) + "\n"
        texto += "LS = " + str(cluster[index].clusterFeat.LS) + "\n"
        texto += "N = " + str(cluster[index].clusterFeat.N) + "\n"

    print(texto)
    return texto


def convertMatCsv(path, nomearquivo, extensao):
    data = scp.loadmat(path + nomearquivo + extensao)

    for i in data:
        if '__' not in i and 'readme' not in i:
            np.savetxt(("dados/mock/"+nomearquivo+"/"+nomearquivo+i+".csv"),data[i], fmt='%s',delimiter='|')
