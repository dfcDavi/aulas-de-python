import unittest

from operacoes import somar, subtrair, multiplicar, dividir

class TesteOperacoes(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2,3), 5)
        self.assertEqual(somar(-1,1), 0)
        self.assertEqual(somar(-2,-3), -5)

    def test_subtrair(self):
        self.assertEqual(subtrair(2,3), -1)
        self.assertEqual(subtrair(-1,1), -2)
        self.assertEqual(subtrair(-2,-3), 1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2,3), 6)
        self.assertEqual(multiplicar(-1,1), -1)
        self.assertEqual(multiplicar(-2,-3), 6)
    
    def test_dividir(self):
        self.assertEqual(dividir(-6,3), -2)
        self.assertEqual(dividir(-1,1), -1)
        with self.assertRaises(ValueError) as contexto: 
            dividir(1,0)
        self.assertEqual(str(contexto.exception),"divisão por zero!")

if __name__ == '__main__':
    unittest.main()