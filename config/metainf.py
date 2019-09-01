# -*- coding: utf-8 -*-


dados = "P"
# numCluster = "K"
results = "GT"

# lista = ["constraceptive", "german", "optic", "pageblocks", "satellite", "magic", "yeast"]
lista = ["magic"] #, "yeast"]

# numCluster = [3, 2, 2, 10, 5, 7, 10]

numCluster = [2] #, 10]

numPart = 1

threshholdBirch = [0.25]  #0.209] #0.2037821906368138120]

threshholdLeader = [2.1]#0.95]#, 0.68]

valoresParaAlgoritmos = {
  "constraceptive": Info("constraceptive", 0, 0, 3),
  "german": Info("german", 0, 0, 2),
  "optic": Info("optic", 0, 0, 10),
  "pageblocks": Info("pageblocks", 0, 0, 5),
  "satellite": Info("satellite", 0, 0, 7),
  "magic": Info("magic", 0, 0, 2),
  "yeast": Info("yeast", 0, 0, 10)
}


class Info:
  def __init__(self, name, threshholdBirch, threshholdLeader, numCluster):
    self.name = name
    self.threshholdBirch = threshholdBirch
    self.threshholdLeader = threshholdLeader
    self.numCluster = numCluster


