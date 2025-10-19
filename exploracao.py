import pandas as pd

CSV_PATH = "data/vendas.csv"

print("Visualizando as 5 primeiras linhas do dataset:")
df = pd.read_csv(CSV_PATH)
print(df.head())
print("\n" + "="*50 + "\n")

print(f"O dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas.\n")

print("Tipo de dados de cada coluna:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

print("Contagem de valores ausentes por coluna:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")

print("Filtrando vendas com preço unitário maior que 100:")
df_preco_maior_100 = df[df['preco_unitario'] > 100]
print(df_preco_maior_100.head())
print("\n" + "="*50 + "\n")

print("Ordenando o dataset pelo preço em ordem decrescente:")
df_ordenado_por_preco = df.sort_values(by='preco_unitario', ascending=False)
print(df_ordenado_por_preco.head())
print("\n" + "="*50 + "\n")