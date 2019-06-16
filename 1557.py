while True:
    n = input()
    if not n:
        break
    
    maxStringLength = len(str((2**(n - 1))**2))
    n2 = 0

    for nIndex in range(n):
        l = ""

        for nIndex2 in range(n):
            nE = 2**(n2 + nIndex2)
            
            stringLength = len(str(nE))

            if nIndex2:
                l += " "

            for strIndex in range(maxStringLength - stringLength):
                l += " "
            
            l += str(nE)
        print l
        n2 += 1
    
    print ""