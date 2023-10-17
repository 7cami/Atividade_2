import pandas as pd
import matplotlib.pyplot as plt

#Análise de dados sobre focos de incêndio no cerrado ocorridos entre 1998 e 2023

df_arquivo= pd.read_csv("arquivo.csv", index_col=0)
#print (df_arquivo)

#Somente os anos com todos os meses monitorados
df_arquivo = df_arquivo.dropna()


#Qual o total de focos de incêndio a cada ano?
df_arquivo['Total anual'] = df_arquivo.sum(axis=1)

#Qual os meses com maior e menor ocorrência de focos de incêndio em cada ano?
df_arquivo['Mês intenso'] = df_arquivo.iloc[:, :-2].idxmax(axis=1)
df_arquivo['Mês ameno'] = df_arquivo.iloc[:, :-2].idxmin(axis=1)

#Substituindo um cabeçalho subjetivo por objetivo
df_arquivo=df_arquivo.rename(columns={'Mês ameno': 'Menor ocorrência', 'Mês intenso': 'Maior ocorrência'})

#Qual o total de focos de incêndio de cada mês ao longo dos anos?
df_arquivo = df_arquivo.T
df_arquivo['Total por mês'] = df_arquivo.iloc[:-3, :].sum(axis=1)
df_arquivo = df_arquivo.T
print(df_arquivo)

#Quais os anos e o mês destes que setembro não registrou a maior ocorrência de focos?
anos_distoantes = df_arquivo.iloc[:-1,-2]
filter= anos_distoantes != "Setembro"
anos_distoantes=anos_distoantes[filter]
anos_distoantes=anos_distoantes.to_string()
print(anos_distoantes)

df_arquivo.to_csv("arquivo_final.csv")

df_arquivo.plot( y='Total anual', ylabel='Focos de incêndio', xlabel='Ano', title =' Focos de incêndio no cerrado de 1999 a 2022')
plt.show()