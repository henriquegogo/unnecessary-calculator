import sys, unittest
sys.dont_write_bytecode = True
from calculator import sum, sub, mult, div

class TestCalcula(unittest.TestCase):

    def test_sum(self):
        calculation = sum(1, 2)
        expected = 3
        self.assertEqual(calculation, expected)

        calculation = sum(-1, 1)
        expected = 0
        self.assertEqual(calculation, expected)

        calculation = sum(-1, -1)
        expected = -2
        self.assertEqual(calculation, expected)

    def test_sub(self):
        calculation = sub(2, 1)
        expected = 1
        self.assertEqual(calculation, expected)

        calculation = sub(-1, 1)
        expected = -2
        self.assertEqual(calculation, expected)

        calculation = sub(-1, -1)
        expected = 0
        self.assertEqual(calculation, expected)

    def test_mult(self):
        calculation = mult(2, 3)
        expected = 6
        self.assertEqual(calculation, expected)

        calculation = mult(-1, 3)
        expected = -3
        self.assertEqual(calculation, expected)

        calculation = mult(-1, -3)
        expected = 3
        self.assertEqual(calculation, expected)

    def test_div(self):
        calculation = div(6, 3)
        expected = 2
        self.assertEqual(calculation, expected)

        calculation = div(-6, 3)
        expected = -2
        self.assertEqual(calculation, expected)

        calculation = div(-6, -3)
        expected = 2
        self.assertEqual(calculation, expected)

        with self.assertRaises(ZeroDivisionError):
            div(6, 0)

if __name__ == '__main__':
    unittest.main()
