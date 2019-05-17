while True:
    try:
        x = input()
        y = (raw_input()).split(' ')
        m = 0

        for e in y:
            if int(e) > m:
                m = int(e)

        if m >= 20:
            print 3
        elif m >= 10 and m < 20:
            print 2
        elif m < 10:
            print 1
        
    except EOFError:
        break
