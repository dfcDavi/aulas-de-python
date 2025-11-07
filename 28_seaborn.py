import seaborn as sbn
import pandas as pd
import matplotlib.pyplot as plt

data = {

    'idade': [22,25,30],
    'salario': [2200,2500, 3000]
}

df = pd.DataFrame(data)

sbn.scatterplot(data=df, x='idade', y='salario')

plt.title('Relação entre idade e salário')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

