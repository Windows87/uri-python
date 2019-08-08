while True:
    try:
        p = raw_input()
        if p == 'esquerda':
            print 'ingles'
        elif p == 'direita':
            print 'frances'
        elif p == 'nenhuma':
            print 'portugues'
        else:
            print 'caiu'
    except EOFError:
        break