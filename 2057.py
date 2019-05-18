a, b, c = (raw_input()).split(' ')
a = int(a)
b = int(b)
c = int(c)

r = a + b + c

if r >= 24:
    print r - 24
elif r < 0:
    print r + 24
else:
    print r
