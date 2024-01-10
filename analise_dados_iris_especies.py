import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

print("Dados OLAP:")
print(iris.head())
print("\n")

olap_data = iris.groupby('species').mean()
print("Análise OLAP - Média por Espécie:")
print(olap_data)
print("\n")

olap_counts = iris['species'].value_counts()
print("Análise OLAP - Contagem de Ocorrências por Espécie:")
print(olap_counts)
print("\n")

sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
plt.title('Gráfico de Dispersão das Medidas Sepal por Espécie')
plt.show()
