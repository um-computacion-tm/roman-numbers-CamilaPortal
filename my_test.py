import unittest
from Decimal2roman import decimal_to_roman
from Roman2decimal import roman_to_decimal

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
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
    
    def test9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, "IX")
    
    def test24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado, "XXIV")

    def test58(self):
        resultado = decimal_to_roman(58)
        self.assertEqual(resultado, "LVIII")
    
    def test100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")

    def test150(self):
        resultado = decimal_to_roman(150)
        self.assertEqual(resultado, "CL")
    
    def test205(self):
        resultado = decimal_to_roman(205)
        self.assertEqual(resultado, "CCV")
    
    def test468(self):
        resultado = decimal_to_roman(468)
        self.assertEqual(resultado, "CDLXVIII")

    def test500(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, "D")

    def test999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, "CMXCIX")
    
    def test1000(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, "M")
    
    def test1125(self):
        resultado = decimal_to_roman(1125)
        self.assertEqual(resultado, "MCXXV")
    
    def test3999(self):
        resultado = decimal_to_roman(3999)
        self.assertEqual(resultado, "MMMCMXCIX")

################################### TEST ROMANO A DECIMAL ###################################################

class TestRomanToDecimal(unittest.TestCase):
    def test1(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)
    
    def test2(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, 2)
    
    def test3(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, 3)

    def test4(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4) 

    def test5(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado, 5)
    
    def test6(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado, 6)
    
    def test7(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual(resultado, 7)

    def test8(self):
        resultado = roman_to_decimal("VIII")
        self.assertEqual(resultado, 8)
    
    def test9(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)
    
    def test10(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)

    def test12(self):
        resultado = roman_to_decimal("XII")
        self.assertEqual(resultado, 12)
    
    def test15(self):
        resultado = roman_to_decimal("XV")
        self.assertEqual(resultado, 15)
    
    def test45(self):
        resultado = roman_to_decimal("XLV")
        self.assertEqual(resultado, 45)
    
    def test100(self):
        resultado = roman_to_decimal("C")
        self.assertEqual(resultado, 100)
    
    def test299(self):
        resultado = roman_to_decimal("CCXCIX")
        self.assertEqual(resultado, 299)

    def test500(self):
        resultado = roman_to_decimal("D")
        self.assertEqual(resultado, 500)

    def test850(self):
        resultado = roman_to_decimal("DCCCL")
        self.assertEqual(resultado, 850)
    
    def test1000(self):
        resultado = roman_to_decimal("M")
        self.assertEqual(resultado, 1000)
        
if __name__ == '__main__':
    unittest.main()