import unittest

def roman_to_decimal(roman):

    total=0
    prev=0
    valor_actual=0
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    for letra in range(len(roman)-1,-1,-1):
        valor_actual = values[roman[letra]]

        if valor_actual >= prev:
            total += valor_actual

        else:
            total-=valor_actual
            
        
        prev = values[roman[letra]]

    return total


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