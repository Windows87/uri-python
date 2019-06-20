digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    try:
        texto = raw_input()
        digitosValue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        digitoMaior = 0
        nDigito = 0

        for digito in texto:
            digitosValue[digitos.index(digito)] += 1
        
        for index in range(10):
            digitoValue = digitosValue[index]
            if nDigito <= digitoValue:
                digitoMaior = index
                nDigito = digitoValue 
        
        print digitoMaior
    except EOFError:
        break