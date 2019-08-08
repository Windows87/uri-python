n = input()

for nIndex in range(n):
    n2 = input()
    ns = raw_input().split(' ')
    ni = []

    for na in ns:
        na = int(na)
        if na % 2 > 0:
            ni.insert(len(ni), na)
    
    t = ''
    l = len(ni)

    ni = sorted(ni, reverse = True)
    n2 = 0
    n3 = 0

    while n3 != l:
        t += str(ni[n2])
        n3 += 1

        if n3 != l:
            t += ' '
            t += str(ni[l - 1 - n2])
            n3 += 1
        
        if n3 != l:
            n2 += 1    
            t += ' '
    
    print t