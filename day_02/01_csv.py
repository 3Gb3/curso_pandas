# %%
# Trabalhando com diferentes formatos de arquivo no Pandas

import pandas as pd

# Carregando arquivo CSV com separador ponto-e-vírgula
df = pd.read_csv("../data/clientes.csv", sep=';')
df

# %%
# Salvando o DataFrame como CSV com vírgula como separador
# index=False evita salvar o índice como uma coluna extra
df.to_csv('clientes.csv', index=False, sep=',')

# %%
# Salvando em formato Parquet (mais eficiente para grandes volumes de dados)
df.to_parquet('clientes.parquet', index=False)

# %%
# Carregando arquivo Parquet
df2 = pd.read_parquet("clientes.parquet")
df2

# %%
# Salvando como arquivo Excel
df2.to_excel("clientes.xlsx", index=False)

# %%
# Carregando arquivo Excel
df3 = pd.read_excel("clientes.xlsx")
df3