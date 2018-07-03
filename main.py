# -*- coding: utf-8 -*-
from dados.DAOarquivo import *
from dados.DAOdataset import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Responsável por iniciar os dados vindo do csv
def inicia_dataset(caminho):
    daoIO = DAOarquivo(caminho)
    iris = daoIO.LerArquivo()
    dados = iris.iloc[:, 0:4].values
    return dados

# Calculo dos cluters features ainda não utilizado, não sei bem como utilizar ainda, creio que ocorrerá mudanças
def cria_estatisticas(dados):
    DatasetFeatures = DAOdataset(dados)
    DatasetFeatures.InicializaEstatisticas()
    for item in DatasetFeatures.clusterFeat.SS:
        print item

# Plota o grafico resultante da aplicação do kmeans no conjuto de dados
def plot_grafico(dados, kmeans):
    plt.scatter(dados[:, 0], dados[:,1], s = 100, c = kmeans.labels_)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, marker= '*', c = 'red',label = 'Centroids')
    plt.title('Iris Clusters and Centroids')
    plt.xlabel('petal length in cm')
    plt.ylabel(' petal width in cm')
    plt.legend()
    plt.show()
 
# Aplica o kmeans no conjunto de dados
def aplica_kmeans(dados):
    kmeans = KMeans(n_clusters = 3, init = 'random')
    kmeans.fit(dados)
    print kmeans.cluster_centers_
    print kmeans.labels_
    print len(kmeans.labels_)
    plot_grafico(dados, kmeans)


def main():
    caminho = 'dados/mock/iris-dataset.csv'
    dados = inicia_dataset(caminho)
    aplica_kmeans(dados)


if __name__ == '__main__':
    main()
