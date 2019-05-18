x = input()
m = 0
n = 0

for i in range(x):
    y, z = (raw_input()).split(' ')
    if float(z) > m:
        m = float(z)
        n = y

if m < 8:
    print "Minimum note not reached"
else:
    print n
