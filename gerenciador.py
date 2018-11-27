# -*- coding: utf-8 -*-
from clusters.cluster import Cluster
from clusters.clusterfeatures import ClusterFeatures
from dados.daoarquivo import DAOarquivo
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from algoritimosclustering.simplekmeans import SimpleKmeansPython
from algoritimosclustering.simplekmeansmake import SimplePassKmeans
from algoritimosclustering.birch import BirchAlgo
from algoritimosclustering.leader import TheLeaderAlgorithm

class Gerenciador(object):
    """
        Classe responsável por gerenciar as funções necessárias
        Basicamente para não explicitar todas as funções existentes na main
    """
    daoIO = None
    executa = False

    def __init__(self, num_cluster):
        self.simple_kmeans = SimpleKmeansPython(num_cluster)
        self.sp_kmeans = SimplePassKmeans(num_cluster)
        self.birch = BirchAlgo(threshold=1.0)
        self.leader = TheLeaderAlgorithm(threshold=4.5)
    

    # Responsável por iniciar os dados vindo do csv
    def inicia_dataset(self, caminho, particao_final = 10):
        self.daoIO = DAOarquivo(caminho)
        self.daoIO.LerArquivo()
        self.daoIO.calcula_particao(particao_final)
        self.daoIO.inicia_dados()
        self.simple_kmeans.verdadeira_estatistica(self.daoIO.dados)
        if(particao_final > 1):
            self.executa = True


    def novo_data_stream(self):
        # self.executa = self.daoIO.pega_particao()
        self.executa = self.daoIO.cria_aleatorio()
        self.simple_kmeans.atualiza_kmeans(self.daoIO.randon_data)
        self.sp_kmeans.aplica_kmeans(self.daoIO.randon_data)
        self.birch.aplica_birch(self.daoIO.randon_data)
        self.leader.aplica_leader(self.daoIO.randon_data)
        # self.criarCluster()


    def plot_grafico_clustering(self, labels, centers, name):
        plt.scatter(self.daoIO.randon_dados[:, 0], self.daoIO.randon_dados[:,1], s = 100, c = labels)
        plt.scatter(centers[:, 0], centers[:, 1], s = 300, marker='*', c= 'red', label='Centroids')
        plt.title('Iris ' + name + ' Clustering Algorithm')
        plt.xlabel('petal length in cm')
        plt.ylabel('petal width in cm')
        plt.legend()
        plt.show()


    def criarCluster(self):

        #Kmeans do scitlearn
        dadosOrganizados = self.pegaClustersOrganizados(self.daoIO.randon_data, self.simple_kmeans.labels_temporary, self.simple_kmeans.centers)
        self.preencherClusters(dadosOrganizados, self.simple_kmeans)

        #Kmeans baseado de um codigo na internet
        dadosOrganizados = self.pegaClustersOrganizados(self.daoIO.randon_data, self.sp_kmeans.labels, self.sp_kmeans.centers)
        self.preencherClusters(dadosOrganizados, self.sp_kmeans)

        #Birch do scitlearn
        dadosOrganizados = self.pegaClustersOrganizados(self.daoIO.randon_data, self.birch.labels, self.birch.centers)
        self.preencherClusters(dadosOrganizados, self.birch)

        #Leader baseado em um algoritimo na internet
        dadosOrganizados = self.pegaClustersOrganizados(self.daoIO.randon_data, self.leader.labels, self.leader.centers)
        self.preencherClusters(dadosOrganizados, self.leader)
    

    def preencherClusters(self, dadosOrganizados, algoritmoCluster):
        if(algoritmoCluster.clusters == []):
            for cluster in dadosOrganizados:
                novoCluster = Cluster(np.array(dadosOrganizados[cluster]['dados']), dadosOrganizados[cluster]['centroid'])
                algoritmoCluster.clusters.append(novoCluster)
        else:
            for index in  range(0, len(algoritmoCluster.clusters)):
                algoritmoCluster.clusters[index].AtualizaDados(np.array(dadosOrganizados[index]['dados']))
                algoritmoCluster.clusters[index].centroide = dadosOrganizados[index]['centroid']

    
    def pegaClustersOrganizados(self, dadosRecebidos, labels, centroids):
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
    

    # Aplica o kmeans no conjunto de dados
    def iniciar(self):
        # kmeans biblioteca do python
        self.simple_kmeans.aplica_kmeans(self.daoIO.randon_data)
        # Baseado no do amiguinho
        self.sp_kmeans.inicia_kmeans(self.daoIO.randon_data)
        self.sp_kmeans.aplica_kmeans(self.daoIO.randon_data)
        #BIRCH
        self.birch.aplica_birch(self.daoIO.randon_data)
        #The Leader alghortm
        self.leader.aplica_leader(self.daoIO.randon_data)


    def mostra_estatisticas(self):
        self.simple_kmeans.estatisticas()
