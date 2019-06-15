x = raw_input().split(' ')
y = raw_input().split(' ')

ok = True

for nIndex in range(len(x)):
    if x[nIndex] == y[nIndex]:
        ok = False
        break

if ok:
    print "Y"
else:
    print "N"