# -*- coding: utf-8 -*-
#!_/usr/bin/python
from dados.daoarquivo import DaoArquivo


class DataProcess(object):
    randon_part_data = None
    part_data = None
    part = None
    num_part = None
    start = 0
    end = 0

    def __init__(self, path):
        self.daoIO = DaoArquivo(path)

    
    def calcula_particao(self, num_part):
        self.part = round(len(self.daoIO.dataset) / num_part)
        self.num_part = num_part
    

    def pega_particao(self):
        self.start = self.end
        self.end = self.end + self.start
        if(self.end >= len(self.dataset)):
            self.end = len(self.dataset)
        self.part_data = self.dataset.iloc[self.start:self.end, 0:4].values
        if(self.end == len(self.dataset)):
            return False
        return True

    
    def inicia_dados(self):
        self.LerArquivo()
        self.end = 0
        self.end = self.part
        self.dataset = self.dataset.iloc[:, 0:4].values
        # self.particao = self.normaliza_dados(self.dataset.iloc[self.pont_inicial:self.pont_final, 0:4].values)
        self.cria_aleatorio()
        return True


    def cria_aleatorio(self):
            data = []
        for index in range(0, self.batch):
            pos = randint(0, len(self.dataset) - 1)
            if(self.particao == None):
                data.append(self.dados[pos,:])
                self._rowAcess.append(pos)
                # return True
            else:
                if(pos in self._rowAcess):
                    continue
                else:
                    data.append(self.dados[pos])
                    self._rowAcess.append(pos)
                    if(len(self._rowAcess) == len(self.dados)):
                        return False
        self.randon_data = np.array(data)
        if(self.randon_dados is None):
            self.randon_dados = self.randon_data
        else:
            self.randon_dados = np.append(self.randon_dados, self.randon_data, axis=0)
            if(len(self.randon_dados) == len(self.dados)):
                return False
        return True