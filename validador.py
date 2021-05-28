from medidassimilaridade.contagempares import ContagemParesOnline
import pandas as pd
import numpy as np
from sklearn.metrics.cluster import rand_score, pair_confusion_matrix, contingency_matrix
import statistics as sta

def readLabels(path):
    return pd.read_csv(path, header=None)

def main(dataset, algo, estastisticas_gerais):
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
    df = []
    for index in range(len(labels_verdadeiro)):
        contagem_de_pares.atualiza(labels_verdadeiro[index], labels_particao[index])
        rand_index.append(contagem_de_pares.rand_index)
        media = sta.mean(rand_index)
        desvio_padrao = sta.pstdev(rand_index)
        dados = [contagem_de_pares.rand_index, media, desvio_padrao]
        df.append(dados)
    dados_rand_index = pd.DataFrame(list(map(np.ravel, rand_index)))
    dados_estatististicos = pd.DataFrame(list(map(np.ravel, df)))
    nomeArquivo =  algo + "_" + dataset + "/" + algo + "_" + dataset + "_ri"
    dados_rand_index.to_csv(caminho + nomeArquivo + '.csv', index=False, header=False)
    nomeArquivo_dados = algo + "_" + dataset + "/" + algo + "_" + dataset + "_estastisticas"
    dados_estatististicos.to_csv(caminho + nomeArquivo_dados + '.csv', index=False, header=['rand_index', 'media', 'desvio_padrao'])
    print("RI Python {} {}: {}".format(dataset, algo, sk_rand_score))
    print("N's Python {} {}: \n{}".format(dataset, algo, sk_pair_confusion_matrix))
    print("Contigencia's Python {} {}: \n{}".format(dataset, algo, sk_contigencia))
    print("RI {} {}: {}".format(dataset, algo, contagem_de_pares.rand_index))
    print("N's {} {}: \n{}".format(dataset, algo, contagem_de_pares.matriz_confusao_pares))
    print("Contigencia's {} {}: \n{}".format(dataset, algo, contagem_de_pares.matriz_confusao))
    print('Média: {}'.format(media))
    print('Desvio Padrao: {}'.format(desvio_padrao))
    estastisticas_gerais.append([dataset, algo, contagem_de_pares.rand_index, media, desvio_padrao])



if __name__ == '__main__':
    list_databases = ["constraceptive", "german", "optic", "pageblocks", "satellite", "magic", "yeast"]
    list_algo = ['simple_pass_k_means', 'simple_pass_k_means_make', 'leader', 'birch', 'bok', 'boem', 'marjorityvoting']
    columns = ['databse', 'algorithm', 'rand_index', 'media', 'desvio_padrao']
    estastisticas_gerais = []
    for database in list_databases:
        for algo in list_algo:
           main(database, algo, estastisticas_gerais)
    estastisticas_gerais = pd.DataFrame(list(map(np.ravel, estastisticas_gerais)))
    estastisticas_gerais.to_csv('estatisticas_gerais.csv', index=False, header=columns)
    
