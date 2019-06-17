while True:
    t = raw_input().lower()
    if t == '*':
        break

    ok = True
    ps = t.split(' ')
    n = ps[0][0]

    for p in ps:
        if n != p[0]:
            ok = False
            break
    
    if ok:
        print "Y"
    else:
        print "N"