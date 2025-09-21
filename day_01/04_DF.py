# %%

import pandas as pd

idades = [
    23, 45, 12, 67, 34,
    32, 89, 54, 21, 43,
    38, 29, 41, 50, 60,
]

nomes = [
    'Maria', 'Carlos', 'João', 'Ana', 'Pedro',
    'Lucas', 'Fernanda', 'Juliana', 'Roberto', 'Patrícia',
    'Mariana', 'Rafael', 'Aline', 'Bruno', 'Camila',
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# DataFrame pode ser tipo um varal, que você vai lá e pendura series nele

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

# %%
# Podemos acessar tanto por "Roupa estendida", quando por index

df['nomes']
df.iloc[0]

# %%

df.iloc[0]['nomes']