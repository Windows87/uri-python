while True:
    try:
        antigo = raw_input().lower()
        novo = raw_input()
        texto = raw_input()
        palavras = texto.replace('<', '.<').replace('>', '>.').split('.')
        textoNovo = ""
        textoFinal = ""

        for palavra in palavras:
            novaPalavra = palavra
            if novaPalavra != '':
                if novaPalavra[0] == '<':
                    textoNovo += novaPalavra.lower().replace(antigo, novo)
                else:
                    textoNovo += novaPalavra

        palavras2 = texto.split(' ')
        palavras3 = textoNovo.split(' ')
        
        for nIndex in range(len(palavras3)):
            if palavras2[nIndex].lower() == palavras3[nIndex]:
                textoFinal += palavras2[nIndex] + ' '
            else:
                textoFinal += palavras3[nIndex] + ' '
        
        print textoFinal[0:len(textoFinal) - 1]
    except EOFError:
        break