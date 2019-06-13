letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    try:
        texto = raw_input()
        novoTexto = ""

        for letra in texto:
            novaLetra = letra.lower()
            try:
                letraIndex = letras.index(novaLetra)
                if letraIndex + 1 <= 13:
                    if letra.islower():
                        novoTexto += letras[letraIndex + 13]
                    else:
                        novoTexto += letras[letraIndex + 13].upper()
                else:
                    if letra.islower():
                        novoTexto += letras[letraIndex - 13]
                    else:
                        novoTexto += letras[letraIndex - 13].upper()
            except ValueError:
                novoTexto += letra
        
        print novoTexto
    except EOFError:
        break