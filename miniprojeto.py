import pandas as pd
import numpy as np

# 1 - CARREGANDO  A BASE

df = pd.read_csv(r"C:\Users\User\Documents\EstudosPROG\git_aula\gitsenai\Miniprojeto\Varejo.csv", sep=";")

print("Número de registros:", df.shape[0])
print("Número de colunas:", df.shape[1])

print("Colunas:")
print(df.columns.tolist())

print("Tipos de dados:")
print(df.dtypes)

# 2. LIMPEZA DOS DADOS

print("\VALORES NULOS")
print(df.isnull().sum())


print("\nDuplicatas antes da limpeza:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicatas depois da limpeza:", df.duplicated().sum())


print("Tipos antes da conversão:")
print(df.dtypes)


df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)

print("Tipos depois da conversão:")
print(df.dtypes)

print("Datas inválidas:", df["DATA"].isna().sum())

# - ESTATÍSTICAS DESCRITIVAS


print("\n===== NÚMERO DE FILHOS DOS CLIENTES =====")

print(df["CL_FHL"].describe())
print(df["CL_FHL"].mode().tolist())

compras_genero = df.groupby("CL_GENERO").size()

print("COMPRAS POR GÊNERO")
print(compras_genero.sort_values(ascending=False))


compras_categoria = df.groupby("PR_CAT").size()

print("COMPRAS POR CATEGORIA")
print(compras_categoria.sort_values(ascending=False))


genero_categoria = df.groupby(
    ["CL_GENERO", "PR_CAT"]
).size()

print("COMPRAS POR GÊNERO E CATEGORIA")
print(genero_categoria.sort_values(ascending=False))
