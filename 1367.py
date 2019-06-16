while True:
    n = input()
    
    if not n:
        break

    cl = 0
    ct = 0
    inc = []
    inct = []

    for nIndex in range(n):
        p, t, c = raw_input().split(' ')
        if c == 'correct':
            cl += 1
            ct += int(t)

            try:
                incIndex = inc.index(p)
                ct += 20 * inct[incIndex]
            except ValueError:
                continue
        else:
            try:
                incIndex = inc.index(p)
                inct[incIndex] += 1
            except ValueError:
                inc.insert(len(inc), p)
                inct.insert(len(inct), 1)
    
    print str(cl) + ' ' + str(ct)