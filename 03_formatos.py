''' detalhando strings e usando formato '''

nomeCompleto = "Davipde França Carneiro"
inicio = 5
fim = inicio + 6
print(nomeCompleto)

print(nomeCompleto[inicio:fim])

nome = input("Qual o seu nome?: ")
sobrenome = input("Qual o seu sobrenome?: ")
print(nome + " " + sobrenome)

valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o segundo valor: ")
print("A soma é: " + str(int(valor1) + int(valor2)))