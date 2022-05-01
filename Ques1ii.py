from asyncio.windows_events import NULL
import unittest


def maxVal(arr):
    mm = float('-inf')
    for x in arr:
        if x > mm:
            mm = x

    if mm == float('-inf'):
        return NULL
    
    return mm

def minVal(arr):
    mm = float('inf')
    for x in arr:
        if x < mm:
            mm = x

    if mm == float('inf'):
        return NULL
    
    return mm

class Q1iiMaxTest(unittest.TestCase):

    arr = []

    def test_1(self):
        self.assertEqual(maxVal(self.arr),NULL)

    def test_2(self):
        for x in range(1,1000):
            self.arr.append(x)
        self.assertEqual(maxVal(self.arr), max(self.arr))
        self.arr.clear()

    def test_3(self):
        for x in range(-1000,-1):
            self.arr.append(x)
        self.assertEqual(maxVal(self.arr), max(self.arr))
        self.arr.clear()

    def test_4(self):
        for x in range(-1000,1000):
            self.arr.append(x)
        self.assertEqual(maxVal(self.arr), max(self.arr))
        self.arr.clear()
    
    def test_5(self):
        for x in range(-1000,1000,5):
            self.arr.append(x)
        self.assertEqual(maxVal(self.arr), max(self.arr))
        self.arr.clear()

class Q1iiMinTest(unittest.TestCase):

    arr = []

    def test_1(self):
        self.assertEqual(minVal(self.arr),NULL)

    def test_2(self):
        for x in range(1,1000):
            self.arr.append(x)
        self.assertEqual(minVal(self.arr), min(self.arr))
        self.arr.clear()

    def test_3(self):
        for x in range(-1000,-1):
            self.arr.append(x)
        self.assertEqual(minVal(self.arr), min(self.arr))
        self.arr.clear()

    def test_4(self):
        for x in range(-1000,1000):
            self.arr.append(x)
        self.assertEqual(minVal(self.arr), min(self.arr))
        self.arr.clear()
    
    def test_5(self):
        for x in range(-1000,1000,5):
            self.arr.append(x)
        self.assertEqual(minVal(self.arr), min(self.arr))
        self.arr.clear()


if __name__ == '__main__':
    unittest.main()