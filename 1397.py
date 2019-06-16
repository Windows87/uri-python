while True:
    n = input()
    if not n:
        break

    wA = 0
    wB = 0

    for nIndex in range(n):
        x, y = raw_input().split(' ')
        
        if int(x) > int(y):
            wA += 1

        if int(y) > int(x):
            wB += 1
    
    print str(wA) + ' ' + str(wB)