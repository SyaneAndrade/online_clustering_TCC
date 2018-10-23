# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from gerenciador import Gerenciador



def main():
    # Caminho onde se encontra o conjunto de dados
    caminho = 'dados/mock/iris-dataset.csv'
    # Numero de cluster para os algoritimos de clusterização de dados
    num_cluster = 3
    # Cria um objeto do tipo gerenciador já inicializando os parametros necessários
    gerenciador = Gerenciador(num_cluster)
    # Cria um df dos dados retirados do csv
    gerenciador.inicia_dataset(caminho, 3)
    # Aplica o algoritimo kmenas nos dados
    gerenciador.iniciar()
    gerenciador.plot_grafico_clustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn")
    gerenciador.plot_grafico_clustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me")
    gerenciador.plot_grafico_clustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH")

    while(gerenciador.executa):
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        # Aplica o algoritimo kmenas nos dados
        gerenciador.novo_data_stream()
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        gerenciador.plot_grafico_clustering(gerenciador.simple_kmeans.labels, gerenciador.simple_kmeans.centers, "Kmeans sklearn")
        gerenciador.plot_grafico_clustering(gerenciador.sp_kmeans.labels, gerenciador.sp_kmeans.centers, "Kmeans online mode make for me")
        gerenciador.plot_grafico_clustering(gerenciador.birch.labels, gerenciador.birch.centers, "BIRCH")
        print('\n\n')
    gerenciador.mostra_estatisticas()


if __name__ == '__main__':
    main()


    # https://gist.github.com/yjzhang/aaf460849a4398422785c0e85932688d

    # https://github.com/Hareric/ClusterTool

    # http://hareric.com/2016/07/06/%E4%B8%80%E8%B6%9F%E8%81%9A%E7%B1%BB(One-Pass%20Cluster)%E5%8F%8Apython%E5%AE%9E%E7%8E%B0/

    # https://github.com/yz-cnsdqz/dynamic_clustering
    