n = input()

for nIndex in range(n):
    texto = raw_input()

    if len(texto) == 5:
        print "3"
    else:
        oneOk = 0
        already = []

        for letra in texto:
            try:
                ['o', 'n', 'e'].index(letra)
                try:
                    already.index(letra)
                except ValueError:
                    oneOk += 1
                    already.insert(len(already), letra)
            except ValueError:
                continue
        
        if oneOk == 2:
            print "1"
        else:
            print "2"