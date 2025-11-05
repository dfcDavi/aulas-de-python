from random import randint

print("### Iniciando o Jogo ###")

random = randint(0, 100)
chute = 0

nivelDificuldade = int(input("Qual o nível de dificuldade?\n[1] Fácil\n[2] Médio\n[3] Difícil\n"))
print('')

if nivelDificuldade == 1:

    chances = 10

if nivelDificuldade == 2:

    chances = 5

if nivelDificuldade == 3:

    chances = 3

while chute != random :
    chute = input("Chute um número entre 0 e 100: ")

    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('------')
            print("Parabéns! você acertou! O número era {} e você ainda tinha {} chances".format(random,chances))
            print('------')
        else :
            print('')
            if chute > random :
                print("Você errou! Dica: É um número menor")
            else :
                print("Você errou! Dica: É um número maior")
            print("Você ainda possui {} chances".format(chances))
            print("")
        if chances == 0 :
            print("Suas chances acabaram! Você perdeu!")
            print("O valor era: {}".format(random))
            print("")
            break;
print("Fim de jogo!")

