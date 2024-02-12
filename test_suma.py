import unittest
from main import *


class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(3, 5), -2)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(5, 2), 2.5)
        self.assertEqual(dividir(-6, 3), -2)
        self.assertEqual(dividir(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(0, 5), 0)


if __name__ == '__main__':
    unittest.main()
