n = input()

for nIndex in range(n):
    a = float(input())
    d = 0

    while a > 1:
        d += 1
        a = a / 2.0
    
    print str(d) + ' dias'