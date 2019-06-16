def printLine(s, i):
    for nIndex in range(s + i):
        l = ""

        for xIndex in range(s):
            l += " "
            
        for xIndex in range(i):
            l += "*"
            
    print l

while True:
    try:
        n = input()
        s = n/2
        i = 1

        while s >= 0:
            printLine(s, i)
            i += 2
            s -= 1
        
        printLine(n/2, 1)
        printLine(n/2 - 1, 3)
        
        print ""
    except EOFError:
        break