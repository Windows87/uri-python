n = input()
p = 0
ap = 0

for nIndex in range(n):
    t = raw_input()
    if p == -1:
        continue

    if t[0] == '.':
        ap += 1
    else:
        if ap == 1 or ap == 2:
            ap = 0
            p += 1
        elif ap >= 3:
            p = -1

if ap == 1 or ap == 2:
    p += 1
elif ap >= 3:
    p = -1
    
if p == -1:
    print "N"
else:
    print p