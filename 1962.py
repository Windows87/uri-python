n = input()

for nIndex in range(n):
    x = input()
    if x - 2014 > 0:
        print str(x - 2014) + ' A.C.'
    else:
        print str(2014 - x + 1) + ' D.C.'