# Agrupamento de dados Online via Combinação de Partição

Este repositório contem as implementações para fundamentar a pesquisa de adaptação de métodos de Agrupamento via Combinação de Partição no contexto de Agrupamento de Dados Online afim de aumentar a confiabiabilidade dos resultados.
O trabalho aqui em si, simula o stream de dados, fazendo uma classificação do dado por vez.

## Instalando dependencias
```bash
pip install -r requirements.txt
```
## Como usar

Para executar os agrupamentos desenvolvidos basta rodar:
```bash
python main.py
```
Para mudar o database que está sendo classificado, editar o arquivo : `conf/metainf.py` , a lista de dados disponiveis junto com esse trabalho:

* constraceptive
* german
* optic
* pageblocks
* satellite
* magic
* yeast

Essas bases são publicas e podem ser encontradas no [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

As configurações para cada dataset está em um comentário no `metainf.py`.
