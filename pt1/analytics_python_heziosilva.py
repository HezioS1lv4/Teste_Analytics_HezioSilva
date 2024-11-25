# -*- coding: utf-8 -*-
"""Analytics Python- HezioSilva

Original file is located at
    https://colab.research.google.com/drive/1BoAX3roKDLxs6ILC_bKvwOWPUI8erGE8

# Imports
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

"""# 1.   Limpeza e Análise de Dados de Vendas

# Gerar um dataset de vendas com 50 registros simulados
"""

# Gerar um dataset de vendas com 50 registros simulados
np.random.seed(42)  # Para resultados reprodutíveis

# Função para gerar datas dentro de um ano específico
def generate_dates(start_date, end_date, num_dates):
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    delta = end - start
    return [start + timedelta(days=np.random.randint(0, delta.days)) for _ in range(num_dates)]

# Simulação de dados
data = {
    'ID': range(1, 51),
    'Data': generate_dates('01/01/2023', '31/12/2023', 50),
    'Produto': np.random.choice(['Produto A', 'Produto B', 'Produto C', 'Produto D'], size=50),
    'Categoria': np.random.choice(['Categoria 1', 'Categoria 2', 'Categoria 3'], size=50),
    'Quantidade': np.random.randint(1, 20, size=50),
    'Preço': np.random.uniform(10, 100, size=50).round(2)
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Introduzir alguns valores nulos e duplicados para simulação
df.loc[5, 'Quantidade'] = np.nan  # Valor faltante
df.loc[10, 'Preço'] = np.nan  # Valor faltante
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)  # Duplicar a primeira linha

# Exibir o dataset original com valores faltantes e duplicados
print("Dataset original com valores faltantes e duplicados:")
print(df.head(), "\n")

"""# Limpeza de dados

"""

# Tratamento de valores faltantes: preencher com a média da coluna onde aplicável
df['Quantidade'] = df['Quantidade'].fillna(df['Quantidade'].mean())
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())

# 2. Remover duplicatas
df.drop_duplicates(inplace=True)

# 3. Conversão de tipos de dados, se necessário
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Exibir o dataset limpo
print("Dataset limpo:")
print(df.head(), "\n")

df.isnull().sum() # Verificando qtd de items nulos nas tabelas (averiguandoq que a limpeza ocorreu bem)

# Salvar o dataset limpo em um arquivo CSV
df.to_csv('data_clean.csv', index=False)

"""# Análises"""

# Calcular o total de vendas (Quantidade * Preço) por produto
df['Total_Vendas'] = df['Quantidade'] * df['Preço']
total_vendas_por_produto = df.groupby('Produto')['Total_Vendas'].sum()

# Identificar o produto com o maior número de vendas totais
produto_maior_venda = total_vendas_por_produto.idxmax()
maior_venda = total_vendas_por_produto.max()

# Exibir resultados das análises
print("Total de vendas por produto:")
print(total_vendas_por_produto, "\n")

print(f"Produto com o maior número de vendas totais: {produto_maior_venda} com vendas totais de R${maior_venda:.2f}")

"""# 2. Análise Exploratória de Dados de Vendas"""

# Gerar dataset de vendas para reconstruir o ambiente
np.random.seed(42)

def generate_dates(start_date, end_date, num_dates):
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    delta = end - start
    return [start + timedelta(days=np.random.randint(0, delta.days)) for _ in range(num_dates)]

data = {
    'ID': range(1, 51),
    'Data': generate_dates('01/01/2023', '31/12/2023', 50),
    'Produto': np.random.choice(['Produto A', 'Produto B', 'Produto C', 'Produto D'], size=50),
    'Categoria': np.random.choice(['Categoria 1', 'Categoria 2', 'Categoria 3'], size=50),
    'Quantidade': np.random.randint(1, 20, size=50),
    'Preço': np.random.uniform(10, 100, size=50).round(2)
}

df = pd.DataFrame(data)
df.loc[5, 'Quantidade'] = np.nan
df.loc[10, 'Preço'] = np.nan
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
df['Quantidade'] = df['Quantidade'].fillna(df['Quantidade'].mean())
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())
df.drop_duplicates(inplace=True)
df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
df['Total_Vendas'] = df['Quantidade'] * df['Preço']

# Configurar o estilo do Seaborn
sns.set_theme(style="whitegrid")

# Adicionar colunas de ano e mês para análise mensal
df['Ano_Mes'] = df['Data'].dt.to_period('M')

# Tendência de vendas ao longo do tempo (mensal)
tendencia_vendas = df.groupby('Ano_Mes')['Total_Vendas'].sum()

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))
tendencia_vendas.plot(kind='line', marker='o', color='blue')
plt.title('Tendência de Vendas Mensais (2023)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Total de Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('tendencia_vendas.png')  # Salvar o gráfico
plt.show()

# Identificar padrões ou insights
# 1. Mês com maior volume de vendas
mes_maior_venda = tendencia_vendas.idxmax()
valor_maior_venda = tendencia_vendas.max()

# 2. Mês com menor volume de vendas
mes_menor_venda = tendencia_vendas.idxmin()
valor_menor_venda = tendencia_vendas.min()

# Exibir os insights
print()
print(f"O mês com o MAIOR volume de vendas foi {mes_maior_venda}, com um total de R${valor_maior_venda:.2f}.")
print()
print(f"O mês com o MENOR volume de vendas foi {mes_menor_venda}, com um total de R${valor_menor_venda:.2f}.")

"""# Outros insights interessantes que  eu considero ter"""

# Gráfico de pizza dos produtos mais vendidos
vendas_por_produto = df.groupby('Produto')['Quantidade'].sum()

# Criar gráfico de pizza
plt.figure(figsize=(8, 8))
vendas_por_produto.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Distribuição dos Produtos Mais Vendidos (em Quantidade)', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()

grouped_data = df.groupby(['Ano_Mes', 'Produto'])['Quantidade'].sum().unstack(fill_value=0)

grouped_data_filled = grouped_data

# Criar o gráfico de barras empilhadas
plt.figure(figsize=(14, 7))
grouped_data_filled.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='viridis')

# Ajustes de título e rótulos
plt.title('Quantidade de Produtos por Mês (Barras Empilhadas)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Produto', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
