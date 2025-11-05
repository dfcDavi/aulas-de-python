import numpy as np

#criando array numpy
arr = np.array([1,2,3,4,5])
print(arr)

#operações matemáticas em arrays
print(arr * 2) #multiplicando por 2

#operações entre arrays
arr2 = np.array([10,20,30,40,50])

#somando o arr com arr2
print(arr + arr2)

#criando uma matrix 2D 2x3
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)

#soma e media da matriz
print(np.sum(matriz))
print(np.mean(matriz))

#transposta da matriz
print(matriz.T)

#gerando números aleatórios entre 0 e 1
print(np.random.rand(3,3)) #gera uma matriz 3x3 com valores aleatórios


