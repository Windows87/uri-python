n, maxH = raw_input().split(' ')
n = int(n)
maxH = int(maxH)
pas = []

for nIndex in range(n):
    x = raw_input()
    h = x.split(' ')
    h = int(h[len(h) - 1])

    if h > maxH:
        pas.insert(len(pas), x.replace(' ' + str(h), ''))

for e in pas:
    print e
