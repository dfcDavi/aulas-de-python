deseja = True

while deseja :
    anoNascimento = int (input("em que ano você nasceu?: "))
    anoAtual = int(input("Em que ano nós estamos?: "))
    idade = anoAtual - anoNascimento

    print("Sua idade é: " + str(idade))

    resposta = input("Você deseja testar novamente ('S/N')?: ")

    if resposta == 'N' :
        deseja = False


        

