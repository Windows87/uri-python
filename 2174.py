n = input()
ab = []

for nIndex in range(n):
    p = raw_input().lower()
    try:
        ab.index(p)
    except ValueError:
        ab.insert(len(ab), p)

print 'Falta(m) ' + str(151 - len(ab)) + ' pomekon(s).'