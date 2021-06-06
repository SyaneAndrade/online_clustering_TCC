# -*- coding: utf-8 -*-
from clusters.clusterfeatures import ClusterFeatures
from dados.daoarquivo import DAOarquivo
from sklearn.cluster import KMeans
import numpy as np
from copy import deepcopy
from algoritimosclustering.simplekmeans import SimpleKmeansPython
from algoritimosclustering.simplekmeansmake import SimplePassKmeans
from algoritimosclustering.birch import BirchAlgo
from algoritimosclustering.leader import TheLeaderAlgorithm
from funcoesconsenso.marjorityvoting import MarjorityVoting
from funcoesconsenso.bestofk import BestOfKOnline
from funcoesconsenso.bestoneelementsmoves import BestOneElementsMovesOnline
from helper.funcoesaux import preencherClusters
from helper.funcoesaux import pegaClustersOrganizados
from helper.funcoesaux import criaTexto

class Gerenciador(object):
    """
        Classe responsável por gerenciar as funções necessárias
        Basicamente para não explicitar todas as funções existentes na main
    """
    daoIO = None
    executa = False
    simple_kmeans = None
    sp_kmeans = None
    birch = None
    leader = None
    marjorityvoting = None
    vote = None
    num_cluster = 0
    list_algo = ["kmeans", "birch", "leader"]

    def __init__(self, caminho):
        self.daoIO = DAOarquivo(caminho)

    def inicia(self, num_cluster, threshholdBirch, thresholdLeader):
        self.simple_kmeans = SimpleKmeansPython(num_cluster)
        self.sp_kmeans = SimplePassKmeans(num_cluster)
        self.birch = BirchAlgo(threshold=threshholdBirch)
        self.leader = TheLeaderAlgorithm(threshold=thresholdLeader)
        self.marjorityvoting = MarjorityVoting()
        self.bok = BestOfKOnline(self.list_algo)
        self.boem = BestOneElementsMovesOnline(self.list_algo)
        self.num_cluster = num_cluster
        self.daoIO.cluster = num_cluster
    

    # Responsável por iniciar os dados vindo do csv
    def iniciaDataset(self, particao_final = 10):
        self.daoIO.LerArquivo()
        self.daoIO.calcula_particao(particao_final)
        self.daoIO.inicia_dados()
        self.simple_kmeans.verdadeira_estatistica(self.daoIO.dados)
        if(particao_final > 1 or particao_final == 0):
            self.executa = True


    def novoDataStream(self, randon):
        if randon:
            self.executa = self.daoIO.cria_aleatorio()
            self.birch.aplica_birch(self.daoIO.randon_data)
            self.leader.aplica_leader(self.daoIO.randon_data)
            if(len(self.daoIO.particao_cluster) == self.num_cluster):
                self.simple_kmeans.atualiza_kmeans(self.daoIO.randon_data)
                self.sp_kmeans.aplica_kmeans(self.daoIO.randon_data)
                for i in range(self.num_cluster, 0, -1):
                    self.cria_vote(-i)
                    self.marjorityvoting.counting_votes(self.votes)
                    self.gerenciaBests(-i)
                self.criarCluster(True)
        else:
            self.executa = self.daoIO.pega_particao()
            self.birch.aplica_birch(self.daoIO.particao)
            #The Leader alghortm
            self.leader.aplica_leader(self.daoIO.particao)
            if(len(self.daoIO.particao_cluster) == self.num_cluster):
                self.simple_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                # Baseado no do amiguinho
                self.sp_kmeans.aplica_kmeans(self.daoIO.particao_cluster)

                for i in range((len(self.sp_kmeans.labels) - self.num_cluster),len(self.sp_kmeans.labels), 1):
                    self.cria_vote(i)
                    cluster = self.marjorityvoting.counting_votes(self.votes)
                    self.marjorityvoting.marjorityvoting(cluster)
                    self.gerenciaBests(i)
                self.criarCluster(False)
                self.daoIO.particao_cluster = None
            elif((len(self.daoIO.particao_cluster) > self.num_cluster) and self.executa == False):
                self.simple_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                # Baseado no do amiguinho
                self.sp_kmeans.aplica_kmeans(self.daoIO.particao_cluster)

                for i in range((len(self.sp_kmeans.labels) - len(self.daoIO.particao_cluster)),len(self.sp_kmeans.labels), 1):
                    self.cria_vote(i)
                    cluster = self.marjorityvoting.counting_votes(self.votes)
                    self.marjorityvoting.marjorityvoting(cluster)
                    self.gerenciaBests(i)
                self.criarCluster(False)
                self.daoIO.particao_cluster = None

    def cria_vote(self, pos):
        self.votes = np.array([self.simple_kmeans.labels[pos], self.birch.labels[pos], self.leader.labels[pos]])

    def gerenciaBests(self, pos):
        self.bok.atualiza([self.simple_kmeans.labels[pos], self.birch.labels[pos], self.leader.labels[pos]])
        self.bok.getBestK()
        self.boem.atualiza([self.simple_kmeans.labels[pos], self.birch.labels[pos], self.leader.labels[pos]], self.bok.best_algo)
        self.boem.getBestElementMoves()

    def criarCluster(self, randon):

        com_label = (len(self.birch.labels) - len(self.daoIO.particao_cluster))
        if randon:
        #Kmeans do scitlearn
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.randon_data, self.simple_kmeans.labels, self.simple_kmeans.centers)
            preencherClusters(dadosOrganizados, self.simple_kmeans)

                    #Kmeans baseado de um codigo na internet
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.randon_data, self.sp_kmeans.labels, self.sp_kmeans.centers)
            preencherClusters(dadosOrganizados, self.sp_kmeans)

            #Birch do scitlearn
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.randon_data, self.birch.labels, self.birch.centers)
            preencherClusters(dadosOrganizados, self.birch)

            #Leader baseado em um algoritimo na internet
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.randon_data, self.leader.labels, self.leader.centers)
            preencherClusters(dadosOrganizados, self.leader)
        else:
            #Kmeans do scitlearn
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.particao_cluster, self.simple_kmeans.labels[com_label:], self.simple_kmeans.centers)
            preencherClusters(dadosOrganizados, self.simple_kmeans)

            #Kmeans baseado de um codigo na internet
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.particao_cluster, self.sp_kmeans.labels[com_label:], self.sp_kmeans.centers)
            preencherClusters(dadosOrganizados, self.sp_kmeans)

            #Birch do scitlearn
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.particao_cluster, self.birch.labels[com_label:], self.birch.centers)
            preencherClusters(dadosOrganizados, self.birch)

            #Leader baseado em um algoritimo na internet
            dadosOrganizados = pegaClustersOrganizados(self.daoIO.particao_cluster, self.leader.labels[com_label:], self.leader.centers)
            preencherClusters(dadosOrganizados, self.leader)
    

    # Aplica o kmeans no conjunto de dados
    def iniciar(self, randon):
        # kmeans biblioteca do python
        if randon:
            #BIRCH
            self.birch.aplica_birch(self.daoIO.randon_data)
            #The Leader alghortm
            self.leader.aplica_leader(self.daoIO.randon_data)
            if(len(self.daoIO.particao_cluster) == self.num_cluster):
                self.simple_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                # Baseado no do amiguinho
                # self.sp_kmeans.inicia_kmeans(self.daoIO.randon_data)
                self.sp_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                cluster = self.marjorityvoting.counting_votes(self.votes)
                self.marjorityvoting.marjorityvoting(cluster)
                self.criarCluster(True)
                self.daoIO.particao_cluster = None
        else:
            #BIRCH
            self.birch.aplica_birch(self.daoIO.particao)
            #The Leader alghortm
            self.leader.aplica_leader(self.daoIO.particao)
            if(len(self.daoIO.particao_cluster) == self.num_cluster):
                self.simple_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                # Baseado no do amiguinho
                self.sp_kmeans.aplica_kmeans(self.daoIO.particao_cluster)
                self.marjorityvoting.counting_votes(self.votes)
                self.criarCluster(True)
                self.daoIO.particao_cluster = None


    def mostraEstatisticas(self):
        self.simple_kmeans.estatisticas()   

    def finalizador(self, dataset):
        caminho = "dados/mock/" + dataset + "/"
        criaTexto(self.simple_kmeans, "simple_pass_k_means_" + dataset, self.daoIO, caminho, True)

        criaTexto(self.sp_kmeans, "simple_pass_k_means_make_" + dataset, self.daoIO, caminho, True)

        criaTexto(self.birch, "birch_" + dataset, self.daoIO, caminho, True)

        criaTexto(self.leader, "leader_" + dataset, self.daoIO, caminho, True)

        criaTexto(self.boem, "boem_"+ dataset, self.daoIO, caminho, False)

        criaTexto(self.bok, "bok_" + dataset, self.daoIO, caminho, False)
        
        criaTexto(self.marjorityvoting, "marjorityvoting_" + dataset, self.daoIO, caminho, False)
