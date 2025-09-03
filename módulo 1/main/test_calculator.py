import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """Configura a instância da calculadora antes de cada teste."""
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)
        self.assertEqual(self.calc.somar(-1, 1), 0)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(10, 5), 50)
        self.assertEqual(self.calc.multiplicar(10, 0), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 5), 2)
        self.assertEqual(self.calc.dividir(9, 3), 3)

    # 3. Validação de entradas inválidas
    def test_dividir_por_zero(self):
        """Verifica se a divisão por zero levanta uma exceção."""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
