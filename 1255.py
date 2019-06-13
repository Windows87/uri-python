letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = input()

for nIndex in range(n):
    letrasValores = []
    valores = []
    texto = raw_input().lower()
    maior = 1

    for caractere in texto:
        try:
            index = letras.index(caractere)
            try:
                letrasValoresIndex = letrasValores.index(caractere)
                valores[letrasValoresIndex] += 1          
                if valores[letrasValoresIndex] > maior:
                    maior = valores[letrasValoresIndex]
            except ValueError:
                letrasValores.insert(len(letrasValores), caractere)
                valores.insert(len(valores), 1)
        except ValueError:
            continue
    
    maioresLetras = []

    for mIndex in range(len(valores)):
        if valores[mIndex] == maior:
            maioresLetras.insert(len(maioresLetras), letrasValores[mIndex])

    maioresLetras = sorted(maioresLetras)
    texto = ""

    for maiorLetra in maioresLetras:
        texto += maiorLetra

    print texto