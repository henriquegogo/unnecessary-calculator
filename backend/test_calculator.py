import sys, unittest
from calculator import sum, sub, mult, div

sys.dont_write_bytecode = True

class TestCalcula(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(-1, 3), -3)
        self.assertEqual(mult(-1, -3), 3)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(-6, -3), 2)
        with self.assertRaises(ZeroDivisionError):
            div(6, 0)

if __name__ == '__main__':
    unittest.main()
