# %%
# Extraindo tabelas de páginas web usando pandas

import requests
import pandas as pd

# URL da página da Wikipedia sobre unidades federativas do Brasil
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

# Headers necessários para simular um navegador real (evita bloqueio)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

# Fazendo requisição HTTP para obter o conteúdo da página
r = requests.get(url, headers=headers)

# read_html encontra automaticamente todas as tabelas HTML na página
dfs = pd.read_html(r.text)
dfs

# %%
# Verificando quantas tabelas foram encontradas na página
len(dfs)

# %%
# Selecionando a segunda tabela (índice 1) que contém dados das UFs
df_uf = dfs[1]
# Salvando a tabela extraída como CSV
df_uf.to_csv('uf_brasil.csv')