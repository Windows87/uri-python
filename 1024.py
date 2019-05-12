x = input()

for i in range(x):
    y = raw_input()
    r1 = ""
    r2 = ""
    r3 = ""

    for l in y:
        if l.isupper() or l.islower(): 
            l = chr(ord(l) + 3)
        r1 += l

    i2 = len(r1) - 1
    while i2 >= 0:
        r2 += r1[i2]
        i2 -= 1

    m = len(r2)/2

    for i2 in range(len(r2)):
        if(i2 >= m):
            l = chr(ord(r2[i2]) - 1)
        else:
            l = r2[i2]
        r3 += l

    print(r3)
    
