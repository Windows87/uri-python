letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n = input()

for nIndex in range(n):
    texto = raw_input()
    novoTexto = ""
    nEsquerda = input()

    for letra in texto:
        novoTexto += letras[letras.index(letra) - nEsquerda]

    print novoTexto
