"""
trabalhando com tipificação e variáveis

"""

nome = 'Davi'                #string
sobrenome = "França"         #string
idade = 35                   #integer
altura = 1.75                #float
bermuda = False;             #boolean

#não concatena texto com inteiro. Tem que usar str()
print(nome + ' ' + sobrenome + " tem " + str(idade) + " anos.")
textoMuitasLinhas = '''

    um longo texto é assim
    tem muitas linhas
    para exibir

'''
print(textoMuitasLinhas)

print(idade + 2)

idadeTexto = '2'

print(idadeTexto + idadeTexto)

print(idade + altura)