while True:
    n = input()
    palavras = []
    maior = 0

    if n == 0:
        break
    
    for nIndex in range(n):
        palavra = raw_input()
        palavras.insert(len(palavras), palavra)
        if len(palavra) > maior:
            maior = len(palavra)

    for palavra in palavras:
        espacos = maior - len(palavra)
        novaPalavra = ""
        
        for i in range(espacos):
            novaPalavra += " "
        
        novaPalavra += palavra

        print novaPalavra
    
    print ""