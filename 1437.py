while True:
    n = input()
    if not n:
        break
    s = raw_input()
    a = 0

    for e in s:
        if e == 'E':
            a -= 90
        else:
            a += 90
        
        if a == 360 or a == -360:
            a = 0
    
    if a == 0:
        print 'N'
    elif a == 180 or a == -180:
        print 'S'
    elif a > 0:
        print 'L'
    else:
        print 'O'