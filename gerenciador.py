# -*- coding: utf-8 -*-
from clusters.cluster import Cluster
from clusters.clusterfeatures import ClusterFeatures
from dados.daoarquivo import DAOarquivo
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class Gerenciador(object):
    """
        Classe responsável por gerenciar as funções necessárias
        Basicamente para não explicitar todas as funções existentes na main
    """
    clusters = []
    dados = None

    def __init__(self, num_cluster):
        self.kmeans = KMeans(n_clusters=num_cluster, init='random')
                    

    # # Calculo dos cluters features ainda não utilizado, não sei bem como utilizar ainda, creio que ocorrerá mudanças
    # def cria_estatisticas(self, dados):
    #     DatasetFeatures = DAOdataset(dados)
    #     DatasetFeatures.InicializaEstatisticas()
    #     for item in DatasetFeatures.clusterFeat.SS:
    #         print item


    # Responsável por iniciar os dados vindo do csv
    def inicia_dataset(self, caminho, particao = 10):
        daoIO = DAOarquivo(caminho)
        iris = daoIO.LerArquivo()
        self.dados = iris.iloc[:particao, 0:4].values

    def novo_data_stream(self, novosDados = None):
        if not novosDados:
            novosDados = self.dados
        self.kmeans = KMeans(n_clusters=len(self.clusters), init=self.kmeans.cluster_centers_)
        self.dados = novosDados
        self.aplica_kmeans()
        

    # Plota o grafico resultante da aplicação do kmeans no conjuto de dados
    def plot_grafico(self):
        plt.scatter(self.dados[:, 0], self.dados[:,1], s = 100, c = self.kmeans.labels_)
        plt.scatter(self.kmeans.cluster_centers_[:, 0], self.kmeans.cluster_centers_[:, 1], s = 300, marker= '*', 
                    c = 'red',label = 'Centroids')
        plt.title('Iris Clusters and Centroids')
        plt.xlabel('petal length in cm')
        plt.ylabel(' petal width in cm')
        plt.legend()
        plt.show()
    
    def criarCluster(self, dados, centroids):
        return Cluster(dados)
    
    def preencherClusters(self, dadosOrganizados):
        for cluster in dadosOrganizados:
            novoCluster = self.criarCluster(dadosOrganizados[cluster]['dados'], 'Sem centroid')
            self.clusters.append(novoCluster)
    
    def pegaClustersOrganizados(self, dadosRecebidos, labels, centroids):
        qtdClusters = len(centroids)
        dadosAgregados = {}
        #instanciando o objeto
        for i in range(qtdClusters):
            dadosAgregados[i] = {
                'dados': []
                # centroid: False
            }
        # Colocando os dados
        for index in range(len(dadosRecebidos)):
            dadosAgregados[labels[index]]['dados'].append(dadosRecebidos[index])

        return dadosAgregados
    


    # Aplica o kmeans no conjunto de dados
    def aplica_kmeans(self):
        self.kmeans.fit(self.dados)
        print (self.dados)
        print (self.clusters)
        print ("Mostrando os centroides selecionados")
        print (self.kmeans.cluster_centers_)
        print ("\n\n")
        print ("Distribuição dos clusters nos dados")
        print (self.kmeans.labels_)
        print ("\n\n")
        print ("Objeto no fim")
        print ("\n\n")
        dadosOrganizados = self.pegaClustersOrganizados(self.dados, self.kmeans.labels_, self.kmeans.cluster_centers_)
        self.preencherClusters(dadosOrganizados)
        print('\n\n')
        print(self.clusters)