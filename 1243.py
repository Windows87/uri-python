letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.']

while True:
    try:
        texto = raw_input()
        palavras = texto.split(' ')
        nPalavras = 0
        nTamanhoPalavras = 0

        for palavra in palavras:
            ePalavra = True
            nPontos = 0

            for caracter in palavra:
                try:
                    letras.index(caracter)
                    if caracter == '.':
                        if nPontos >= 1:
                            ePalavra = False
                            break
                        else:
                            nPontos += 1
                except:
                    ePalavra = False
                    break
            
            if ePalavra:
                nPalavras += 1
                nTamanhoPalavras += len(palavra.replace('.', ''))
        
        medioTamanhoPalavras = 0

        if nPalavras != 0:
            medioTamanhoPalavras = int(nTamanhoPalavras / nPalavras)

        if medioTamanhoPalavras <= 3:
            print "250"
        elif medioTamanhoPalavras == 4 or medioTamanhoPalavras == 5:
            print "500"
        else:
            print "1000"
    except EOFError:
        break