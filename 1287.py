while True:
    try:
        valor = raw_input().replace('l', '1').replace('o', '0').replace('O', '0').replace(',', '').replace(' ', '')
        try:
            valor = int(valor)
            if valor > 2147483647:
                print 'error'
            else:
                print valor
        except ValueError:
            print 'error'
    except EOFError:
        break