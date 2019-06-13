n = input()

for nIndex in range(n):
    texto = raw_input()
    textoMetade = len(texto)/2

    novoTexto = ""

    for textoIndex in range(len(texto)):
        novoTexto += texto[textoMetade -1 - textoIndex]

    print novoTexto