import pandas as pd

#criando dataframe
data = {

    'nome' : ['Caio', 'Davi'],
    'idade' : [25, 30],
    'salario' : [5000, 6000]

}

df = pd.DataFrame(data)

print(df)
print(df['nome'])

print (df[df['idade'] > 25])

#acrescenta coluna imposto
df['imposto'] = df['salario'] * 0.1

print(df)

media_salarial = df['salario'].mean()

print(media_salarial)

print(df['salario'].min())
print(df['salario'].max())
print(df['salario'].sum())

print(df.describe())

#ordenar por salario
print(df.sort_values(by='salario', ascending=False)) #False é decrescente / True é crescente

df['setor'] = ['TI', 'RH']

print(df.groupby('setor')['salario'].mean())

print(df['setor'].value_counts())

bonus_data = {

    'nome' : ['Caio', 'Davi'],
    'bonus' : [500, 1600]
}

df_bonus = pd.DataFrame(bonus_data)
#fazendo merge
df_merged = pd.merge(df, df_bonus, on='nome') #on usa como referência o nome para identificar elementos iguais
print(df_merged)

#calculo do salario final
df_merged['salario_final'] = df_merged['salario'] - df_merged['imposto'] + df_merged['bonus']
print(df_merged)


#salvar em csv
df.to_csv(r'C:\Users\davi.carneiro\Desktop\Python_EAD\salarios.csv', index=False) #index=False retira o índice da tabela

