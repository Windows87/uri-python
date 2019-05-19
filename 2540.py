while True:
    try:
        x = input()
        y = raw_input().split(' ')
        p = 0
        
        for e in y:
            if e == "1":
                p += 1

        if p >= 2/3.0 * x:
            print "impeachment"
        else:
            print "acusacao arquivada"
    except EOFError:
        break
