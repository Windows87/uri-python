def setNumbers(m):
    s = 0
    for i in range(int(round(len(m)/2)) + 1):
        rn = len(m[0]) - s
        for i2 in range(rn - s):
            m[s][i2 + s] = s + 1
            
        for i2 in range(rn - s):
            m[rn - 1][i2 + s] = s + 1

        for i2 in range(rn - s):
            m[s + i2][s] = s + 1
            
        for i2 in range(rn - s):
            m[s + i2][rn - 1] = s + 1            

        s += 1
        
    return m

def printMatriz(m):
    for e in m:
        t = ""
        for e2 in e:
            if e2 >= 10:
                t += " " + str(e2) + " "
            else:
                t += "  " + str(e2) + " "
        print t[0:len(t) - 1]
    print ""

while True:
    x = input()
    m = []

    if x == 0:
        break

    for i in range(x):
        l = []
        for i2 in range(x):
            l.insert(len(l), 0)
        m.insert(len(m), l)

    m = setNumbers(m)
    printMatriz(m)
