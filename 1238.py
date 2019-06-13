n = input()

for nIndex in range(n):
    texto = raw_input()
    palavras = texto.split(' ')
    novoTexto = ""

    index = 0
    stopped = False

    while index <= len(palavras[0]) - 1 or index <= len(palavras[1]) - 1:
        if index <= len(palavras[0]) - 1:
          novoTexto += palavras[0][index]
        if index <= len(palavras[1]) - 1:
            novoTexto += palavras[1][index]
        
        index += 1
    
    print novoTexto