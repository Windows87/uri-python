while True:
    try:
        x = raw_input()
        c = True
        r = ""
        
        for e in x:
            if c == True:
                e = e.upper()
            else:
                e = e.lower()
            
            r += e
            if e != ' ':
                c = not c
        print r
    except EOFError:
        break
