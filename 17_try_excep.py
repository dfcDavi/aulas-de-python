def divisao(a, b):
    
    try:
        resultado = a/b
        print(f"o resultado de {a} por {b} é: {resultado}")
    
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero")
    except TypeError:
        print("Ambos os valores devem ser números")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    #o else é se o try ocorrer com sucesso
    else:
        print("Divisão realizada com sucesso!")
    #o finally sempre ocorre, com ou sem erro no try
    finally: 
        print("O processo de divisão foi concluído")
#normal
divisao(10,2)

#por zero
divisao(10,0)

#tipos invalidos
divisao(10, "dois")

#erro inesperado
divisao("dez", "dois")


