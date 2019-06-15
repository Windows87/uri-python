while True:
    texto = raw_input()
    
    if texto == '*':
        break

    comps = texto.split('/')
    comps = comps[1:len(comps) - 1]

    ok = 0

    for comp in comps:
        t = 0.0

        for caracter in comp:
            if caracter == 'W':
                t += 1
            elif caracter == 'H':
                t += 1/2.0
            elif caracter == 'Q':
                t += 1/4.0
            elif caracter == 'E':
                t += 1/8.0
            elif caracter == 'S':
                t += 1/16.0
            elif caracter == 'T':
                t += 1/32.0
            else:
                t += 1/64.0

        if t == 1:
            ok += 1
    
    print ok