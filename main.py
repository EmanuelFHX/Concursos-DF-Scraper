import pandas as pd
from scraper import buscar_concursos
from salario import extrair_salario
from utils import limpar_salario

# 1. Buscar concursos
dados = buscar_concursos()

df = pd.DataFrame(dados).drop_duplicates()

# 2. Extrair salários
salarios = []

for link in df["link"]:
    salario = extrair_salario(link)
    salarios.append(salario)

df["salario"] = salarios

# 3. Ordenar
df["salario_num"] = df["salario"].apply(limpar_salario)
df = df.sort_values(by="salario_num", ascending=False)

# 4. Salvar
df.to_excel("data/concursos_df.xlsx", index=False)

print(df.head(10))