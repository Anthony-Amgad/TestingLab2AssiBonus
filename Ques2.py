import unittest


class Clock:
    state = "NORMAL"
    state1 = "TIME"
    m = 0
    h = 0
    D = 1
    M = 1
    Y = 2000

    def inp(self, c):

        if self.state == "NORMAL" :
            if c == 'c':
                self.state = "UPDATE"
                self.state1 = "min"
            if c == 'b':
                self.state = "ALARM"
                self.state1 = "Alarm"
            if c == 'a':
                if self.state1 == "TIME":
                    self.state1 = "DATE"
                else:
                    self.state1 = "TIME"
        if self.state == "UPDATE":
            if c == 'd':
                self.state = "NORMAL"
                self.state1 = "TIME"
            if c == 'a':
                if self.state1 == "year":
                    self.state = "NORMAL"
                    self.state1 = "TIME"
                if self.state1 == "month":
                    self.state1 = "year"
                if self.state1 == "day":
                    self.state1 = "month"
                if self.state1 == "hour":
                    self.state1 = "day"
                if self.state1 == "min":
                    self.state1 = "hour"
            if c == 'b':
                if self.state1 == "min":
                    self.m += 1
                    if self.m >= 60:
                        self.m = 0
                if self.state1 == "hour":
                    self.h += 1
                    if self.h >= 24:
                        self.h = 0
                if self.state1 == "day":
                    self.D += 1
                    if self.D > 31:
                        self.D = 1
                if self.state1 == "month":
                    self.M += 1
                    if self.M > 12:
                        self.M = 1
                if self.state1 == "year":
                    self.Y += 1
                    if self.Y > 2100:
                        self.Y = 2000
        if self.state == "ALARM":
            if c == 'd':
                self.state = "NORMAL"
                self.state1 = "TIME"
            if c == 'a':
                self.state1 = "Chime"
        return [self.state, self.state1, str(self.Y)+"-"+str(self.M)+"-"+str(self.D), str(self.h)+":"+str(self.m)]


class Q2ECTest(unittest.TestCase):

    def test_1(self):
        obj = Clock()
        res = obj.inp('a')
        self.assertEqual(res[0],"NORMAL")
        self.assertEqual(res[1],"DATE")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:0")

    def test_2(self):
        obj = Clock()
        obj.inp('a')
        res = obj.inp('a')
        self.assertEqual(res[0],"NORMAL")
        self.assertEqual(res[1],"TIME")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:0")

    def test_3(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        res = obj.inp('c')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:0")

    def test_4(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:1")

    def test_5(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"hour")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:1")

    def test_6(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"hour")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"1:1")

    def test_7(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"day")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"1:1")

    def test_8(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"day")
        self.assertEqual(res[2],"2000-1-2")
        self.assertEqual(res[3],"1:1")

    def test_9(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"month")
        self.assertEqual(res[2],"2000-1-2")
        self.assertEqual(res[3],"1:1")

    def test_10(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"month")
        self.assertEqual(res[2],"2000-2-2")
        self.assertEqual(res[3],"1:1")

    def test_11(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"year")
        self.assertEqual(res[2],"2000-2-2")
        self.assertEqual(res[3],"1:1")

    def test_12(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"year")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_13(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"NORMAL")
        self.assertEqual(res[1],"TIME")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_14(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('c')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_15(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('c')
        res = obj.inp('d')
        self.assertEqual(res[0],"NORMAL")
        self.assertEqual(res[1],"TIME")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_16(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('c')
        obj.inp('d')
        res = obj.inp('b')
        self.assertEqual(res[0],"ALARM")
        self.assertEqual(res[1],"Alarm")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_17(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('c')
        obj.inp('d')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"ALARM")
        self.assertEqual(res[1],"Chime")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")

    def test_18(self):
        obj = Clock()
        obj.inp('a')
        obj.inp('a')
        obj.inp('c')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('a')
        obj.inp('c')
        obj.inp('d')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('d')
        self.assertEqual(res[0],"NORMAL")
        self.assertEqual(res[1],"TIME")
        self.assertEqual(res[2],"2001-2-2")
        self.assertEqual(res[3],"1:1")


class Q2ADUPTest(unittest.TestCase):

    def test_1(self):
        obj = Clock()
        res = obj.inp('c')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:0")

    def test_2(self):
        obj = Clock()
        obj.inp('c')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:1")

    def test_3(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"min")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:2")

    def test_4(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"hour")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"0:2")

    def test_5(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"hour")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"1:2")

    def test_6(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"hour")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"2:2")

    def test_7(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"day")
        self.assertEqual(res[2],"2000-1-1")
        self.assertEqual(res[3],"2:2")

    def test_8(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"day")
        self.assertEqual(res[2],"2000-1-2")
        self.assertEqual(res[3],"2:2")

    def test_9(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"day")
        self.assertEqual(res[2],"2000-1-3")
        self.assertEqual(res[3],"2:2")

    def test_10(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"month")
        self.assertEqual(res[2],"2000-1-3")
        self.assertEqual(res[3],"2:2")

    def test_11(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"month")
        self.assertEqual(res[2],"2000-2-3")
        self.assertEqual(res[3],"2:2")

    def test_12(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"month")
        self.assertEqual(res[2],"2000-3-3")
        self.assertEqual(res[3],"2:2")

    def test_13(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        res = obj.inp('a')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"year")
        self.assertEqual(res[2],"2000-3-3")
        self.assertEqual(res[3],"2:2")

    def test_14(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"year")
        self.assertEqual(res[2],"2001-3-3")
        self.assertEqual(res[3],"2:2")

    def test_15(self):
        obj = Clock()
        obj.inp('c')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        obj.inp('b')
        obj.inp('a')
        obj.inp('b')
        res = obj.inp('b')
        self.assertEqual(res[0],"UPDATE")
        self.assertEqual(res[1],"year")
        self.assertEqual(res[2],"2002-3-3")
        self.assertEqual(res[3],"2:2")


   

if __name__ == '__main__':
    unittest.main()