import unittest

def decimal_to_roman(decimal):

    roman = {
        1 : "I",
        5 : "V",
        10 : "X"
    }

    if decimal <= 3:
        return roman[1]*decimal
    if decimal == 4:
        return roman[1]+roman[5]
    if decimal == 5:
        return roman[5]
    if decimal >= 6 and decimal <=8:
        return roman[5]+(roman[1]*(decimal-5))
    

class TestDecimalToRoman(unittest.TestCase):
    def test1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")
    
    def test2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, "II")

    def test3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, "III")

    def test4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")

    def test5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")

    def test6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")

    def test7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")

    def test8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, "VIII")


if __name__ == '__main__':
    unittest.main()