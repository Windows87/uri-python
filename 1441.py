while True:
    n = input()

    if not n:
        break
    
    mv = n

    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n * 3 + 1

        if n > mv:
            mv = n
    
    print mv