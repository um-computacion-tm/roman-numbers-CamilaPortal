
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


if __name__ == '__main__':
    pass