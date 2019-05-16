x = input()

for i in range(x):
    y, z = (raw_input()).split(' ')
    y = int(y)
    z = int(z)
    s = 0
    n = 0
    i2 = 0

    while n != z:
        if (y + i2) % 2 != 0:
            n += 1
            s += y + i2
        i2 += 1
    

    print s
