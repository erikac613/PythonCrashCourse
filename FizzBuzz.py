import unittest

def fizz_buzz(integer):
    print("Ran test")
    #for int in list:
    if integer%15 == 0:
        return "FIZZBUZZ"
    elif integer%5 == 0:
        return "BUZZ"
    elif integer%3 == 0:
        return "FIZZ"
    else:
        return ""

#fizz_buzz(list(range(100)))

class MyTest(unittest.TestCase):

    def test_div_15(self):
        self.assertEqual("FIZZBUZZ", fizz_buzz(30))

    def test_div_5(self):
        self.assertEqual("BUZZ", fizz_buzz(10))

    def test_div_3(self):
        self.assertEqual("FIZZ", fizz_buzz(9))

    def test_div_neither(self):
        self.assertEqual("", fizz_buzz(7))

unittest.main()
