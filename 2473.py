selecs = raw_input().split(' ')
sort = raw_input().split(' ')
n = 0

for selec in selecs:
    try:
        sort.index(selec)
        n += 1
    except ValueError:
        continue

if n == 3:
    print "terno"
elif n == 4:
    print "quadra"
elif n == 5:
    print "quina"
elif n == 6:
    print "sena"
else:
    print "azar"