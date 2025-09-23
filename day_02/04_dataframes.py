# %%
# Explorando e analisando DataFrames - métodos básicos de investigação

import pandas as pd

# Carregando dados de clientes
df_clientes = pd.read_csv('../data/clientes.csv', sep=';')
df_clientes

# %%
# head(): mostra as primeiras 5 linhas (ou número especificado)
df_clientes.head(5)

# %%
# tail(): mostra as últimas 5 linhas (ou número especificado)
df_clientes.tail(5)

# %%
# sample(): mostra 5 linhas aleatórias do DataFrame
df_clientes.sample(5)

# %%
# shape: retorna tupla com (número de linhas, número de colunas)
df_clientes.shape

# %%
# columns: lista com os nomes de todas as colunas
df_clientes.columns

# %%
# index: mostra informações sobre o índice do DataFrame
df_clientes.index

# %%
# info(): resumo completo do DataFrame incluindo uso de memória
# memory_usage='deep' calcula o uso real de memória
df_clientes.info(memory_usage='deep')

# %%
# dtypes: mostra o tipo de dados de cada coluna
df_clientes.dtypes