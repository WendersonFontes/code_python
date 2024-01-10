import pandas as pd

# Criar um DataFrame com informações sobre projetos de construção com estrutura de aço leve
data = {
    'Projeto': ['Casa A', 'Edifício B', 'Apartamento C', 'Escritório D', 'Loja E'],
    'Área Total (m²)': [150, 800, 120, 300, 80],
    'Custo Total (BRL)': [200000, 1000000, 150000, 400000, 120000],
    'Tempo de Construção (meses)': [6, 18, 8, 12, 5],
    'Número de Andares': [1, 5, 3, 4, 1],
}

df = pd.DataFrame(data)

# Exibir o DataFrame
print("Dados OLAP:")
print(df)
print("\n")

# Realizar análise OLAP (média de custo por andar)
df['Custo por Andar (BRL)'] = df['Custo Total (BRL)'] / df['Número de Andares']
olap_data = df[['Projeto', 'Custo por Andar (BRL)']]
print("Análise OLAP - Média de Custo por Andar:")
print(olap_data)
print("\n")

# Realizar análise OLAP mais avançada (resumo estatístico)
summary_stats = df.describe()
print("Resumo Estatístico:")
print(summary_stats)
