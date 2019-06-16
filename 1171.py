n = input()
d = []
q = []

for nIndex in range(n):
    k = input()

    try:
        dIn = d.index(k)
        q[dIn] += 1
    except ValueError:
        d.insert(len(d), k)
        q.insert(len(q), 1)

sor = sorted(d)

for e in sor:
    ap = q[d.index(e)]
    print str(e) + ' aparece ' + str(ap) + ' vez(es)'