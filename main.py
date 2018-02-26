from DAOarquivo import *
from DAOdataset import *

def main():
    daoArquivo = DAOarquivo("caminho")
    dataset = daoArquivo.LerArquivo()
    daoDataset = DAOdataset(dataset)
    daoDataset.PrintDataSet
    return 0



if __name__ == '__main__':
    main()
    