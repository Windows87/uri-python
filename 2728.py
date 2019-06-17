while True:
    try:
        ps = raw_input().lower().split('-')
        w = ['c', 'o', 'b', 'o', 'l']
        ok = True

        for i in range(len(ps)):
            p = ps[i]
            w2 = w[i]
            if p[0] != w2 and p[len(p) - 1] != w2:
                ok = False
                break

        if ok:
            print "GRACE HOPPER"
        else:
            print "BUG"
    except EOFError:
        break