import unittest


def isEven(i):
    if i % 2 == 0:
        return True
    return False

class Q1iTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(isEven(0), True)

    def test_2(self):
        self.assertEqual(isEven(5), False)

    def test_3(self):
        self.assertEqual(isEven(88), True)

    def test_4(self):
        self.assertEqual(isEven(-121), False)
    
    def test_5(self):
        self.assertEqual(isEven(-83212), True)


if __name__ == '__main__':
    unittest.main()