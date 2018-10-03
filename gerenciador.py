# -*- coding: utf-8 -*-
from clusters.cluster import Cluster
from clusters.clusterfeatures import ClusterFeatures
from dados.daoarquivo import DAOarquivo
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from algoritimosclustering.simplekmeans import SimpleKmeansPython
from algoritimosclustering.simplekmeansmake import SimplePassKmeans

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
        

    # Plota o grafico resultante da aplicação do kmeans no conjuto de dados
    def plot_grafico(self):
        plt.scatter(self.daoIO.dados[:self.daoIO.pont_final, 0], self.daoIO.dados[:self.daoIO.pont_final,1], s = 100, c = self.simple_kmeans.labels)
        plt.scatter(self.simple_kmeans.centers[:, 0], self.simple_kmeans.centers[:, 1], s = 300, marker= '*', 
                    c = 'red',label = 'Centroids')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('petal length in cm')
        plt.ylabel(' petal width in cm')
        plt.legend()
        plt.show()


    # Plota o grafico resultante da aplicação do kmeans no conjuto de dados
    def plot_grafico_radon(self):
        plt.scatter(self.daoIO.randon_dados[:, 0], self.daoIO.randon_dados[:,1], s = 100, c = self.simple_kmeans.labels)
        plt.scatter(self.simple_kmeans.centers[:, 0], self.simple_kmeans.centers[:, 1], s = 300, marker= '*', 
                    c = 'red',label = 'Centroids')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('petal length in cm')
        plt.ylabel(' petal width in cm')
        plt.legend()
        plt.show()
    

    def plot_grafico_radon_sp(self):
        plt.scatter(self.daoIO.randon_dados[:, 0], self.daoIO.randon_dados[:,1], s = 100, c = self.sp_kmeans.labels)
        plt.scatter(self.sp_kmeans.centers[:, 0], self.sp_kmeans.centers[:, 1], s = 300, marker= '*', 
                    c = 'red',label = 'Centroids')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('petal length in cm')
        plt.ylabel(' petal width in cm')
        plt.legend()
        plt.show()


    def plot_grafico_kmeans(self):
        plt.scatter(self.daoIO.dados[:self.daoIO.pont_final, 0], self.daoIO.dados[:self.daoIO.pont_final,1], s = 100, c = self.sp_kmeans.labels)
        plt.scatter(self.sp_kmeans.centers[:, 0], self.sp_kmeans.centers[:, 1], s = 300, marker= '*', 
                    c = 'red',label = 'Centroids')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('petal length in cm')
        plt.ylabel(' petal width in cm')
        plt.legend()
        plt.show()
    

    def criarCluster(self, dados, centroids):
        return Cluster(dados)
    

    def preencherClusters(self, dadosOrganizados):
        if(self.simple_kmeans.clusters is None):
            for cluster in dadosOrganizados:
                novoCluster = self.criarCluster(dadosOrganizados[cluster]['dados'], 'Sem centroid')
                self.simple_kmeans.clusters.append(novoCluster)
        else:
            for index in  range(0, len(self.simple_kmeans.clusters)):
                self.simple_kmeans.clusters.append(dadosOrganizados[index]['dados'])

    
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
            dadosAgregados[labels[index]]['dados'].append(dadosRecebidos[index])

        return dadosAgregados
    

    # Aplica o kmeans no conjunto de dados
    def iniciar(self):
        # kmeans biblioteca do python
        self.simple_kmeans.aplica_kmeans(self.daoIO.randon_data)
        # Baseado no do amiguinho
        self.sp_kmeans.inicia_kmeans(self.daoIO.randon_data)
        self.sp_kmeans.aplica_kmeans(self.daoIO.randon_data)

        dadosOrganizados = self.pegaClustersOrganizados(self.daoIO.randon_data, self.simple_kmeans.labels, self.simple_kmeans.centers)
        self.preencherClusters(dadosOrganizados)


    def mostra_estatisticas(self):
        self.simple_kmeans.estatisticas()