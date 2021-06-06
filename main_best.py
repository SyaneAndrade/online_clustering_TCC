# -*- coding: utf-8 -*-
from funcoesconsenso.bestofk import BestOfKOnline
from funcoesconsenso.bestoneelementsmoves import BestOneElementsMovesOnline
import numpy as np

if __name__ == '__main__':
    list_algo = ["P1", "P2", "P3"]
    P1 = np.array([0, 0, 1, 2, 2])
    P2 = np.array([0, 1, 1, 2, 2])
    P3 = np.array([0, 1, 2, 1, 2])
    bok = BestOfKOnline(list_algo)
    boem = BestOneElementsMovesOnline(list_algo)
    for i in range(0, len(P1)):
        print(i)
        bok.atualiza([P1[i], P2[i], P3[i]])
        bok.getBestK()
        boem.atualiza([P1[i], P2[i], P3[i]], bok.best_algo)
        # print("Matriz de Confusão \n {} \n".format(dict_contagem.matriz_confusao))
        # print("Matriz de confusao de pares\n {} \n".format(dict_contagem.matriz_confusao_pares))
        # print("Rand Index\n {} \n".format(dict_contagem.rand_index))
        print("BOK")
        print("Matriz Distancia BoK \n {} \n".format(bok.matriz_distancia))
        print("Soma Distancia BoK \n {} \n".format(bok.soma_distancia))
        print("BestK {}".format(bok.getBestK()))
        print("Best Algo {}\n".format(bok.best_algo))
        print("\n\nBest one Elements Moves {}".format(boem.getBestElementMoves()))
        print("\n\nSoma das Distancias BOEM {}\n\n".format(boem.somas_distancias))
