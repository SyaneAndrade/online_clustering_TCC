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
lista = ["constraceptive"] #, "yeast"]

# numCluster = [3, 2, 2, 10, 5, 7, 10]

numCluster = [3] #, 10]

numPart = 0

threshholdBirch = [5]  #0.209] #0.2037821906368138120]

# threshholdLeader = [19.66]#0.95]#, 0.68]
threshholdLeader = [19.9999999999999982236406]#[19.99999999999999822365 0.95]#, 0.68]

valoresParaAlgoritmos = {
  "constraceptive": Info("constraceptive", 5, 19.9999999999999982236406, 3), # Leader não esta correto
  #"german": Info("german", 37, 150, 2), # CERTO JA
  #"optic": Info("optic", 33.33, 235, 10), # CERTO JA
  #"pageblocks": Info("pageblocks", 11950, 50000, 5), # CERTO JA
  # "satellite": Info("satellite", 87.565, 660, 7), # CERTO JA
  # "magic": Info("magic", 0.25, 2.1, 2), # CERTO JA
  # "yeast": Info("yeast", 0.28, 1.07, 10) # CERTO JA
}



