# %%
import pandas as pd

idades = [
    23, 45, 12, 67, 34,
    32, 89, 54, 21, 43,
    38, 29, 41, 50, 60,
]

series_idades = pd.Series(idades)
series_idades

# %%
idades[0]
series_idades[0]
# %%
# Os indices dentro de um series funcionam como chaves em dict, então usando o sort_values, eles irão se organizar,
# Mas os indices vão continuar com o mesmo valor de antes
series_idades = series_idades.sort_values()
series_idades[0]

# %%
# Utilizando o Iloc procuramos por posição e não por "Chave" como em um dict
print(series_idades.iloc[0])
print(series_idades.iloc[-1])

# %%
series_idades.iloc[:3]

# %%

# Podemos definir nossos próprios indices
idades = [
    23, 45, 12, 67, 34,
    32, 89, 54, 21, 43,
    38, 29, 41, 50, 60,
]

indexs = [
    'Maria', 'Carlos', 'João', 'Ana', 'Pedro',
    'Lucas', 'Fernanda', 'Juliana', 'Roberto', 'Patrícia',
    'Mariana', 'Rafael', 'Aline', 'Bruno', 'Camila',
]

series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
# Agora podemos acessar os valores usando os nomes definidos como indices
series_idades['Ana']

# %%
series_idades.loc['Lucas']