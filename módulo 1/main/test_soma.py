import unittest
from minha_matematica import somar

class TestSomar(unittest.TestCase):

    def test_soma_positivos(self):
        """Testa se a soma de números positivos está correta."""
        resultado = somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_negativos(self):
        """Testa a soma com números negativos."""
        resultado = somar(-10, -5)
        self.assertEqual(resultado, -15)

    def test_soma_com_zero(self):
        """Testa a soma com um dos números sendo zero."""
        resultado = somar(7, 0)
        self.assertEqual(resultado, 7)

if __name__ == '__main__':
    unittest.main()
