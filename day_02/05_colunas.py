# %%
# Manipulando colunas: renomeando, selecionando e reorganizando

import pandas as pd

# Carregando dados de transações
df = pd.read_csv('../data/transacoes.csv', sep=';')
df

# %%
# Verificando os tipos de dados das colunas
df.dtypes

# %%
# Renomeando colunas usando um dicionário
# Definindo mapeamento antigo -> novo nome
renamed_columns = {"DtCriacao": "DaCriacao", "QtdePontos": "QtPontos"}

# Duas formas de renomear:
# df2 = df.rename(columns={"DtCriacao": "DaCriacao",
#                         "QtdePontos": "QtPontos"})  # Cria novo DataFrame

# inplace=True modifica o DataFrame original sem criar cópia
df.rename(columns=renamed_columns, inplace=True)

# %%
# Verificando se as colunas foram renomeadas
df.dtypes

# %%
# Selecionando colunas específicas usando lista
colunas = ["IdCliente", "IdTransacao"]
df[colunas]

# %%
# Reorganizando colunas em ordem alfabética
# Primeiro obtemos lista de todas as colunas
organizar_colunas = list(df.columns)
# Ordenamos alfabeticamente
organizar_colunas.sort()
organizar_colunas

# %%
# Aplicando a nova ordem de colunas ao DataFrame
df = df[organizar_colunas]
df