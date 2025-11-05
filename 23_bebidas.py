#análise simples com numpy + pandas
#dataset: drinks.csv da fivethirtyeight

import numpy as np
import pandas as pd

#ler o arquivo csv
df = pd.read_csv(r'C:\Users\davi.carneiro\Desktop\Python_EAD\drinks.csv')

print(df.head()) #apenas as primeiras linhas

#selecionar as colunas de bebidas
colunas_bebidas = ['beer_servings', 'spirit_servings', 'wine_servings']

print(df.columns)

#calculando a soma das bebidas por país

#converte pra array
dados_bebidas  = df[colunas_bebidas].values

df['total_bebidas'] = np.sum(dados_bebidas, axis=1) #soma linha a linha

print(df[['country', 'total_bebidas']].head())

#media total global

media_global = np.mean(df['total_bebidas'].values)
print(media_global)

#criar coluna marcando quem está acima ou abaixo da média

df['acima_media'] = np.where(df['total_bebidas'] > media_global, 'Sim', 'Nao')
print(df[['country', 'total_bebidas', 'acima_media']].head())

#contar países acima e abaixo da média

qtd_acima = (df['acima_media'] == 'Sim').sum()
qtd_abaixo = (df['acima_media'] == 'Nao').sum()

print('Quantidade de países acima da média: ', qtd_acima)
print('Quantidade de países abaixo da média: ', qtd_abaixo)

#mostrar apenas países acima da média
paises_acima = df[df['acima_media'] == 'Sim']
print('Países acima da média de consumo: ')
print(paises_acima[['country', 'total_bebidas']].sort_values(by='total_bebidas', ascending=False).head())

#países que mais bebem cerveja

top_cervejas = df.sort_values(by='beer_servings', ascending=False)
print(top_cervejas[['country', 'beer_servings']].head(10))

#salvar o resultado em csv

df.to_csv(r'C:\Users\davi.carneiro\Desktop\Python_EAD\resultado_analise_drinks.csv', index=False)
print('Arquivo resultado_analise_drinks.csv salvo com sucesso!')