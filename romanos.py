import unittest

def decimal_to_roman(decimal):

    roman = ""
    unidad = (((decimal % 1000) % 100) % 10)
    decena = (((decimal % 1000) % 100) // 10)
    centena = (decimal % 1000)//100
    u_de_mil= decimal // 1000

    if u_de_mil >=1 and u_de_mil <=3:
        for i in range (u_de_mil):
            roman += "M"
    
############################################
    
    if centena >= 1 and centena <= 3:
        for i in range(centena):
            roman += "C"

    if centena == 4:
        roman += "CD"
    
    if centena == 5:
        roman += "D"
    
    if centena >= 6 and centena <= 8:
        roman += "D"+"C"*(centena-5)

    if centena == 9:
        roman += "CM"
    
###########################################

    if decena >= 1 and decena <= 3:
        for i in range(decena):
            roman += "X"

    if decena == 4:
        roman +="XL"
    
    if decena == 5:
        roman += "L"
    
    if decena >= 6 and decena <= 8:
        roman += "L"+"X"*(decena-5)
    
    if decena == 9:
        roman += "XC"

#############################################

    if unidad >=1 and unidad <= 3:
        for i in range(unidad):
            roman += "I"
            
    if unidad == 4:
        roman +="IV"

    if unidad == 5:
        roman += "V"

    if unidad >= 6 and unidad <=8:
        roman += "V" + "I"*(unidad-5)
    
    if unidad == 9:
        roman += "IX"
    
    return roman
    

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


if __name__ == '__main__':
    unittest.main()