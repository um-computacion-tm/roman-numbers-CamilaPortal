
def roman_to_decimal(roman:str):

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
    
    

if __name__ == '__main__':
    pass