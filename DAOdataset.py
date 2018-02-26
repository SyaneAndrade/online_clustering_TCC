from ClusterFeatures import *

class DAOdataset(object):
    """
        Estrutura para acesso, leitura e atualizações dos dados do conjunto,
        assim como também suas características estatísticas
    """
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.clusterFeat = ClusterFeatures(len(dataset))

    def InicializaEstatisticas(self):
        self.clusterFeat.CalSomaLinear(self.dataset)
        self.clusterFeat.CalSquare(self.dataset)

    def AtualizaEstatisticas(self):
        self.clusterFeat.AtualizaEstatistica(self.dataset)

    def PrintDataSet(self):
        for item in self.dataset:
            print(item)
        
    def AtualizaDados(self, new_item):
        if(new_item not in self.dataset.values):
            self.dataset.append(new_item)

    def AcessaDado(self, posicao):
        return self.dataset[posicao]
