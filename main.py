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
    gerenciador.inicia_dataset(caminho)
    # Aplica o algoritimo kmenas nos dados
    gerenciador.aplica_kmeans()

    #Plota o grafico mostrando a distribuição dos dados nos clusters
    gerenciador.plot_grafico()

    caminho = 'dados/mock/iris-dataset.csv'
    gerenciador.inicia_dataset(caminho, 150)
    # Aplica o algoritimo kmenas nos dados
    gerenciador.novo_data_stream()
    #Plota o grafico mostrando a distribuição dos dados nos clusters
    gerenciador.plot_grafico()

if __name__ == '__main__':
    main()


    # https://gist.github.com/yjzhang/aaf460849a4398422785c0e85932688d
