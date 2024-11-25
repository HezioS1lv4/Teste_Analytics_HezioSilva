# Análise de Dados de Vendas - Projeto Simulado

Este projeto simula um dataset de vendas e realiza análises exploratórias, gerando insights e visualizações úteis. 
O objetivo é fornecer exemplos práticos de limpeza de dados, análise exploratória e criação de gráficos utilizando Python.

## Estrutura do Repositório

- `dataset.csv`: Arquivo contendo os dados simulados (após a limpeza).
- `grafico_linha_tendencia_vendas`: Gráfico de linha mostrando a tendência de vendas mensais em 2023.
- `grafico_pizza_produtos`: Gráfico de pizza com a distribuição percentual dos produtos mais vendidos.
- `gráfico de barras empilhadas`: Gráfico de Barras Empilhadasa detalhando a quantidade mensal de vendas para cada produto.
- `analytics_python_heziosilva.py`: Script principal que executa a geração, limpeza e análise dos dados.
- `README.md`: Este arquivo, explicando o projeto.

## Como Executar os Scripts

1. Clone este repositório para sua máquina local:
    ```bash
    git clone <url-do-repositorio>
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd <nome-do-diretorio>
    ```

3. Instale as dependências necessárias:
    ```bash
     pip install -r requirements.txt

    ```

4. Execute o script principal:
    ```bash
    python analytics_python_heziosilva.py
    ```

## Dependências

- `pandas`: Manipulação e análise de dados.
- `numpy`: Suporte para operações numéricas.
- `matplotlib`: Geração de gráficos.
- `seaborn`: Estilização e gráficos estatísticos.

## Suposições Feitas

1. **Simulação dos Dados**:
    - Os produtos, categorias e preços foram gerados aleatoriamente para fins de demonstração.
    - As datas de vendas abrangem o período de 01/01/2023 a 31/12/2023.

2. **Limpeza dos Dados**:
    - Valores nulos na coluna `Quantidade` foram preenchidos com a média da coluna.
    - Valores nulos na coluna `Preço` foram preenchidos com a média da coluna.

3. **Análises Realizadas**:
    - Calculou-se o total de vendas para cada produto e mês.
    - Identificou-se os meses com maior e menor volume de vendas.

## Resultados

Os gráficos e arquivos gerados oferecem uma visão clara das vendas ao longo do ano de 2023, permitindo insights úteis para tomadas de decisão.

---

**Autor:** Hézio S. dos Santos
