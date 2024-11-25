# Análise de Dados de Vendas - Projeto Simulado

Este projeto simula um dataset de vendas e realiza análises exploratórias, gerando insights e visualizações úteis. O objetivo é fornecer exemplos práticos de limpeza de dados, análise exploratória e criação de gráficos utilizando Python, além de demonstrar o processo de manipulação de dados em SQL para análise.

## Estrutura do Repositório


- **`pt1: Programação em Python`**
    - **`analytics_python_heziosilva.py`**: cript principal que executa a geração, limpeza e análise dos dados em Python.
        - `grafico_linha_tendencia_vendas`: Gráfico de linha mostrando a tendência de vendas mensais em 2023.
        - `grafico_pizza_produtos`: Gráfico de pizza com a distribuição percentual dos produtos mais vendidos.
        - `gráfico de barras empilhadas`: Gráfico de Barras Empilhadas detalhando a quantidade mensal de vendas para cada produto.

- **`pt2: SQL`**
    - **`scripts_sql/`**: Diretório contendo scripts SQL relacionados ao processo de importação e manipulação dos dados.
        - `Criacao_Tabela.sql`: Script para criação da tabela `Produtos` no banco de dados SQL Server.
        - `Insercao_Dados.sql`: Script com os comandos `INSERT INTO` para inserção dos dados de vendas na tabela `Produtos`.
        - `Consultas_Analiticas.sql`: Scripts de consultas SQL para análise de vendas, incluindo total de vendas por produto e mês, e produtos mais vendidos.

- **`pt3: Interpretação de Resultados`**
    - Resultados das consultas SQL que fornecem insights sobre os dados, como a tendência de vendas, os meses com maior e menor volume de vendas, e a distribuição dos produtos mais vendidos.
    - Explicações e análises sobre os gráficos gerados no Python, destacando os insights extraídos das visualizações.
    - Comparação dos resultados obtidos com as consultas SQL e as análises gráficas para verificar a consistência e validar os insights.


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

## Processamento no SQL

Além da análise em Python, os dados passaram por um processo de **importação e manipulação** dentro de um banco de dados SQL Server para facilitar a análise e a criação de relatórios. Abaixo estão as etapas realizadas no SQL:

1. Criação Banco de dados e Tabela
2. Inserção dos Dados
3. Consultas SQL para Análise

    
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
