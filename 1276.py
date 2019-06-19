alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    try:
        texto = raw_input().replace(' ', '')
        letras = []

        for letra in texto:
            try:
                letras.index(letra)
            except ValueError:
                letras.insert(len(letras), letra)
        
        faixas = []
        letras = sorted(letras)
        primeiraLetra = ''
        ultimaLetra = ''
        
        for letra in letras:
            if primeiraLetra == '':
                primeiraLetra = letra
                ultimaLetra = letra
            else:
                if alfabeto.index(letra) == alfabeto.index(ultimaLetra) + 1:
                    ultimaLetra = letra
                else:
                    faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
                    primeiraLetra = letra
                    ultimaLetra = letra
        
        if primeiraLetra and ultimaLetra:
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
        elif primeiraLetra and ultimaLetra == '':
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
        
        textoFinal = ''

        for faixa in faixas:
            textoFinal += faixa + ', '
        
        print textoFinal[0: len(textoFinal) - 2]
    except EOFError:
        break