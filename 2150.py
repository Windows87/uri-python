while True:
    try:
        a = raw_input()
        c = []
        b = raw_input()
        t = 0

        for d in a:
            c.insert(len(c), d)
        
        for d in b:
            try:
                c.index(d)
                t += 1
            except ValueError:
                continue
        
        print t
    except EOFError:
        break