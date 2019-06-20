n = input()

for nIndex in range(n):
    b = input()
    
    A1, D1, L1 = raw_input().split(' ')
    A2, D2, L2 = raw_input().split(' ')

    P1 = (int(A1) + int(D1))/2.0
    P2 = (int(A2) + int(D2))/2.0

    if int(L1) % 2 == 0:
        P1 += b
    
    if int(L2) % 2 == 0:
        P2 += b
    
    if P1 == P2:
        print 'Empate'
    elif P1 > P2:
        print 'Dabriel'
    else:
        print 'Guarte'