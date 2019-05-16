while True:
    y = input()

    if y == 0:
        break
    
    s = 0
    n = 0
    i = 0

    while n != 5:
        if (y + i) % 2 == 0:
            n += 1
            s += y + i
        i += 1
    

    print s
