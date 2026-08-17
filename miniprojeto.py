import pandas as pd
import numpy as np

# 1 - CARREGANDO  A BASE
# Abaixo será carregado a base do csv utilizando o pandas. Foram removidas colunas vazias, já que não tem informações úteis.
# Foi mostrado o número de registros na base.
# Tmaabém foi mostrado o nome, tipo e números de colunas na base.

df = pd.read_csv(r"C:\Users\User\Documents\EstudosPROG\git_aula\gitsenai\Miniprojeto\Varejo.csv", sep=";")

print("Número de registros:", df.shape[0])
print("Número de colunas:", df.shape[1])

print("Colunas:")
print(df.columns.tolist())

print("Tipos de dados:")
print(df.dtypes)

# 2. LIMPEZA DOS DADOS
# Abaixo será feita a verificação de nulos na base
# Foi verificado a quantidade de duplicados
# Também foi verificado se existem dados vazios ou preenchidos apenas com espaços
# Verificado data inválidas

print("VALORES NULOS")
print(df.isnull().sum())


duplicatas_antes = df.duplicated().sum()
print("\nDuplicatas antes da limpeza:", duplicatas_antes)


df = df.drop_duplicates()

duplicatas_depois = df.duplicated().sum()
print("Duplicatas depois da limpeza:", duplicatas_depois)


print("Tipos antes da conversão:")
print(df.dtypes)


print("\n===== CATEGORIAS VAZIAS =====")

colunas_texto = df.select_dtypes(include="object").columns

for coluna in colunas_texto:
    vazios = (df[coluna].astype(str).str.strip() == "").sum()
    print(f"{coluna}: {vazios} valores vazios")

df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)

print("Tipos depois da conversão:")
print(df.dtypes)

print("Datas inválidas:", df["DATA"].isna().sum())

# 3 - ESTATÍSTICAS DESCRITIVAS
# Abaixo foram geradas (média; mediana; desvio padrão; moda; máximo; mínimo; e contagem, quartis) utilizando o método describe()


print("\n===== NÚMERO DE FILHOS DOS CLIENTES =====")

print(df["CL_FHL"].describe())
print(df["CL_FHL"].mode().tolist())

# 4 - EXPLORAR PADRÕES DE AGRUPAMENTO
# Abaixo foram agrupados os registros pelo gênero dos clientes
# Utilizando o size(), que contabiliza a quantidade de registros.
# Foi ordenado os resultados do maior para o menor
# Também foi agrupado os registros por gategoria e gênero, simultaneamnte e em ordem decrescente

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


print("CONCLUSÕES")
# Abaixo foram idendificados: 
# O gênero com maior quantidade de registros
# A categoria com maior quantidade de registros
# Quantas duplicatas foram removidas durante a limpeza
# A quantidade de valores nulos depois da limpeza
# A quantidade de datas inválidas depois da conversão

genero_maior = compras_genero.idxmax()
quantidade_genero = compras_genero.max()

print(f"1. O gênero com maior quantidade de registros foi "f"{genero_maior}, com {quantidade_genero} registros.")

categoria_maior = compras_categoria.idxmax()
quantidade_categoria = compras_categoria.max()

print(f"2. A categoria com maior quantidade de registros foi " f"{categoria_maior}, com {quantidade_categoria} registros.")

print(f"3. Foram removidos {duplicatas_antes} registros duplicados.")

total_nulos = df.isnull().sum().sum()

print(f"4. Após a limpeza, a base possui {total_nulos} valores nulos.")

datas_invalidas = df["DATA"].isna().sum()

print(f"5. Após a conversão da coluna DATA, foram encontradas " f"{datas_invalidas} datas inválidas.")

