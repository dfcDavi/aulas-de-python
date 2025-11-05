class Calculadora :
    def somar (self, *args):
        return sum(args)
    
calc = Calculadora()

print(calc.somar(1,2,3,4,5))