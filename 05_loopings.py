'''
trabalhando com loopings
'''

#for

cidades = ['recife', 'sao paulo', 'olinda']

for cidade in cidades :
    print(cidade)

palavra = "caio"
contador = 0
for letra in palavra:
    print(str(contador) + ' - ' + letra)
    contador = contador + 1
print(cidades[2])

#while

botaoExecutar = True
contador = 0

while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False
