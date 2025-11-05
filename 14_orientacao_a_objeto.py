class Carro :

    def __init__ (self, modelo, cor) :
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 #carro começa parado

    def acelerar(self, incremento) :
        '''acelerar o carro'''
        self.velocidade += incremento
        print(f'o carro {self.modelo} acelerou para {self.velocidade} km/h')

    def parar(self) :
        self.velocidade = 0
        print(f'o carro {self.modelo} parou')

    def desacelerar(self, decremento):
        while self.velocidade > 0 and decremento > 0:
           passo = min (10, self.velocidade)
           self.velocidade -= passo
           decremento -= passo
           print(f'o carro {self.modelo} desacelerou para {self.velocidade}')

        if self.velocidade == 0 :           
        #self.velocidade -= decremento
            print(f'O carro {self.modelo} parou')


carro_instrutor = Carro('Suzuki', 'amarelo')
carro_instrutor.acelerar(20)
carro_instrutor.acelerar(30)

carro_vicente = Carro('BYD', 'cinza')
carro_vicente.acelerar(90)

carro_instrutor.desacelerar(20)
#carro_vicente.parar()
#carro_instrutor.parar()

