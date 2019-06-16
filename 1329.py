while True:
    n = input()
    m = 0
    j = 0

    if not n:
        break

    t = raw_input().split(' ')
    for c in t:
        if c == '0':
            m += 1
        else:
            j += 1
    
    print 'Mary won ' + str(m) + ' times and John won ' + str(j) + ' times'