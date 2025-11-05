'''
trabalhando com funções
'''

def minhaFuncao() :
    print('Hello World!')

minhaFuncao()
minhaFuncao()

cidades = ['recife', 'olinda', 'sao luis', 'mogi das cruzes']
contador = 0

def minhaFuncaoMelhorada(city, count) :
    print(str(count) + " - " + city)

for cidade in cidades :
    contador = contador + 1
    minhaFuncaoMelhorada(cidade, contador)

