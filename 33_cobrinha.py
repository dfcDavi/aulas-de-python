import turtle
import random
import time

# === configuração da janela do jogo ===

janela = turtle.Screen()
janela.title('Jogo da Cobrinha - Nokia 3310')
janela.bgcolor('black')
janela.setup(width=600, height=600)
janela.tracer(0) #controle manual da atualização da tela

# === cabeça da cobra ===

cabeca_cobra = turtle.Turtle()
cabeca_cobra.speed(0)
cabeca_cobra.shape('square')
cabeca_cobra.color("violet")
cabeca_cobra.penup() #levanta a caneta
cabeca_cobra.goto(0,0)
cabeca_cobra.direcao = 'stop'

# === comida da cobra ===

comida = turtle.Turtle()
comida.shape('circle')
comida.color('green')
comida.speed(0)
comida.penup()
comida.goto(0, 100) #primeira posição da comida. As demais serão aleatórias

#lista de segmentos (corpo da cobra)
segmentos = []
#variável de pontuação
pontuacao = 0

#funções de movimento

def ir_para_cima():
    if cabeca_cobra.direcao != 'Down':
        cabeca_cobra.direcao = 'Up'

def ir_para_baixo():
    if cabeca_cobra.direcao != 'Up':
        cabeca_cobra.direcao = 'Down'

def ir_para_esquerda():
    if cabeca_cobra.direcao != 'Right':
        cabeca_cobra.direcao = 'Left'

def ir_para_direita():
    if cabeca_cobra.direcao != 'Left':
        cabeca_cobra.direcao = 'Right'

#controles do jogo
janela.listen()
janela.onkeypress(ir_para_cima, "Up") #seta pra cima do teclado
janela.onkeypress(ir_para_baixo, "Down") #seta pra baixo do teclado
janela.onkeypress(ir_para_esquerda, "Left") #seta pra esquerda do teclado
janela.onkeypress(ir_para_direita, "Right") #seta pra direita do teclado

# === função para mover a cabeça da cobra ===

def mover():
    x = cabeca_cobra.xcor()
    y = cabeca_cobra.ycor()

    if cabeca_cobra.direcao == 'Up':
        cabeca_cobra.sety(y+20)

    elif cabeca_cobra == 'Down':
        cabeca_cobra.sety(y-20)

    elif cabeca_cobra == 'Left':
        cabeca_cobra.setx(x-20)

    elif cabeca_cobra == 'Right':
        cabeca_cobra.setx(x+20)

#=== Loop principal ===
while True:
    janela.update()
    #verificar colisão com as bordas

    if cabeca_cobra.xcor() > 290 or cabeca_cobra.xcor() < -290 or cabeca_cobra.ycor() > 290 or cabeca_cobra.ycor() < -290:
        time.sleep(1)
        cabeca_cobra.goto(0,0)
        cabeca_cobra.direcao = 'stop'

        #apagar os segmentos existentes (corpo da cobra)

        #esconde o corpo fora da visão do usuário
        for segmento in segmentos: #para cada segmento atual
            segmento.goto(1000,1000) #move a posição para fora da tela
        segmentos.clear() #limpa lista de segmentos

        pontuacao = 0
        janela.title('Jogo da Cobrinha - Nokia 3310')

    #verificar se come a comida
    if cabeca_cobra.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280, 280)
        comida.goto(x,y)

        #adiciona novo segmento ao corpo
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape('square')
        novo_segmento.color('purple')
        novo_segmento.penup()
        segmentos.append(novo_segmento)

        pontuacao += 10
        janela.title(f"Jogo da Cobrinha - Pontos: {pontuacao}")

    #mover o corpo da cobra
    
    #move cada segmento para a posição do anterior (de trás pra frente)
    for i in range(len(segmentos)-1,0,-1): #índices do último até o segundo (decrementando)
        x = segmentos[i-1].xcor() #pega a coordenada x do segmento anterior
        y = segmentos[i-1].ycor() #pega a coordenada y do segmento anterior
        segmentos[i].goto(x,y) #move o segmento atual para a posição anterior

    #move o primeiro segmento para onde estava a cabeça da cobrinha
    if len(segmentos) > 0: #se existir pelo menos um segmento
        x = cabeca_cobra.xcor() #lê a posição x da cabeça
        y = cabeca_cobra.ycor()
        segmentos[0].goto(x,y)
    
    #move a cabeça da caobra conforme a direção definida
    mover()

    #verificar colisao com o próprio corpo
    for segmento in segmentos:
        if segmento.distance(cabeca_cobra) < 20:
            time.sleep(1)
            cabeca_cobra.goto(0,0)
            cabeca_cobra.direcao = 'stop'

            #esconde o corpo fora da visão do usuário
            for segmento in segmentos: #para cada segmento atual
                segmento.goto(1000,1000) #move a posição para fora da tela
            
            segmentos.clear() #limpa lista de segmentos

            pontuacao = 0
            janela.title('Jogo da Cobrinha - Nokia 3310')
    
    time.sleep(0.1) #pequena pausa na velocidade do jogo, 10 frames por segundo

#mantém a tela aberta
janela.mainloop()