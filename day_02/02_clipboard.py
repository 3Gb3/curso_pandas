# %%
# Carregando dados diretamente da área de transferência (clipboard)
# Útil quando você copia dados de uma planilha Excel ou outro aplicativo

import pandas as pd

# Lê dados da área de transferência com separador ponto-e-vírgula
# Primeiro copie alguns dados com Ctrl+C antes de executar
df = pd.read_clipboard(sep=';')
df