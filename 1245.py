while True:
    try:
        n = input()
        ps = []
        q = 0

        for nIndex in range(n):
            p = raw_input()
            w = ''
            if p[len(p) - 1] == 'E':
                w = p.replace('E', 'D')
            else:
                w = p.replace('D', 'E')
            try:
                ps.index(w)
                ps.remove(w)
                q += 1
            except ValueError:
                ps.insert(len(ps), p)
        
        print q
    except EOFError:
        break