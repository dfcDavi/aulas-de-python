executar = True

while executar:
    escolhas = '''

    [1] ou [+] para Somar
    [2] ou [-] para Subtrair
    [3] ou [+] para Multiplicar
    [4] ou [+] para Dividir
    [5] ou [+] para Sair
    (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)
    '''
    print(escolhas)
    operador = input("Qual sua opção?: ")
    valor01 = int (input("Escolha o primeiro número: "))
    valor02 = int (input("Escolha o segundo número: "))
    textoFinal = '''
    Deseja realizar outro cálculo?
    [1] Não, desejo sair!
    [2] Sim, desejo realizar outro cálculo
    '''

    if operador == '1' or operador == '+' or operador == 'Somar' :
        resultado = valor01 + valor02
        print('O resultado é: ' + str(resultado))
        print(textoFinal)
        escolhaFinal = input("Qual a sua escolha?")
        if escolhaFinal == '1' :
            executar = False

