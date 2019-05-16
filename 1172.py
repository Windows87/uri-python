l = []

for i in range(10):
    y = input()
    if y <= 0:
        y = 1
    l.insert(len(l), y)

for i in range(10):
    print "X[" + str(i) + "] = " + str(l[i])
