import matplotlib.pyplot as plt
import numpy as np


#exemplo de gráfico de linha

#dados para o grafico de linha

x = np.linspace(0, 10, 100) #100 pontos entre 0 e 10
y = np.sin(x)

plt.plot(x, y, label='Seno(x)', color='b')

#adicionando titulos e rotulos
plt.title('Gráfico de linha: Seno(x)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#adicionar legenda
plt.legend()

#exibir gráfico
plt.show()


categorias = ['A', 'B', 'C', 'D']
valores = [10,20,15,25]

#criando grafico de barras
plt.bar(categorias, valores, color='green')
plt.title('Gráfico de barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

plt.show()

