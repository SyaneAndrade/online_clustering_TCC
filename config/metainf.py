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
lista = ["magic"] #, "yeast"]

# numCluster = [3, 2, 2, 10, 5, 7, 10]

numCluster = [2] #, 10]

numPart = 0

threshholdBirch = [137]  #0.209] #0.2037821906368138120]

# threshholdLeader = [19.66]#0.95]#, 0.68]
threshholdLeader = [570]#[19.99999999999999822365 0.95]#, 0.68]

valoresParaAlgoritmos = {
  # "constraceptive": Info("constraceptive", 5, 11.3, 3), #Certo ja
  #"german": Info("german", 37, 100, 2), # Certo ja
  #"optic": Info("optic", 33.33, 45.5, 10), # Certo ja
  #"pageblocks": Info("pageblocks", 11950, 30000, 5), # Certo ja
  # "satellite": Info("satellite", 87.565, 135, 7), # Certo ja
  # "magic": Info("magic",137, 570, 2), # Certo ja
  # "yeast": Info("yeast", 0.28, 0.61, 10) # Certo ja
}



