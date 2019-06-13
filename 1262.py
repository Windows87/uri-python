while True:
    try:
        acoes = raw_input()
        maxLeituras = input()
        leitura = 0
        soma = 0

        for acao in acoes:
            if acao == "W":
                soma += 1
                leitura = 0
            else:
                if leitura == 0:
                    soma += 1

                if leitura < maxLeituras:
                    leitura += 1
                else:
                    leitura = 1
                    soma += 1
        
        print soma
    except EOFError:
        break