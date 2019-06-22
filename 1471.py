while True:
    try:
        n, r = raw_input().split(' ')
        m = raw_input().split(' ')
        nr = []
        nm = int(n) - int(r)

        if not nm:
            print '*'
            continue
        
        for nIndex in range(int(n)):
            nIndex += 1

            try:
                m.index(str(nIndex))
            except ValueError:
                nr.insert(len(nr), nIndex)
                nm -= 1
            
            if not nm:
                break
        
        nr = sorted(nr)
        t = ""

        for e in nr:
            t += str(e) + " "
        
        print t
    except EOFError:
        break