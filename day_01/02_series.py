# %%
idades = [18 , 20, 19, 15, 33, 20, 69, 75, 32, 53]
media_idades = sum(idades) / len(idades)
print(f'Media das idades = {media_idades}')
diffs = max(idades) - min(idades)
print(f'Diferencial = {diffs}')

# %%
import pandas as pd

series_idades = pd.Series(idades)  # Converte para o mesmo tipo
series_idades

# %%
media_idades_series = series_idades.mean()
variancia_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades