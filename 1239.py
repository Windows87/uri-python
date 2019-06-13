while True:
    try:
        texto = raw_input()
        openedItalico = False
        openedBold = False
        novoTexto = ""

        for letra in texto:
            if letra == '_':
                if openedItalico:
                    letra = '</i>'
                    openedItalico = False
                else:
                    letra = '<i>'
                    openedItalico = True

            if letra == '*':
                if openedBold:
                    letra = '</b>'
                    openedBold = False
                else:
                    letra = '<b>'
                    openedBold = True
            
            novoTexto += letra

        print novoTexto
    except EOFError:
        break