import pandas as pd
import numpy as np

# 1 - CARREGANDO  A BASE

df = pd.read_csv(r"C:\Users\User\Documents\EstudosPROG\git_aula\gitsenai\Miniprojeto\Varejo.csv")

print("Número de registros:", df.shape[0])
print("Número de colunas:", df.shape[1])

print("\nColunas:")
print(df.columns.tolist())

print("Tipos de dados:")
print(df.dtypes)

