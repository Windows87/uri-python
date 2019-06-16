alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = input()

for nIndex in range(n):
    utilizado = []
    texto = raw_input()

    for caracter in texto:
        try:
            alfabeto.index(caracter)
            try:
                utilizado.index(caracter)
            except ValueError:
                utilizado.insert(len(utilizado), caracter)
        except ValueError:
            continue

    if len(utilizado) == len(alfabeto):
        print 'frase completa'
    elif len(utilizado) >= len(alfabeto)/2:
        print 'frase quase completa'
    else:
        print 'frase mal elaborada'