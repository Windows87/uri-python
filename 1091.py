while True:
    n = input()
    
    if not n:
        break
    
    dX, dY = raw_input().split(' ')
    dX = int(dX)
    dY = int(dY)

    for nIndex in range(n):
        x, y = raw_input().split(' ')
        x = int(x)
        y = int(y)

        if x == dX or y == dY:
            print "divisa"
        elif x > dX and y > dY:
            print "NE"
        elif x > dX and y < dY:
            print "SE"
        elif x < dX and y > dY:
            print "NO"
        else:
            print "SO"