nomeAluno = input("Qual o nome do aluno?: ")
mediaAluno = int(input("Qual a média do aluno " + nomeAluno + " ?: "))
tipoEscola = input("Em que escola o " + nomeAluno + " estuda?: \n[1] Pública\n[2] Particular:\n")
freqAluno = int(input("Qual a frequência do aluno " + nomeAluno + "?: "))

if tipoEscola == "2" :
    print("-----Escola Particular-----")
    if(mediaAluno >= 7 and freqAluno >= 70) :
        print("O aluno " + nomeAluno + " foi Aprovado")
    else :
        print("O aluno " + nomeAluno + " foi Reprovado")

if tipoEscola == "1" :
    print("-----Escola Pública-----")
    if mediaAluno >= 7 or freqAluno >= 70 :
        print("O aluno " + nomeAluno + " foi Aprovado")
    else :
        print("O aluno " + nomeAluno + " foi Reprovado")

print("fim do boletim")