# -*- coding: utf-8 -*-


class Info:
  def __init__(self, name, threshholdBirch, threshholdLeader, numCluster):
    self.name = name
    self.threshholdBirch = threshholdBirch
    self.threshholdLeader = threshholdLeader
    self.numCluster = numCluster

dados = "P"
# numCluster = "K"
results = "GT"

# lista = ["constraceptive", "german", "optic", "pageblocks", "satellite", "magic", "yeast"]
lista = ["satellite"] #, "yeast"]

# numCluster = [3, 2, 2, 10, 5, 7, 10]

numCluster = [7] #, 10]

numPart = 0

threshholdBirch = [0.28]  #0.209] #0.2037821906368138120]

threshholdLeader = [1.07]#0.95]#, 0.68]

valoresParaAlgoritmos = {
  "constraceptive": Info("constraceptive", 0, 0, 3),
  "german": Info("german", 0, 0, 2),
  "optic": Info("optic", 0, 0, 10),
  "pageblocks": Info("pageblocks", 0, 0, 5),
  "satellite": Info("satellite", 0, 0, 7), # resultado para b=0.28 e l = 1.07 => qtdCentroids: {b: 6435, l: 6435}
  # "magic": Info("magic", 0.25, 2.1, 2), # CERTO JA
  # "yeast": Info("yeast", 0.28, 1.07, 10) # CERTO JA
}



