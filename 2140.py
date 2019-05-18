while True:
    x, y = (raw_input()).split(' ')

    if x == "0" and y == "0":
        break

    t = int(y) - int(x)
    p = False
    n = [2, 5, 10, 20, 50, 100]

    for e in n:
        for e2 in n:
            if e + e2 == t:
                p = True
                break
        if p == True:
            break

    if p == True:
        print "possible"
    else:
        print "impossible"
