from medidassimilaridade.contagempares import ContagemParesOnline
from helper.funcoesaux import criaTexto
import pandas as pd
import numpy as np
from sklearn.metrics.cluster import rand_score, pair_confusion_matrix, contingency_matrix


def readLabels(path):
    return pd.read_csv(path)



def main(dataset, algo):
    caminho = "dados/mock/" + dataset + "/"
    path_verdade = caminho + dataset + "GT.csv"
    path_particao =  caminho + algo + "_" + dataset + "/" + algo + "_" + dataset + "_labels.csv"
    contagem_de_pares = ContagemParesOnline(dataset + '_labels_verdadeiro', algo)
    labels_verdadeiro = readLabels(path_verdade).to_numpy()
    labels_particao = readLabels(path_particao).to_numpy()
    labels_verdadeiro = labels_verdadeiro.flatten() - 1
    labels_particao = labels_particao.flatten()
    sk_rand_score = rand_score(labels_verdadeiro, labels_particao)
    sk_pair_confusion_matrix = pair_confusion_matrix(labels_verdadeiro, labels_particao)
    sk_contigencia = contingency_matrix(labels_verdadeiro, labels_particao)
    rand_index = []
    for index in range(len(labels_verdadeiro)):
        contagem_de_pares.atualiza(labels_verdadeiro[index], labels_particao[index])
        #print("Valores: {} {} index : {}".format(labels_verdadeiro[index], labels_particao[index], index))
        #print("Matriz confusao \n {}".format(contagem_de_pares.matriz_confusao))
        rand_index.append(contagem_de_pares.rand_index)
    dados_rand_index = pd.DataFrame(list(map(np.ravel, rand_index)))
    nomeArquivo =  algo + "_" + dataset + "/RI"
    dados_rand_index.to_csv(caminho + nomeArquivo + '.csv', index=False, header=False)
    print("RI Python {} {}: {}".format(dataset, algo, sk_rand_score))
    print("N's Python {} {}: \n{}".format(dataset, algo, sk_pair_confusion_matrix))
    # print("Contigencia's Python {} {}: \n{}".format(dataset, algo, sk_contigencia))
    print("RI {} {}: {}".format(dataset, algo, contagem_de_pares.rand_index))
    print("N's {} {}: \n{}".format(dataset, algo, contagem_de_pares.matriz_confusao_pares))
    # print("Contigencia's {} {}: \n{}".format(dataset, algo, contagem_de_pares.matriz_confusao))


if __name__ == '__main__':
    list_algo = ['simple_pass_k_means', 'simple_pass_k_means_make', 'leader', 'birch', 'bok', 'boem', 'marjorityvoting']
    for item in list_algo:
       main('optic', item)
