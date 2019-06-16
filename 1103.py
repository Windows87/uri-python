while True:
    texto = raw_input()
        
    if texto == '0 0 0 0':
        break
        
    h1, m1, h2, m2 = texto.split(' ')
    ht1 = int(h1)*60 + int(m1)
    ht2 = int(h2)*60 + int(m2)

    if ht2 >= ht1:
        print ht2 - ht1
    else:
        print  -(ht1 - (24*60 + ht2))