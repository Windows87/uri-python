alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = input()

for nIndex in range(n):
    nLinhas = input()
    soma = 0

    for nLinhasIndex in range(nLinhas):
        texto = raw_input()
        caractereIndex = 0

        for caractere in texto:
            soma += alfabeto.index(caractere) + nLinhasIndex + caractereIndex
            caractereIndex += 1
    
    print soma