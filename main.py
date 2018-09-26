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
    # gerenciador.plot_grafico()
    # gerenciador.plot_grafico_kmeans()
    gerenciador.plot_grafico_radon()
    gerenciador.plot_grafico_radon_sp()

    while(gerenciador.executa):
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        # Aplica o algoritimo kmenas nos dados
        gerenciador.novo_data_stream()
        #Plota o grafico mostrando a distribuição dos dados nos clusters
        # gerenciador.plot_grafico()
        # gerenciador.plot_grafico_kmeans()
        gerenciador.plot_grafico_radon()
        gerenciador.plot_grafico_radon_sp()
        # print(gerenciador.simple_kmeans.centers)
        print('\n\n')
    gerenciador.mostra_estatisticas()


if __name__ == '__main__':
    main()


    # https://gist.github.com/yjzhang/aaf460849a4398422785c0e85932688d


#     [[ 7.7   3.    6.1   2.3 ]
#  [ 6.61  3.17  5.46  2.24]
#  [ 6.    2.8   5.    1.85]]


# [[ 6.85        3.07368421  5.74210526  2.07105263]
#  [ 5.9016129   2.7483871   4.39354839  1.43387097]
#  [ 5.006       3.428       1.462       0.246     ]]

