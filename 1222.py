while True:
    try:
        nPalavras, nLinhasMax, nCaractMax = raw_input().split(' ')
        nLinhasMax = int(nLinhasMax)
        nCaractMax = int(nCaractMax)

        texto = raw_input()
        textoPalavras = texto.split(' ')

        nLinhas = 0
        nCaracteres = 0
        index = 0

        for palavra in textoPalavras:
            palavraTamanho = len(palavra)
            
            if palavraTamanho + nCaracteres > nCaractMax:
                nLinhas += 1
                nCaracteres = palavraTamanho
            else:
                nCaracteres += palavraTamanho

            if index != len(textoPalavras) - 1:
                if nCaracteres + 1 < nCaractMax:
                    nCaracteres += 1
                else:
                    nLinhas += 1
                    nCaracteres = 0
            
            index += 1

        print int(nLinhas/nLinhasMax) + 1
    except EOFError:
        break